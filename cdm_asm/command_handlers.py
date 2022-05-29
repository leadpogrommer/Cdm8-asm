from cdm_asm.asm_commands import instructions as insset
from cdm_asm.ast_nodes import *
from cdm_asm.code_segments import *
from typing import get_origin, get_args
import bitstruct

from cdm_asm.error import CdmException, CdmExceptionTag, CdmTempException

def assert_args(args, *types, single_type=False):
    ts = [(t if get_origin(t) is None else get_args(t)) for t in types]
    if single_type:
        if len(ts) != 1:
            raise TypeError('Exactly one type must be specified when single_type is True')
        ts = ts * len(args)
    elif len(args) != len(ts):
        raise CdmTempException(f'Expected {len(ts)} arguments, but found {len(args)}')

    for i in range(len(args)):
        if not isinstance(args[i], ts[i]):
            raise CdmTempException(f'Incompatible argument type {type(args[i])}')


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
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [BytesSegment(bytearray([opcode])), OffsetExpressionSegment(arg)]

def long_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [BytesSegment(bytearray([opcode])), LongExpressionSegment(arg)]

def ldsa_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, RelocatableExpressionNode)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])[0]

    return [BytesSegment(cmd_piece.data), ShortExpressionSegment(arg)]

def ldi_handler(opcode: int, arguments: list):
    assert_args(arguments, RegisterNode, RelocatableExpressionNode | str)
    reg, arg = arguments
    cmd_piece = unary_handler(opcode, [reg])[0]

    if isinstance(arg, str):
        arg_data = bytearray(arg, 'utf8')
        if len(arg_data) != 1:
            raise CdmTempException('Argument must be a string of length 1')
        cmd_piece.data.extend(arg_data)
        return [BytesSegment(cmd_piece.data)]
    elif isinstance(arg, RelocatableExpressionNode):
        return [BytesSegment(cmd_piece.data), ShortExpressionSegment(arg)]

def osix_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [BytesSegment(bytearray([opcode])), ConstExpressionSegment(arg, positive=True)]

def spmove_handler(opcode: int, arguments: list):
    assert_args(arguments, RelocatableExpressionNode)
    arg = arguments[0]

    return [BytesSegment(bytearray([opcode])), ConstExpressionSegment(arg)]


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
}

cpu_instructions = {}
for category, instructions in insset.items():
    for mnemonic, opcode in instructions.items():
        cpu_instructions[mnemonic] = (opcode, command_handlers[category])

def assemble_command(line: InstructionNode) -> list[CodeSegment]:
    try:
        if line.mnemonic in cpu_instructions:
            opcode, handler = cpu_instructions[line.mnemonic]
            segments = handler(opcode, line.arguments)
        else:
            raise CdmTempException(f'Unknown instruction "{line.mnemonic}"')
        for segment in segments:
            segment.location = line.location
        return segments
    except CdmTempException as e:
        raise CdmException(CdmExceptionTag.ASM, line.location.file, line.location.line, e.message)
