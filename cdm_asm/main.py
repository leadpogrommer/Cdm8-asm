import codecs
import json

import colorama
from antlr4 import *

from cdm_asm.error import CdmException
from cdm_asm.macro_processor import process_macros, read_mlb
from cdm_asm.assembler import ObjectModule, assemble
from cdm_asm.ast_builder import build_ast
from cdm_asm.linker import link
import os.path
import sys
from dataclasses import asdict
import pathlib
import os
import argparse


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


def main():
    # TODO: enable object file generation (when stand-alone linker will be ready)
    parser = argparse.ArgumentParser('Cdm8e assembler')
    # parser.add_argument('-o', '--object', type=str, help='Object file directory (object files will be stored here)')
    parser.add_argument('-i', '--image', type=str, help='Image file path')
    parser.add_argument('-d', '--debug', type=str, help='Debug info path')
    parser.add_argument('sources', type=str, nargs='+', help='Source files')
    args = parser.parse_args()

    colorama.init()

    try:
        library_macros = read_mlb(str(pathlib.Path(__file__).parent.joinpath('standard.mlb').absolute()))
        source_files = args.sources
        objects = []
        for filepath in source_files:
            with open(filepath, 'rb') as file:
                data = file.read()
                data = codecs.decode(data, 'ascii', 'strict')
                # tolerate files without newline at the end
                if data[-1] != '\n':
                    data += '\n'
                input_stream = InputStream(data)

            macro_expanded_input_stream = process_macros(input_stream, library_macros, str(pathlib.Path(filepath).absolute()))
            # print(macro_expanded_input_stream)
            r = build_ast(macro_expanded_input_stream, str(pathlib.Path(filepath).absolute()))
            obj = assemble(r)

            objects.append(obj)

        data, code_locations = link(objects)
        image_root, _ = os.path.splitext(source_files[0])
        if args.image is not None:
            write_image(args.image, data)

        # write code locations(debug info)
        code_locations = {key: asdict(loc) for key, loc in code_locations.items()}
        json_locations = json.dumps(code_locations, indent=4, sort_keys=True)
        if args.debug is not None:
            with open(args.debug, 'w') as f:
                f.write(json_locations)
    except CdmException as e:
        e.log()
        exit(1)


if __name__ == '__main__':
    main()