from asm_commands import assembly_directives as dirset
from ast_nodes import *
from command_handlers import assemble_command
from dataclasses import dataclass


@dataclass
class Template:
    def __init__(self):
        self.name: str = ''
        self.labels: dict[str, int] = dict()

@dataclass
class Section:
    def __init__(self):
        self.address: int = 0
        self.name: str = ''
        self.data: bytearray = bytearray()
        self.label_uses: dict[int, str] = dict()
        self.tfield_uses: dict[int, TemplateFieldNode] = dict()
        self.ext_uses: dict[int, str] = dict()
        self.labels: dict[str, int] = dict()
        self.ents: dict[str, int] = dict()
        self.exts: set[str] = set()

@dataclass
class ObjectSectionRecord:
    def __init__(self, s: Section = Section()):
        self.address: int = s.address
        self.name: str = s.name
        self.data: bytearray = s.data
        self.rel: set[int] = set(filter(lambda k: k not in s.ext_uses, s.label_uses))
        self.ents: dict[str, int] = s.ents

@dataclass
class ObjectModule:
    def __init__(self):
        self.asects: list[ObjectSectionRecord] = []
        self.rsects: list[ObjectSectionRecord] = []
        self.exts: dict[str, dict[str, list[int]]] = dict()


def assemble_template(sn: TemplateSectionNode):
    size = 0
    template = Template()
    template.name = sn.name
    for line in sn.lines:
        if isinstance(line, LabelDeclarationNode):
            label_name = line.label.name
            if label_name in template.labels:
                raise Exception(f'Duplicate label "{label_name}" declaration')

            if line.external:
                raise Exception('External labels not allowed in templates')
            elif line.entry:
                raise Exception('Ents not allowed in templates')
            else:
                template.labels[label_name] = size

        elif isinstance(line, InstructionNode):
            if line.mnemonic not in dirset:
                raise Exception('Only "dc" and "ds" allowed in templates')
            cmd_piece = assemble_command(line)
            size += len(cmd_piece.data)
    template.labels['_'] = size
    return template

def assemble_section(sn: SectionNode):
    section = Section()
    if isinstance(sn, AbsoluteSectionNode):
        section.address = sn.address
        section.name = '$abs'
    else:
        section.address = 0
        section.name = sn.name

    for line in sn.lines:
        if isinstance(line, LabelDeclarationNode):
            label_name = line.label.name
            if (label_name in section.labels or
                label_name in section.ents or
                label_name in section.exts):
                raise Exception(f'Duplicate label "{label_name}" declaration')

            if line.external:
                section.exts.add(label_name)
            else:
                section.labels[label_name] = len(section.data) + section.address
                if line.entry:
                    section.ents[label_name] = len(section.data) + section.address

        elif isinstance(line, InstructionNode):
            cmd_piece = assemble_command(line)
            for offset, label in cmd_piece.label_uses.items():
                section.label_uses[len(section.data) + offset] = label.name
            for offset, tfield in cmd_piece.tfield_uses.items():
                section.tfield_uses[len(section.data) + offset] = tfield
            section.data += cmd_piece.data
    return section

def fill_labels(s: Section, local_labels: dict):
    for label_pos, label_name in s.label_uses.items():
        if label_name in s.labels:
            s.data[label_pos] = s.labels[label_name]
        elif label_name in s.exts:
            s.ext_uses[label_pos + s.address] = label_name
        elif label_name in local_labels:
            s.data[label_pos] = local_labels[label_name]
        else:
            raise Exception(f'Label "{label_name}" not found')

def fill_tfields(s: Section, template_fields: dict):
    for tfield_pos, tfield in s.tfield_uses.items():
        if tfield.template_name in template_fields:
            if tfield.field_name in template_fields[tfield.template_name]:
                s.data[tfield_pos] = template_fields[tfield.template_name][tfield.field_name]
                if tfield.negative:
                    s.data[tfield_pos] = 256 - s.data[tfield_pos]
            else:
                raise Exception(f'Template field "{tfield.template_name}.{tfield.field_name}" not found')
        else:
            raise Exception(f'Template "{tfield.template_name}" not found')

def assemble(pn: ProgramNode):
    templates = [assemble_template(t) for t in pn.template_sections]
    template_fields = dict([(t.name, t.labels) for t in templates])

    asects = [assemble_section(asect) for asect in pn.absolute_sections]
    rsects = [assemble_section(rsect) for rsect in pn.relocatable_sections]

    local_labels = dict()
    for sect in asects + templates:
        local_labels |= sect.labels

    obj = ObjectModule()

    for asect in asects:
        fill_labels(asect, local_labels)
        fill_tfields(asect, template_fields)
        obj.asects.append(ObjectSectionRecord(asect))

    for rsect in rsects:
        fill_labels(rsect, local_labels)
        fill_tfields(rsect, template_fields)
        obj.rsects.append(ObjectSectionRecord(rsect))

    for sect in rsects + asects:
        for ext_pos, ext_name in sect.ext_uses.items():
            sections_using_ext = obj.exts.setdefault(ext_name, dict())
            ext_uses = sections_using_ext.setdefault(sect.name, [])
            ext_uses.append(ext_pos)

    return obj
