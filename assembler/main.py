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
        f.write(f'ABS  {asect.address:04x}: ')
        f.write(' '.join([f'{b:02x}' for b in asect.data]) + '\n')

    for asect in obj.asects:
        for ent in asect.ents:
            f.write(f'NTRY {ent} {asect.ents[ent]:04x}\n')

    for rsect in obj.rsects:
        f.write(f'NAME {rsect.name}\n')
        f.write('DATA ' + ' '.join([f'{b:02x}' for b in rsect.data]) + '\n')
        f.write('RELL ' + ' '.join([f'{a:04x}' for a in rsect.rell])  + '\n')
        f.write('RELH ' + ' '.join([f'{a:04x} {b:02x}' for a, b in rsect.relh])  + '\n')
        for ent in rsect.ents:
            f.write(f'NTRY {ent} {rsect.ents[ent]:04x}\n')

    xtrl = dict()
    for sect in obj.asects + obj.rsects:
        for ext_name in sect.xtrl:
            sections_using_ext = xtrl.setdefault(ext_name, dict())
            xtrl_uses = sections_using_ext.setdefault(sect.name, [])
            xtrl_uses.extend(sect.xtrl[ext_name])

    xtrh = dict()
    for sect in obj.asects + obj.rsects:
        for ext_name in sect.xtrh:
            sections_using_ext = xtrh.setdefault(ext_name, dict())
            xtrh_uses = sections_using_ext.setdefault(sect.name, [])
            xtrh_uses.extend(sect.xtrh[ext_name])

    for ext_name in xtrl:
        f.write(f'XTRL {ext_name}:')
        for sect_name in xtrl[ext_name]:
            f.write(' ' + ' '.join([f'{sect_name} {a:04x}' for a in xtrl[ext_name][sect_name]]))
        f.write('\n')

    for ext_name in xtrh:
        f.write(f'XTRH {ext_name}:')
        for sect_name in xtrh[ext_name]:
            f.write(' ' + ' '.join([f'{sect_name} {a:04x} {b:02x}' for a, b in xtrh[ext_name][sect_name]]))
        f.write('\n')

    f.close()


if __name__ == '__main__':
    library_macros = read_mlb(pathlib.Path(__file__).parent.joinpath('standard.mlb'))
    source_files = sys.argv[1:]
    objects = []
    for filepath in source_files:
        root, ext = os.path.splitext(filepath)
        input_stream = FileStream(filepath, 'utf8')
        macro_expanded_input_stream = process_macros(input_stream, library_macros)
        r = build_ast(macro_expanded_input_stream)
        obj = assemble(r)

        for section_arr in (obj.asects, obj.rsects):
            for section in section_arr:
                for location in section.code_locations.values():
                    location.file = filepath

        write_object_file(root + '.obj', obj)
        objects.append(obj)

    data, code_locations = link(objects)
    image_root, _ = os.path.splitext(source_files[0])
    write_image(image_root + '.img', data)

    # write code locations(debug info)
    code_locations = {key: asdict(loc) for key, loc in code_locations.items()}
    json_locations = json.dumps(code_locations)
    with open(image_root + '.dbg.json', 'w') as f:
        f.write(json_locations)
