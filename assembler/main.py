import json

from antlr4 import *
from macro_processor import process_macros, read_mlb
from assembler import ObjectModule, assemble
from ast_builder import build_ast
from linker import link
import os.path
import sys
import pathlib
from dataclasses import asdict


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
    # TODO: write code locations
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

    exts = dict()
    for sect in obj.asects + obj.rsects:
        for ext_name in sect.ext_uses:
            sections_using_ext = obj.exts.setdefault(ext_name, dict())
            ext_uses = sections_using_ext.setdefault(sect.name, [])
            ext_uses.extend(sect.ext_uses[ext_name])

    for ext_name in exts:
        f.write(f'XTRN {ext_name}:')
        for sect_name in exts[ext_name]:
            f.write(' ' + ' '.join([f'{sect_name} {offset:02x}' for offset in exts[ext_name][sect_name]]))
        f.write('\n')

    f.close()


if __name__ == '__main__':
    library_macros = read_mlb(str(pathlib.Path(__file__).parent.joinpath('standard.mlb').absolute()))
    source_files = sys.argv[1:]
    objects = []
    for filepath in source_files:
        root, ext = os.path.splitext(filepath)
        input_stream = FileStream(filepath)
        macro_expanded_input_stream = process_macros(input_stream, library_macros, str(pathlib.Path(filepath).absolute()))
        # print(macro_expanded_input_stream)
        r = build_ast(macro_expanded_input_stream, str(pathlib.Path(filepath).absolute()))
        obj = assemble(r)

        write_object_file(root + '.obj', obj)
        objects.append(obj)

    data, code_locations = link(objects)
    image_root, _ = os.path.splitext(source_files[0])
    write_image(image_root + '.img', data)

    # write code locations(debug info)
    code_locations = {key: asdict(loc) for key, loc in code_locations.items()}
    json_locations = json.dumps(code_locations, indent=4, sort_keys=True)
    with open(image_root + '.dbg.json', 'w') as f:
        f.write(json_locations)
