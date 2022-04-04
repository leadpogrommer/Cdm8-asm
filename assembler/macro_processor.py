from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from dataclasses import dataclass
from generated.MacroLexer import MacroLexer
from generated.MacroParser import MacroParser
from generated.MacroVisitor import MacroVisitor
from typing import Union
import re


def unique(params: list[str]):
    register_available = [True] * 4
    var_params = []
    for param in params:
        param_match = re.fullmatch(r'r(\d)', param)
        if param_match:
            register_number = int(param_match.group(1))
            if not register_available[register_number]:
                raise Exception(f'unique: {param} appears multiple times')
            register_available[register_number] = False
        else:
            var_params.append(param)

    i = 0
    defined_vars = dict()
    for param in var_params:
        while not register_available[i]:
            i += 1
            if i == 4:
                raise Exception(f'unique: not enough registers')
        register_available[i] = False
        defined_vars[param] = f'r{i}'
    return defined_vars

macro_instructions = {
    'unique': unique,
}


@dataclass
class MacroParameter:
    n: int
@dataclass
class MacroNonce:
    pass

@dataclass
class MacroVariable:
    name_pieces: list

@dataclass
class MacroLine:
    label_pieces: list
    instruction_pieces: list
    parameter_pieces: list[list]

@dataclass
class MacroDefinition:
    name: str
    arity: int
    lines: list[MacroLine]


def substitute_piece(piece, params: list[str], nonce: str, variables: dict[str, str]):
    if isinstance(piece, MacroParameter):
        return params[piece.n - 1]
    elif isinstance(piece, MacroNonce):
        return nonce
    elif isinstance(piece, MacroVariable):
        sub = lambda p: substitute_piece(p, params, nonce, variables)
        var_name = ''.join(map(sub, piece.name_pieces))
        return variables[var_name]
    else:
        return piece

def substitute_pieces_in_line(line: MacroLine, params: list[str], nonce: str, variables: dict[str, str]):
    sub = lambda p: substitute_piece(p, params, nonce, variables)
    sub_all = lambda ps: ''.join(map(sub, ps))
    label_part = sub_all(line.label_pieces)
    instruction_part = sub_all(line.instruction_pieces)
    parameter_parts = list(map(sub_all, line.parameter_pieces))
    return (label_part, instruction_part, parameter_parts)

class ExpandMacrosVisitor(MacroVisitor):
    def __init__(self, rewriter=None, mlb_macros=dict()):
        self.nonce = 0
        self.macros = {name: mlb_macros[name].copy() for name in mlb_macros}
        self.rewriter = rewriter

    def add_macro(self, macro: MacroDefinition):
        if macro.name not in self.macros:
            self.macros[macro.name] = dict()
        if macro.arity in self.macros[macro.name]:
            raise Exception(f'Multiple definitions of macro {macro.name}')
        self.macros[macro.name][macro.arity] = macro

    def expand_macro(self, macro_name: str, macro_params: list[str]):
        arity = len(macro_params)
        if macro_name in self.macros and arity in self.macros[macro_name]:
            ret_parts = []
            self.nonce += 1
            macro_nonce = str(self.nonce)
            macro = self.macros[macro_name][arity]
            variables = {}
            for line in macro.lines:
                label_part, instruction_part, parameter_parts \
                    = substitute_pieces_in_line(line, macro_params, macro_nonce, variables)
                label = label_part.rstrip()
                instruction = instruction_part.strip()
                parameters = list(map(str.strip, parameter_parts))
                if parameters == ['']:
                    parameters = []

                if instruction in macro_instructions:
                    variables.update(macro_instructions[instruction](parameters))
                    if label != '':
                        ret_parts.append(f'{label}\n')
                else:
                    expanded_text = self.expand_macro(instruction, parameters)
                    if expanded_text is not None:
                        if label != '':
                            ret_parts.append(f'{label}\n')
                        ret_parts.append(expanded_text)
                    else:
                        ret_parts.append(f'{label_part}{instruction_part}{",".join(parameter_parts)}\n')
            return ''.join(ret_parts)
        return None


    def visitMlb(self, ctx: MacroParser.MlbContext):
        for child in filter(lambda c: isinstance(c, MacroParser.Mlb_macroContext), ctx.children):
            self.add_macro(self.visitMlb_macro(child))
        return self.macros

    def visitProgram(self, ctx: MacroParser.ProgramContext):
        for child in ctx.children:
            if isinstance(child, MacroParser.MacroContext):
                self.add_macro(self.visitMacro(child))
            elif isinstance(child, MacroParser.LineContext):
                label, instruction, parameters = self.visitLine(child)
                expanded_text = self.expand_macro(instruction, parameters)
                if expanded_text is not None:
                    if label != '':
                        expanded_text = f'{label}\n{expanded_text}'
                    self.rewriter.insertBeforeToken(child.start, expanded_text)
                    self.rewriter.delete(self.rewriter.DEFAULT_PROGRAM_NAME, child.start, child.stop)

    def visitMacro(self, ctx: MacroParser.MacroContext):
        header = ctx.macro_header()
        name = header.NAME().getText()
        arity = int(header.DIGIT().getText())
        lines = self.visitMacro_body(ctx.macro_body())
        self.rewriter.delete(self.rewriter.DEFAULT_PROGRAM_NAME, ctx.start, ctx.stop)
        return MacroDefinition(name, arity, lines)

    def visitMlb_macro(self, ctx: MacroParser.Mlb_macroContext):
        header = ctx.mlb_header()
        name = header.NAME().getText()
        arity = int(header.DIGIT().getText())
        lines = self.visitMacro_body(ctx.macro_body())
        return MacroDefinition(name, arity, lines)

    def visitMacro_body(self, ctx: MacroParser.Macro_bodyContext):
        lines = []
        for child in ctx.children:
            lines.append(self.visitMacroLine(child))
        return lines

    def visitMacroLine(self, ctx: MacroParser.LineContext):
        label_pieces = self.visitLabels(ctx.labels())
        instruction_pieces = self.visitMacro_item(ctx.instruction()) if ctx.instruction() is not None else []
        parameter_pieces = [self.visitFirst_param(ctx.first_param())] if ctx.first_param() is not None else [[]]
        for param in ctx.getChildren(lambda c: isinstance(c, MacroParser.ParamContext)):
            parameter_pieces.append(self.visitMacro_item(param))
        return MacroLine(label_pieces, instruction_pieces, parameter_pieces)

    def visitLine(self, ctx: MacroParser.LineContext):
        label = ctx.labels().getText().rstrip()
        instruction = ctx.instruction().getText().strip() if ctx.instruction() is not None else ''
        parameters = [ctx.first_param().getText().strip()] if ctx.first_param() is not None else ['']
        for param in ctx.getChildren(lambda c: isinstance(c, MacroParser.ParamContext)):
            parameters.append(param.getText().strip())
        if parameters == ['']:
            parameters = []
        return (label, instruction, parameters)

    def visitLabels(self, ctx: MacroParser.LabelsContext):
        label_pieces = []
        for label in ctx.getChildren(lambda c: isinstance(c, MacroParser.LabelContext)):
            label_pieces.extend(self.visitMacro_item(label))
        if ctx.WS() is not None:
            label_pieces.append(ctx.WS().getText())
        return label_pieces

    def visitFirst_param(self, ctx: MacroParser.First_paramContext):
        param_pieces = self.visitMacro_item(ctx.param()) if ctx.param() is not None else []
        if ctx.WS() is not None:
            param_pieces = [ctx.WS().getText()] + param_pieces
        return param_pieces

    def visitMacro_item(self, ctx):
        item_pieces = []
        for child in ctx.getChildren():
            if isinstance(child, MacroParser.Macro_variableContext):
                item_pieces.append(self.visitMacro_variable(child))
            elif isinstance(child, MacroParser.Macro_pieceContext):
                item_pieces.append(self.visitMacro_piece(child))
            else:
                item_pieces.append(child.getText())
        return item_pieces

    def visitMacro_variable(self, ctx: MacroParser.Macro_variableContext):
        name_pieces = []
        for child in ctx.children[1:]:
            name_pieces.append(self.visitMacro_piece(child))
        return MacroVariable(name_pieces)

    def visitMacro_piece(self, ctx: MacroParser.Macro_pieceContext):
        if ctx.macro_text() is not None:
            return ctx.macro_text().getText()
        elif ctx.macro_param() is not None:
            return MacroParameter(int(ctx.macro_param().DIGIT().getText()))
        elif ctx.macro_nonce() is not None:
            return MacroNonce()

def read_mlb(filepath='standard.mlb'):
    input_stream = FileStream(filepath)
    lexer = MacroLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MacroParser(token_stream)
    cst = parser.mlb()
    return ExpandMacrosVisitor().visit(cst)

def process_macros(input_stream: InputStream, library_macros=dict()):
    lexer = MacroLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MacroParser(token_stream)
    cst = parser.program()
    rewriter = TokenStreamRewriter(token_stream)
    ExpandMacrosVisitor(rewriter, library_macros).visit(cst)
    return InputStream(rewriter.getDefaultText())
