from cdm_asm.ast_nodes import LabelNode, TemplateFieldNode, RelocatableExpressionNode
from cdm_asm.location import CodeLocation
from dataclasses import dataclass, field

@dataclass
class CodeSegment:
    base_size: int = field(init=False)
    def __post_init__(self):
        # ugly hack to store code location in segments
        # now this whole project is one big and ugly hack
        self.location: CodeLocation = CodeLocation()

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
class ByteExpressionSegment(CodeSegment):
    expr: RelocatableExpressionNode
    const: bool = False
    signed: bool = False
    positive: bool = False
    base_size = 1

@dataclass
class AddressExpressionSegment(CodeSegment):
    expr: RelocatableExpressionNode
    base_size = 2

@dataclass
class TemplateFieldSegment(CodeSegment):
    tfield: TemplateFieldNode
    base_size = 1

@dataclass
class GotoSegment(VariableLengthSegment):
    branch_mnemonic: int
    expr: RelocatableExpressionNode
    base_size = 2
    expanded_size = 5
