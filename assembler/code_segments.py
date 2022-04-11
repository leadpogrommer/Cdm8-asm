from ast_nodes import LabelNode, TemplateFieldNode
from dataclasses import dataclass, field

@dataclass
class CodeSegment:
    base_size: int = field(init=False)

@dataclass
class VariableLengthSegment(CodeSegment):
    is_expanded: bool = field(init=False, default=False)
    expanded_size: int = field(init=False)

@dataclass
class BytesSegment(CodeSegment):
    data: bytearray
    def __init__(self, data: bytearray):
        self.data = data
        self.base_size = len(data)

@dataclass
class ShortAddressSegment(CodeSegment):
    label: LabelNode
    base_size = 1

@dataclass
class LongAddressSegment(CodeSegment):
    label: LabelNode
    base_size = 2

@dataclass
class TemplateFieldSegment(CodeSegment):
    tfield: TemplateFieldNode
    base_size = 1

@dataclass
class GotoSegment(VariableLengthSegment):
    branch_mnemonic: int
    label: LabelNode
    base_size = 2
    expanded_size = 5
