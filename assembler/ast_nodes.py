from dataclasses import dataclass
from location import CodeLocation

@dataclass
class RegisterNode:
    number: int

@dataclass
class LabelNode:
    name: str

@dataclass
class TemplateFieldNode:
    template_name: str
    field_name: str
    negative: bool

@dataclass
class LabelDeclarationNode:
    label: LabelNode
    entry: bool
    external: bool

@dataclass
class InstructionNode:
    mnemonic: str
    arguments: list
    location: CodeLocation

@dataclass
class ConditionNode:
    lines: list
    branch_mnemonic: str
    conjunction: str

@dataclass
class ConditionalStatementNode:
    conditions: list
    then_lines: list
    else_lines: list

@dataclass
class WhileLoopNode:
    condition_lines: list
    branch_mnemonic: str
    lines: list

@dataclass
class UntilLoopNode:
    lines: list
    branch_mnemonic: str

@dataclass
class BreakStatementNode:
    pass

@dataclass
class ContinueStatementNode:
    pass

@dataclass
class SaveRestoreStatement:
    saved_register: RegisterNode
    lines: list
    restored_register: RegisterNode

@dataclass
class SectionNode:
    lines: list

@dataclass
class AbsoluteSectionNode(SectionNode):
    address: int

@dataclass
class RelocatableSectionNode(SectionNode):
    name: str

@dataclass
class TemplateSectionNode(SectionNode):
    name: str

@dataclass
class ProgramNode:
    template_sections: list[TemplateSectionNode]
    relocatable_sections: list[RelocatableSectionNode]
    absolute_sections: list[AbsoluteSectionNode]
