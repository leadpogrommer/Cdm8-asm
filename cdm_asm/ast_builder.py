from antlr4 import *
from cdm_asm.ast_nodes import *
from cdm_asm.generated.AsmLexer import AsmLexer
from cdm_asm.generated.AsmParser import AsmParser
from cdm_asm.generated.AsmParserVisitor import AsmParserVisitor
from base64 import b64decode
from cdm_asm.error import AntlrErrorListener, CdmExceptionTag, CdmException


class BuildAstVisitor(AsmParserVisitor):
    def __init__(self, filepath: str):
        super().__init__()
        self.line_offset = 0
        # self.line_offset = 0
        self.source_path = filepath
        self.line_offset = 0


    def visitProgram(self, ctx:AsmParser.ProgramContext) -> ProgramNode:
        ret = ProgramNode([], [], [])
        for child in ctx.children:
            if isinstance(child, AsmParser.AbsoluteSectionContext):
                ret.absolute_sections.append(self.visitAbsoluteSection(child))
            elif isinstance(child, AsmParser.RelocatableSectionContext):
                ret.relocatable_sections.append(self.visitRelocatableSection(child))
            elif isinstance(child, AsmParser.TemplateSectionContext):
                ret.template_sections.append(self.visitTemplateSection(child))
            elif isinstance(child, AsmParser.Line_markContext):
                self.visitLine_mark(child)
        return ret

    def visitAbsoluteSection(self, ctx:AsmParser.AbsoluteSectionContext) -> AbsoluteSectionNode:
        header = ctx.asect_header()
        lines, locations = self.visitSection_body(ctx.section_body())
        address = self.visitNumber(header.number())
        return AbsoluteSectionNode(lines, locations, address)

    def visitRelocatableSection(self, ctx:AsmParser.RelocatableSectionContext) -> RelocatableSectionNode:
        header = ctx.rsect_header()
        lines, locations = self.visitSection_body(ctx.section_body())
        name = header.name().getText()
        return RelocatableSectionNode(lines, locations, name)

    def visitTemplateSection(self, ctx:AsmParser.TemplateSectionContext) -> TemplateSectionNode:
        header = ctx.tplate_header()
        lines, locations = self.visitSection_body(ctx.section_body())
        name = header.name().getText()
        return TemplateSectionNode(lines, locations, name)

    def visitLine_mark(self, ctx:AsmParser.Line_markContext):
        # TODO: use already parsed values
        value = int(ctx.line_number().getText())
        filepath = b64decode(ctx.filepath().getText()[3:]).decode()
        self.source_path = filepath
        self.line_offset = ctx.start.line - value + 1


    def visitNumber(self, ctx:AsmParser.NumberContext) -> int:
        return int(ctx.getText(), base=0)

    def visitCharacter(self, ctx: AsmParser.CharacterContext) -> int:
        if ctx.getText()[1] == '\\':
            return ord(ctx.getText()[2])
        else:
            return ord(ctx.getText()[1])

    def visitSection_body(self, ctx:AsmParser.Section_bodyContext) -> tuple[list, list[CodeLocation]]:
        return self.visitCode_block(ctx.code_block(), return_locations=True)

    def visitConditional(self, ctx: AsmParser.ConditionalContext):
        conditions = self.visitConditions(ctx.conditions())
        then_lines = self.visitCode_block(ctx.code_block())
        else_lines = self.visitElse_clause(ctx.else_clause()) if ctx.else_clause() else []
        return ConditionalStatementNode(conditions, then_lines, else_lines)

    def visitConditions(self, ctx: AsmParser.ConditionsContext):
        conditions = []
        for cond in ctx.connective_condition():
            conditions.append(self.visitConnective_condition(cond))
        conditions.append(self.visitCondition(ctx.condition()))
        return conditions

    def visitConnective_condition(self, ctx: AsmParser.Connective_conditionContext):
        cond = self.visitCondition(ctx.condition())
        cond.conjunction = ctx.conjunction().getText()
        if cond.conjunction != 'and' and cond.conjunction != 'or':
            raise CdmException(CdmExceptionTag.ASM, self.source_path, ctx.start.line - self.line_offset, 'Expected "and" or "or" in compound condition')
        return cond

    def visitCondition(self, ctx: AsmParser.ConditionContext):
        lines = self.visitCode_block(ctx.code_block())
        return ConditionNode(lines, ctx.branch_mnemonic().getText(), None)

    def visitElse_clause(self, ctx: AsmParser.Else_clauseContext):
        return self.visitCode_block(ctx.code_block())

    def visitWhile_loop(self, ctx: AsmParser.While_loopContext):
        condition_lines = self.visitWhile_condition(ctx.while_condition())
        lines = self.visitCode_block(ctx.code_block())
        return WhileLoopNode(condition_lines, ctx.branch_mnemonic().getText(), lines)

    def visitWhile_condition(self, ctx: AsmParser.While_conditionContext):
        return self.visitCode_block(ctx.code_block())

    def visitUntil_loop(self, ctx: AsmParser.Until_loopContext):
        lines = self.visitCode_block(ctx.code_block())
        return UntilLoopNode(lines, ctx.branch_mnemonic().getText())

    def visitSave_restore_statement(self, ctx: AsmParser.Save_restore_statementContext):
        saved_register = self.visitSave_statement(ctx.save_statement())
        restored_register = self.visitRestore_statement(ctx.restore_statement())
        if restored_register is None: restored_register = saved_register
        lines = self.visitCode_block(ctx.code_block())
        return SaveRestoreStatementNode(saved_register, lines, restored_register)

    def visitSave_statement(self, ctx: AsmParser.Save_statementContext):
        return self.visitRegister(ctx.register())

    def visitRestore_statement(self, ctx: AsmParser.Restore_statementContext):
        return self.visitRegister(ctx.register()) if ctx.register() else None

    def visitGoto_statement(self, ctx: AsmParser.Goto_statementContext):
        return GotoStatementNode(ctx.branch_mnemonic().getText(), self.visitGoto_argument(ctx.goto_argument()))

    def visitCode_block(self, ctx: AsmParser.Code_blockContext, return_locations=False):
        if ctx.children is None:
            if return_locations:
                return [], []
            else:
                return []

        locations = []
        ret = []
        for c in ctx.children:
            if isinstance(c, AsmParser.StandaloneLabelContext):
                ret.append(self.visitStandaloneLabel(c))
            elif isinstance(c, AsmParser.InstructionLineContext):
                ret += self.visitInstructionLine(c)
            elif isinstance(c, AsmParser.ConditionalContext):
                ret.append(self.visitConditional(c))
            elif isinstance(c, AsmParser.While_loopContext):
                ret.append(self.visitWhile_loop(c))
            elif isinstance(c, AsmParser.Until_loopContext):
                ret.append(self.visitUntil_loop(c))
            elif isinstance(c, AsmParser.Save_restore_statementContext):
                ret.append(self.visitSave_restore_statement(c))
            elif isinstance(c, AsmParser.Break_statementContext):
                ret.append(BreakStatementNode())
            elif isinstance(c, AsmParser.Continue_statementContext):
                ret.append(ContinueStatementNode())
            elif isinstance(c, AsmParser.Goto_statementContext):
                ret.append(self.visitGoto_statement(c))
            elif isinstance(c, AsmParser.Line_markContext):
                self.visit(c)
            while len(locations) < len(ret):
                locations.append(CodeLocation(self.source_path, c.start.line - self.line_offset))
        if return_locations:
            return ret, locations
        else:
            return ret

    def visitByte_expr(self, ctx: AsmParser.Byte_exprContext):
        expr = self.visitAddr_expr(ctx.addr_expr())
        expr.byte_specifier = ctx.byte_specifier().getText()
        return expr

    def visitAddr_expr(self, ctx: AsmParser.Addr_exprContext):
        add_terms = []
        sub_terms = []
        const_term = 0
        for c in ctx.children:
            term = self.visitTerm(c.term())
            if c.MINUS() is not None:
                if isinstance(term, int):
                    const_term -= term
                else:
                    sub_terms.append(term)
            else:
                if isinstance(term, int):
                    const_term += term
                else:
                    add_terms.append(term)
        return RelocatableExpressionNode(None, add_terms, sub_terms, const_term)

    def visitStandaloneLabel(self, ctx:AsmParser.StandaloneLabelContext) -> LabelNode:
        label_decl = self.visitLabel_declaration(ctx.label_declaration())
        label_decl.external = ctx.Ext() is not None
        if label_decl.entry and label_decl.external:
            raise CdmException(CdmExceptionTag.ASM, self.source_path, ctx.start.line - self.line_offset, f'Label {label_decl.label.name} cannot be both external and entry')
        return label_decl

    def visitLabel_declaration(self, ctx: AsmParser.Label_declarationContext) -> LabelDeclarationNode:
        is_entry = ctx.ANGLE_BRACKET() is not None
        return LabelDeclarationNode(self.visitLabel(ctx.label()), is_entry, False)

    def visitLabel(self, ctx:AsmParser.LabelContext) -> LabelNode:
        return LabelNode(ctx.getText())

    def visitString(self, ctx:AsmParser.StringContext):
        return ctx.getText()[1:-1]

    def visitRegister(self, ctx:AsmParser.RegisterContext):
        return RegisterNode(int(ctx.getText()[1:]))

    def visitTemplate_field(self, ctx:AsmParser.Template_fieldContext):
        template_name = ctx.name()[0].getText()
        field_name = ctx.name()[1].getText()
        return TemplateFieldNode(template_name, field_name)

    def visitInstructionLine(self, ctx:AsmParser.InstructionLineContext) -> list:
        ret = []
        if ctx.label_declaration() is not None:
            ret.append(self.visitLabel_declaration(ctx.label_declaration()))
        op = ctx.instruction().getText()
        args = self.visitArguments(ctx.arguments()) if ctx.arguments() is not None else []
        ret.append(InstructionNode(op, args, CodeLocation(self.source_path, ctx.start.line - self.line_offset, ctx.start.column)))
        return ret

    def visitArguments(self, ctx:AsmParser.ArgumentsContext):
        return [self.visitArgument(i) for i in ctx.children if isinstance(i, AsmParser.ArgumentContext)]

def build_ast(input_stream: InputStream, filepath: str):
    lexer = AsmLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(AntlrErrorListener(CdmExceptionTag.ASM, filepath))
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = AsmParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(AntlrErrorListener(CdmExceptionTag.ASM, filepath))
    cst = parser.program()
    return BuildAstVisitor(filepath).visit(cst)
