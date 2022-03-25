from antlr4 import *
from generated.AsmLexer import AsmLexer
from generated.AsmParser import AsmParser
from macro_processor import process_macros, read_mlb
from assembler import ObjectModule, assemble
from ast_builder import build_ast
from linker import link
import os.path
import sys
import pathlib


# def printAst(p: ProgramNode):
#     for section in p.sections:
#         print(section.kind.value, section.address)
#         for line in section.lines:
#             if isinstance(line, LabelNode):
#                 print(f'\t{line.name}:')
#             else:
#                 print(f'\t{line.opcode}\t{", ".join(map(lambda a: str(a),line.arguments))}')

def write_image(filename: str, arr: list):
    """
    Write the contents or array into file in logisim-compatible format

    :param filename: Path to output file
    :param arr: Array to be written
    """
    f = open(filename, mode='wb')
    f.write(bytes("v2.0 raw\n", 'UTF-8'))
    for byte in arr:
        f.write(bytes(f'{byte:02x}\n', 'UTF-8'))
    f.close()

def write_object_file(filename: str, obj: ObjectModule):
    f = open(filename, 'w')

    for asect in obj.asects:
        f.write(f'ABS  {asect.address:02x}: ')
        f.write(' '.join([f'{b:02x}' for b in asect.data]) + '\n')

    for asect in obj.asects:
        for ent in asect.ents:
            f.write(f'NTRY {ent} {asect.ents[ent]:02x}\n')

    for rsect in obj.rsects:
        f.write(f'NAME {rsect.name}\n')
        f.write('DATA ' + ' '.join([f'{b:02x}' for b in rsect.data]) + '\n')
        f.write('REL  ' + ' '.join([f'{b:02x}' for b in rsect.rel])  + '\n')
        for ent in rsect.ents:
            f.write(f'NTRY {ent} {rsect.ents[ent]:02x}\n')

    for ext_name in obj.exts:
        f.write(f'XTRN {ext_name}:')
        for sect_name in obj.exts[ext_name]:
            f.write(' ' + ' '.join([f'{sect_name} {offset:02x}' for offset in obj.exts[ext_name][sect_name]]))
        f.write('\n')

    f.close()


if __name__ == '__main__':
    library_macros = read_mlb(pathlib.Path(__file__).parent.joinpath('standard.mlb'))
    source_files = sys.argv[1:]
    objects = []
    for filepath in source_files:
        root, ext = os.path.splitext(filepath)
        input_stream = FileStream(filepath)
        macro_expanded_input_stream = process_macros(input_stream, library_macros)
        lexer = AsmLexer(macro_expanded_input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = AsmParser(token_stream)
        cst = parser.program()
        r = build_ast(cst)
        obj = assemble(r)
        write_object_file(root + '.obj', obj)
        objects.append(obj)

    data = link(objects)
    image_root, _ = os.path.splitext(source_files[0])
    write_image(image_root + '.img', data)
