from asm_commands import instructions as insset, assembly_directives as dirset
from ast_nodes import *
from dataclasses import dataclass
from typing import Union, get_origin, get_args
import bitstruct


ArgAddress = Union[int, LabelNode]
ArgDcConstant = Union[int, str, LabelNode]
ArgLdiConstant = Union[int, str, LabelNode, TemplateFieldNode]
ArgStackOffset = Union[int, TemplateFieldNode]
ArgLdsaOffset = Union[int, LabelNode, TemplateFieldNode]


@dataclass
class CodeSegment:
    data: bytearray
    label_uses: dict[int, LabelNode]
    tfield_uses: dict[int, TemplateFieldNode]


def assert_args(args, *types, single_type=False):
    ts = [(t if get_origin(t) is None else get_args(t)) for t in types]
    if single_type:
        if len(ts) != 1:
            raise TypeError('Exactly one type must be specified when single_type is True')
        ts = ts * len(args)
    elif len(args) != len(ts):
        raise Exception(f'Expected {len(ts)} arguments, but found {len(args)}')

    for i in range(len(args)):
        if not isinstance(args[i], ts[i]):
            raise Exception(f'Incompatible argument type {type(args[i])}')


def binary_handler(opcode: int, arguments: list) -> list[CodeSegment]:
    assert_args(arguments, RegisterNode, RegisterNode)
    data = bitstruct.pack("u4u2u2", opcode // 16, arguments[0].number, arguments[1].number)
    return CodeSegment(bytearray(data), {}, {})

def unary_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode)
    data = bitstruct.pack('u6u2', opcode // 4, arguments[0].number)
    return CodeSegment(bytearray(data), {}, {})

def zero_handler(opcode: int, arguments: list):
    assert_args(arguments)
    return CodeSegment(bytearray([opcode]), {}, {})

def branch_handler(opcode: int, arguments: list):
    assert_args(arguments, ArgAddress)

    if isinstance(arguments[0], int):
        return CodeSegment(bytearray([opcode, arguments[0]]), {}, {})
    elif isinstance(arguments[0], LabelNode):
        return CodeSegment(bytearray([opcode, 0]), {1: arguments[0]}, {})

def ldsa_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, ArgLdsaOffset)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])

    if isinstance(arg, int):
        cmd_piece.data.append(arg)
        return CodeSegment(cmd_piece.data, {}, {})
    elif isinstance(arg, LabelNode):
        cmd_piece.data.append(0)
        return CodeSegment(cmd_piece.data, {1: arg}, {})
    elif isinstance(arg, TemplateFieldNode):
        if arg.negative:
            raise Exception('Cannot use negative template fields in "ldsa" (at least cocas.py doesn\'t allow it)')
        cmd_piece.data.append(0)
        return CodeSegment(cmd_piece.data, {}, {1: arg})

def ldi_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, ArgLdiConstant)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])

    if isinstance(arg, int):
        cmd_piece.data.append(arg)
        return CodeSegment(cmd_piece.data, {}, {})
    elif isinstance(arg, str):
        arg_data = bytearray(arg, 'utf8')
        if len(arg_data) != 1:
            raise Exception('Argument must be a string of length 1')
        cmd_piece.data.extend(arg_data)
        return CodeSegment(cmd_piece.data, {}, {})
    elif isinstance(arg, LabelNode):
        cmd_piece.data.append(0)
        return CodeSegment(cmd_piece.data, {1: arg}, {})
    elif isinstance(arg, TemplateFieldNode):
        if arg.negative:
            raise Exception('Cannot use negative template fields in "ldi" (at least cocas.py doesn\'t allow it)')
        cmd_piece.data.append(0)
        return CodeSegment(cmd_piece.data, {}, {1: arg})

def osix_handler(opcode: int, arguments: list):
    assert_args(arguments, int)
    arg = arguments[0]

    if arg < 0:
        raise Exception('Cannot use negative numbers in "osix"')
    return CodeSegment(bytearray([opcode, arg]), {}, {})

def spmove_handler(opcode: int, arguments: list):
    assert_args(arguments, ArgStackOffset)
    arg = arguments[0]

    if isinstance(arg, int):
        if arg < 0: arg += 256
        return CodeSegment(bytearray([opcode, arg]), {}, {})
    elif isinstance(arg, TemplateFieldNode):
        return CodeSegment(bytearray([opcode, 0]), {}, {1: arg})


def dc_handler(arguments: list):
    assert_args(arguments, ArgDcConstant, single_type=True)
    if len(arguments) == 0:
        raise Exception('At least one argument must be provided')

    data = bytearray()
    label_uses = dict()

    for arg in arguments:
        if isinstance(arg, int):
            data.append(arg)
        elif isinstance(arg, str):
            data.extend(bytearray(arg, 'utf8'))
        elif isinstance(arg, LabelNode):
            label_uses[len(data)] = arg
            data.append(0)
    return CodeSegment(data, label_uses, {})

def ds_handler(arguments: list):
    assert_args(arguments, int)
    space_size = arguments[0]
    if space_size < 0:
        raise Exception('Cannot specify negative size in "ds"')
    return CodeSegment(bytearray(space_size), {}, {})


command_handlers = {
    'zero':   zero_handler,
    'unary':  unary_handler,
    'binary': binary_handler,
    'branch': branch_handler,
    'ldsa':   ldsa_handler,
    'ldi':    ldi_handler,
    'osix':   osix_handler,
    'spmove': spmove_handler,

    'dc': dc_handler,
    'ds': ds_handler,
}

cpu_instructions = {}
for category, instructions in insset.items():
    for mnemonic, opcode in instructions.items():
        cpu_instructions[mnemonic] = (opcode, command_handlers[category])

assembler_directives = {}
for directive in dirset:
    assembler_directives[directive] = command_handlers[directive]

def assemble_command(line: InstructionNode) -> CodeSegment:
    if line.mnemonic in dirset:
        handler = assembler_directives[line.mnemonic]
        return handler(line.arguments)
    else:
        opcode, handler = cpu_instructions[line.mnemonic]
        return handler(opcode, line.arguments)
