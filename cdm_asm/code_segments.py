from cdm_asm.ast_nodes import LabelNode, TemplateFieldNode
from cdm_asm.location import CodeLocation
from dataclasses import dataclass, field

@dataclass
class CodeSegment:
    size: int = field(init=False)

    def __post_init__(self):
        # ugly hack to store code location in segments
        # now this whole project is one big and ugly hack
        self.location: CodeLocation = CodeLocation()


@dataclass
class BytesSegment(CodeSegment):
    data: bytearray
    def __init__(self, data: bytearray):
        self.data = data
        self.size = len(data)

@dataclass
class ShortAddressSegment(CodeSegment):
    label: LabelNode
    size = 1

@dataclass
class LongAddressSegment(CodeSegment):
    label: LabelNode
    size = 2

@dataclass
class LabelBranchSegment(CodeSegment):
    opcode: int
    label: LabelNode
    size = 2

@dataclass
class OffsetBranchSegment(CodeSegment):
    opcode: int
    offset: int
    size = 2

@dataclass
class LongBranchSegment(LabelBranchSegment):
    def expand_long_jump(opcode: int, addr: int):
        inv_opcode = opcode ^ 0x01
        pcl, pch = addr.to_bytes(2, 'little')
        return bytearray([
            inv_opcode, 0x10,   # <INV BRANCH> skip
            0xCC, 0xFE,         # addsp -2
            0xCE,               # pushall
            0xC9, 0x04,         # ldsa r1, 4
            0xD0, pcl,          # ldi r0, <PCL>
            0xA4,               # st r1, r0
            0xC9, 0x05,         # ldsa r1, 5
            0xD0, pch,          # ldi r0, <PCH>
            0xA4,               # st r1, r0
            0xCF,               # popall
            0xD7                # rts
        ])                      # skip:
    size = 17
    pcl_offset = 8
    pxh_offset = 13

@dataclass
class TemplateFieldSegment(CodeSegment):
    tfield: TemplateFieldNode
    size = 1
