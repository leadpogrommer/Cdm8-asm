from dataclasses import dataclass


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
