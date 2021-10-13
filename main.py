from antlr4 import *
from generated.AsmParser import AsmParser
from generated.AsmLexer import AsmLexer
from generated.AsmParserVisitor import AsmParserVisitor
from enum import Enum, auto
from typing import Union
from dataclasses import dataclass, field
from intructions import instructions as insset
import inspect
import bitstruct


@dataclass()
class RegisterNode:
    number: int

@dataclass()
class LabelNode:
    name: str

@dataclass()
class InstructionNode:
    opcode: str
    arguments: list[Union[int, str, RegisterNode, LabelNode]]





@dataclass()
class SectionNode:
    class Kind(Enum):
        ASECT = "asect"
    kind: Kind
    address: int
    lines: list[Union[InstructionNode, LabelNode]]


@dataclass()
class ProgramNode:
    sections: list[SectionNode]



class BuildAstVisitor(AsmParserVisitor):
    def visitProgram(self, ctx:AsmParser.ProgramContext) -> ProgramNode:
        ret = ProgramNode([])
        for child in filter(lambda a: isinstance(a, AsmParser.SectionContext), ctx.children):
            ret.sections.append(self.visitSection(child))
        return ret

    def visitSection(self, ctx:AsmParser.SectionContext) -> SectionNode:
        header = ctx.section_header()  # type: AsmParser.Section_headerContext
        kind = header.SECTION_TYPE().symbol.text
        address = self.visitNumber(header.number())
        lines = self.visitSection_body(ctx.section_body())
        # print(kind, type(kind))
        return SectionNode(SectionNode.Kind(kind), address, lines)

    def visitNumber(self, ctx:AsmParser.NumberContext) -> int:
        return int(ctx.children[0].symbol.text, 0)

    def visitSection_body(self, ctx:AsmParser.Section_bodyContext) -> list[Union[InstructionNode, LabelNode]]:
        ret = []
        for c in ctx.children:
            if isinstance(c, AsmParser.StandaloneLabelContext):
                ret.append(self.visitStandaloneLabel(c))
            elif isinstance(c, AsmParser.InstructionLineContext):
                ret += self.visitInstructionLine(c)
        return ret

    def visitStandaloneLabel(self, ctx:AsmParser.StandaloneLabelContext) -> LabelNode:
        return self.visitLabel(ctx.label())

    def visitLabel(self, ctx:AsmParser.LabelContext) -> LabelNode:
        return LabelNode(ctx.getText())

    def visitString(self, ctx:AsmParser.StringContext):
        return ctx.getText()

    def visitRegister(self, ctx:AsmParser.RegisterContext):
        return RegisterNode(int(ctx.getText()[1:]))

    def visitInstructionLine(self, ctx:AsmParser.InstructionLineContext) -> list[Union[LabelNode, InstructionNode]]:
        ret = []
        if ctx.label() is not None:
            ret.append(self.visitLabel(ctx.label()))
        op = ctx.instruction().children[0].symbol.text
        args = self.visitArguments(ctx.arguments()) if ctx.arguments() is not None else []
        ret.append(InstructionNode(op, args))
        return ret

    def visitArguments(self, ctx:AsmParser.ArgumentsContext):
        return [self.visitArgument(i) for i in ctx.children if isinstance(i, AsmParser.ArgumentContext)]




def printAst(p: ProgramNode):
    for section in p.sections:
        print(section.kind.value, section.address)
        for line in section.lines:
            if isinstance(line, LabelNode):
                print(f'\t{line.name}:')
            else:
                print(f'\t{line.opcode}\t{", ".join(map(lambda a: str(a),line.arguments))}')


@dataclass()
class BinPiece:
    size: int


@dataclass()
class AddressPiece(BinPiece):
    label_name: str
    size = 4


@dataclass()
class DataPiece(BinPiece):
    data: bytearray



class InstructionAssembler:
    def __init__(self):
        self.instructions = {}
        self.handlers = dict(map(lambda a: (a[0].removesuffix('_handler'), a[1]),filter(lambda a: a[0].endswith('handler'), inspect.getmembers(self, inspect.ismethod))))
        for category, instructions in insset.items():
            for instruction, opcode in instructions.items():
                self.instructions[instruction] = (opcode, self.handlers[category])

    def assemble(self, i: InstructionNode) -> list[BinPiece]:
        num_opcode, handler = self.instructions[i.opcode]
        return handler(num_opcode, i.arguments)

    @staticmethod
    def assert_args(args, *types):
        if len(types) != len(args):
            raise Exception
        # for i in range(len(args)):
        #     t = types[i]
        #     if not isinstance(args[i], t):
        #         raise Exception


    def binary_handler(self, opcode: int, arguments: list[Union[int, str, RegisterNode]]):
        self.assert_args(arguments, RegisterNode, RegisterNode)
        data = bitstruct.pack("u4u2u2", opcode // 16, arguments[0].number, arguments[1].number)
        return [DataPiece(1, bytearray(data))]

    def unary_handler(self, opcode: int, arguments: list[Union[int, str, RegisterNode]]):
        self.assert_args(arguments, RegisterNode)
        return [DataPiece(1, bytearray(bitstruct.pack('u6u2', opcode // 4, arguments[0].number)))]

    def zero_handler(self, opcode: int, arguments: list[Union[int, str, RegisterNode]]):
        self.assert_args(arguments)
        return [DataPiece(1, bytearray([opcode]))]

    def branch_handler(self, opcode: int, arguments: list[Union[int, str, RegisterNode, LabelNode]]):
        self.assert_args(arguments, Union[int, LabelNode])

        if isinstance(arguments[0], LabelNode):
            b2 = AddressPiece(1, arguments[0].name)
        else:
            b2 = DataPiece(1, bytearray([arguments[0]]))

        return [DataPiece(1, bytearray([opcode])), b2]

    # TODO: this is a stub
    def dc_handler(self, opcode: int, arguments: list[Union[int, str, RegisterNode, LabelNode]]):
        return [DataPiece(1, bytearray([i])) for i in arguments]

    # TODO: this is a stub
    def ldi_handler(self, opcode: int, arguments: list[Union[int, str, RegisterNode, LabelNode]]):
        if isinstance(arguments[1], LabelNode):
            b2 = AddressPiece(1, arguments[1].name)
        else:
            b2 = DataPiece(1, bytearray([arguments[1]]))
        return self.unary_handler(opcode, [arguments[0]]) + [b2]


@dataclass()
class Section:
    def __init__(self):
        self.size = 0
        self.data: list[BinPiece] = list()
        self.labels: dict[str, int] = dict()
        self.address = 0
        self.instruction_assembler = InstructionAssembler()


    def assemble(self, sn: SectionNode):
        self.address = sn.address

        for line in sn.lines:
            if isinstance(line, LabelNode):
                if line.name in self.labels.keys():
                    raise Exception
                self.labels[line.name] = self.size
            elif isinstance(line, InstructionNode):
                pieces = self.instruction_assembler.assemble(line)
                for piece in pieces:
                    self.size += piece.size
                    self.data.append(piece)
        return self


class Linker:
    def __init__(self):
        pass

    def link(self, sections: list[Section]):
        labels = dict()
        data = [-1] * 256
        for section in sections:
            for name, offset in section.labels.items():
                labels[name] = offset + section.address
        for section in sections:
            addr = section.address
            for piece in section.data:
                if isinstance(piece, AddressPiece):
                    data[addr] = labels[piece.label_name]
                    addr += 1
                elif isinstance(piece, DataPiece):
                    for b in piece.data:
                        data[addr] = b
                        addr += 1

        for i in range(len(data)):
            if data[i] == -1:
                data[i] = 0
        # TODO: check colliding sections
        return data


def write_image(filename: str, arr: list):
    """
    Write the contents or array into file in logisim-compatible format

    :param filename: Path to output file
    :param arr: Array to be written
    """
    f = open(filename, mode='wb')
    f.write(bytes("v2.0 raw\n", 'UTF-8'))
    for byte in arr:
        f.write(bytes('%08x' % byte + '\n', 'UTF-8'))
    f.close()




if __name__ == '__main__':
    lexer = AsmLexer(FileStream('test.asm'))
    tokenStream = CommonTokenStream(lexer)
    parser = AsmParser(tokenStream)
    cst = parser.program()
    # tokenStream.fill()
    r = BuildAstVisitor().visit(cst) # type: ProgramNode
    # printAst(r)
    sections = [Section().assemble(i) for i in r.sections]
    data = Linker().link(sections)
    for i in range(256):
        print("{0:02x}".format(data[i]), end=' ')
        i += 1
        if i % 16 == 0:
            print()

    write_image('test.img', data[:128])

    # for section in r.sections:
    #     j = 0
    #     for p in asm_section(section):
    #         if isinstance(p, DataPiece):
    #             for b in p.data:
    #                 print("{0:02x}".format(b), end=' ')
    #                 j+=1
    #                 if j % 16 == 0:
    #                     print()
    #         else:
    #             print('ZZ ', end='')
    #             j += 1
    #             if j % 16 == 0:
    #                 print()
    #     print()
    #     print()

# import lark
# gf = open("test.lark", 'r')
# l = lark.Lark(gf, debug=True, parser='lalr')
# f = open('test.asm', 'r')
# asmtext = f.read()
# print(l.parse(asmtext))