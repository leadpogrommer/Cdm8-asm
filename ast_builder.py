from antlr4 import *
from ast_nodes import *
from generated.AsmParser import AsmParser
from generated.AsmParserVisitor import AsmParserVisitor


class BuildAstVisitor(AsmParserVisitor):
    def visitProgram(self, ctx:AsmParser.ProgramContext) -> ProgramNode:
        ret = ProgramNode([], [], [])
        for child in filter(lambda a: isinstance(a, AsmParser.SectionContext), ctx.children):
            if isinstance(child, AsmParser.AbsoluteSectionContext):
                ret.absolute_sections.append(self.visitAbsoluteSection(child))
            elif isinstance(child, AsmParser.RelocatableSectionContext):
                ret.relocatable_sections.append(self.visitRelocatableSection(child))
            elif isinstance(child, AsmParser.TemplateSectionContext):
                ret.template_sections.append(self.visitTemplateSection(child))
        return ret

    def visitAbsoluteSection(self, ctx:AsmParser.AbsoluteSectionContext) -> AbsoluteSectionNode:
        header = ctx.asect_header()
        lines = self.visitSection_body(ctx.section_body())
        address = self.visitNumber(header.number())
        return AbsoluteSectionNode(lines, address)

    def visitRelocatableSection(self, ctx:AsmParser.RelocatableSectionContext) -> RelocatableSectionNode:
        header = ctx.rsect_header()
        lines = self.visitSection_body(ctx.section_body())
        name = header.name().getText()
        return RelocatableSectionNode(lines, name)

    def visitTemplateSection(self, ctx:AsmParser.TemplateSectionContext) -> TemplateSectionNode:
        header = ctx.tplate_header()
        lines = self.visitSection_body(ctx.section_body())
        name = header.name().getText()
        return TemplateSectionNode(lines, name)

    def visitNumber(self, ctx:AsmParser.NumberContext) -> int:
        return int(ctx.getText(), base=0)

    def visitSection_body(self, ctx:AsmParser.Section_bodyContext) -> list:
        ret = []
        for c in ctx.children:
            if isinstance(c, AsmParser.StandaloneLabelContext):
                ret.append(self.visitStandaloneLabel(c))
            elif isinstance(c, AsmParser.InstructionLineContext):
                ret += self.visitInstructionLine(c)
        return ret

    def visitStandaloneLabel(self, ctx:AsmParser.StandaloneLabelContext) -> LabelNode:
        label_decl = self.visitLabel_declaration(ctx.label_declaration())
        label_decl.external = ctx.EXT() is not None
        if label_decl.entry and label_decl.external:
            raise Exception(f'Label {label_decl.label.name} cannot be both external and entry')
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
        return TemplateFieldNode(template_name, field_name, ctx.MINUS() is not None)

    def visitInstructionLine(self, ctx:AsmParser.InstructionLineContext) -> list:
        ret = []
        if ctx.label_declaration() is not None:
            ret.append(self.visitLabel_declaration(ctx.label_declaration()))
        op = ctx.instruction().getText()
        args = self.visitArguments(ctx.arguments()) if ctx.arguments() is not None else []
        ret.append(InstructionNode(op, args))
        return ret

    def visitArguments(self, ctx:AsmParser.ArgumentsContext):
        return [self.visitArgument(i) for i in ctx.children if isinstance(i, AsmParser.ArgumentContext)]

def build_ast(cst: AsmParser.ProgramContext):
    return BuildAstVisitor().visit(cst)
