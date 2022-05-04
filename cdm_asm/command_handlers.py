from cdm_asm.asm_commands import instructions as insset, assembly_directives as dirset
from cdm_asm.ast_nodes import *
from cdm_asm.code_segments import *
from typing import Union, get_origin, get_args
import bitstruct

from cdm_asm.error import CdmException, CdmExceptionTag

ArgAddress = Union[int, LabelNode]
ArgDcConstant = Union[int, str, LabelNode]
ArgLdiConstant = Union[int, str, LabelNode, TemplateFieldNode]
ArgStackOffset = Union[int, TemplateFieldNode]
ArgLdsaOffset = Union[int, LabelNode, TemplateFieldNode]


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


def binary_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, RegisterNode)
    data = bitstruct.pack("u4u2u2", opcode // 16, arguments[0].number, arguments[1].number)
    return [BytesSegment(bytearray(data))]

def unary_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode)
    data = bitstruct.pack('u6u2', opcode // 4, arguments[0].number)
    return [BytesSegment(bytearray(data))]

def zero_handler(opcode: int, arguments: list):
    assert_args(arguments)
    return [BytesSegment(bytearray([opcode]))]

def branch_handler(opcode: int, arguments: list):
    assert_args(arguments, ArgAddress)

    if isinstance(arguments[0], int):
        return [OffsetBranchSegment(opcode, arguments[0])]
    elif isinstance(arguments[0], LabelNode):
        return [LabelBranchSegment(opcode, arguments[0])]

def long_handler(opcode: int, arguments: list):
    assert_args(arguments, ArgAddress)

    if isinstance(arguments[0], int):
        return [BytesSegment(bytearray([opcode, arguments[0]]))]
    elif isinstance(arguments[0], LabelNode):
        return [BytesSegment(bytearray([opcode])), LongAddressSegment(arguments[0])]

def ldsa_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, ArgLdsaOffset)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])[0]

    if isinstance(arg, int):
        cmd_piece.data.append(arg)
        return [BytesSegment(cmd_piece.data)]
    elif isinstance(arg, LabelNode):
        return [BytesSegment(cmd_piece.data), ShortAddressSegment(arg)]
    elif isinstance(arg, TemplateFieldNode):
        if arg.negative:
            raise Exception('Cannot use negative template fields in "ldsa" (at least cocas.py doesn\'t allow it)')
        return [BytesSegment(cmd_piece.data), TemplateFieldSegment(arg)]

def ldi_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, ArgLdiConstant)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])[0]

    if isinstance(arg, int):
        cmd_piece.data.append(arg)
        return [BytesSegment(cmd_piece.data)]
    elif isinstance(arg, str):
        arg_data = bytearray(arg, 'utf8')
        if len(arg_data) != 1:
            raise Exception('Argument must be a string of length 1')
        cmd_piece.data.extend(arg_data)
        return [BytesSegment(cmd_piece.data)]
    elif isinstance(arg, LabelNode):
        return [BytesSegment(cmd_piece.data), ShortAddressSegment(arg)]
    elif isinstance(arg, TemplateFieldNode):
        if arg.negative:
            raise Exception('Cannot use negative template fields in "ldi" (at least cocas.py doesn\'t allow it)')
        return [BytesSegment(cmd_piece.data), TemplateFieldSegment(arg)]

def osix_handler(opcode: int, arguments: list):
    assert_args(arguments, int)
    arg = arguments[0]

    if arg < 0:
        raise Exception('Cannot use negative numbers in "osix"')
    return [BytesSegment(bytearray([opcode, arg]))]

def spmove_handler(opcode: int, arguments: list):
    assert_args(arguments, ArgStackOffset)
    arg = arguments[0]

    if isinstance(arg, int):
        if arg < 0: arg += 256
        return [BytesSegment(bytearray([opcode, arg]))]
    elif isinstance(arg, TemplateFieldNode):
        return [BytesSegment(bytearray([opcode, 0])), TemplateFieldSegment(arg)]


def dc_handler(arguments: list):
    assert_args(arguments, ArgDcConstant, single_type=True)
    if len(arguments) == 0:
        raise Exception('At least one argument must be provided')

    segments = []
    for arg in arguments:
        if isinstance(arg, int):
            segments.append(BytesSegment(bytearray([arg])))
        elif isinstance(arg, str):
            segments.append(BytesSegment(bytearray(arg, 'utf8')))
        elif isinstance(arg, LabelNode):
            segments.append(ShortAddressSegment(arg))
    return segments

def ds_handler(arguments: list):
    assert_args(arguments, int)
    space_size = arguments[0]
    if space_size < 0:
        raise Exception('Cannot specify negative size in "ds"')
    return [BytesSegment(bytearray(space_size))]


command_handlers = {
    'zero':   zero_handler,
    'unary':  unary_handler,
    'binary': binary_handler,
    'branch': branch_handler,
    'long':   long_handler,
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


def assemble_command(line: InstructionNode) -> list[CodeSegment]:
    try:
        if line.mnemonic in dirset:
            handler = assembler_directives[line.mnemonic]
            return handler(line.arguments)
        else:
            opcode, handler = cpu_instructions[line.mnemonic]
            segments = handler(opcode, line.arguments)
            for segment in segments:
                segment.location = line.location
            return segments
    except Exception as e:
        if len(e.args) > 0:
            message = str(e.args[0])
        else:
            message = 'Unknown error'
        raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line, message)