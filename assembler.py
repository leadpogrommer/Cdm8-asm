from asm_commands import instructions as insset, assembly_directives as dirset
from ast_nodes import *
from command_handlers import assemble_command
from dataclasses import dataclass


@dataclass
class Template:
    def __init__(self):
        self.name: str = ''
        self.labels: dict[str, int] = dict()

@dataclass
class CodeBlock:
    def __init__(self):
        self.data: bytearray = bytearray()
        self.label_uses: dict[int, str] = dict()
        self.tfield_uses: dict[int, TemplateFieldNode] = dict()
        self.ext_uses: dict[int, str] = dict()
        self.labels: dict[str, int] = dict()
        self.ents: dict[str, int] = dict()
        self.exts: set[str] = set()

    def append_block(self, other):
        self.data += other.data
        self.label_uses.update(other.label_uses)
        self.tfield_uses.update(other.tfield_uses)
        self.ext_uses.update(other.ext_uses)
        self.labels.update(other.labels)
        self.ents.update(other.ents)
        self.exts.update(other.exts)

    def append_branch(self, branch, addr):
        self.data += bytearray([insset['branch'][branch], addr])


@dataclass
class Section(CodeBlock):
    def __init__(self):
        self.address: int = 0
        self.name: str = ''
        super().__init__()

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

def assemble_label_declaration(line: LabelDeclarationNode, start_addr: int):
    block = CodeBlock()
    label_name = line.label.name
    if (label_name in block.labels or
        label_name in block.ents or
        label_name in block.exts):
        raise Exception(f'Duplicate label "{label_name}" declaration')

    if line.external:
        block.exts.add(label_name)
    else:
        block.labels[label_name] = start_addr
        if line.entry:
            block.ents[label_name] = start_addr
    return block

def assemble_instruction(line: InstructionNode, start_addr: int):
    block = CodeBlock()
    cmd_piece = assemble_command(line)
    for offset, label in cmd_piece.label_uses.items():
        block.label_uses[start_addr + offset] = label.name
    for offset, tfield in cmd_piece.tfield_uses.items():
        block.tfield_uses[start_addr + offset] = tfield
    block.data += cmd_piece.data
    return block

def assemble_conditional_statement(line: ConditionalStatementNode, start_addr: int, loop_stack: list):
    block = CodeBlock()
    else_block_present = len(line.else_lines) > 0
    cond_count = len(line.conditions)
    cond_addr = start_addr
    next_or_addr = [-1] * cond_count
    last_or = 0

    cond_blocks = []
    for i in range(cond_count):
        cond_blocks.append(assemble_code_block(line.conditions[i].lines, cond_addr, loop_stack))
        cond_addr += len(cond_blocks[i].data) + 2
        if line.conditions[i].conjunction != 'and':
            for j in range(last_or, i):
                next_or_addr[j] = cond_addr
            last_or = i

    then_addr = cond_addr
    then_block = assemble_code_block(line.then_lines, then_addr, loop_stack)
    else_addr = cond_addr + len(then_block.data)
    if else_block_present:
        else_addr += 2
        else_block = assemble_code_block(line.else_lines, else_addr, loop_stack)

    for i in range(cond_count):
        block.append_block(cond_blocks[i])
        if line.conditions[i].conjunction is None:
            branch = f'bn{line.conditions[i].branch_mnemonic}'
            branch_addr = else_addr
        elif line.conditions[i].conjunction == 'or':
            branch = f'b{line.conditions[i].branch_mnemonic}'
            branch_addr = then_addr
        elif line.conditions[i].conjunction == 'and':
            branch = f'bn{line.conditions[i].branch_mnemonic}'
            branch_addr = next_or_addr[i]
        block.append_branch(branch, branch_addr)

    block.append_block(then_block)
    if else_block_present:
        finally_addr = else_addr + len(else_block.data)
        block.append_branch('br', finally_addr)
        block.append_block(else_block)
    return block

def assemble_while_loop(line: WhileLoopNode, start_addr: int, loop_stack: list):
    loop_stack.append([[], []]) # Objects?
    block = CodeBlock()
    cond_addr = start_addr
    cond_block = assemble_code_block(line.condition_lines, cond_addr, loop_stack)
    loop_body_addr = cond_addr + len(cond_block.data) + 2
    loop_body_block = assemble_code_block(line.lines, loop_body_addr, loop_stack)
    finally_addr = loop_body_addr + len(loop_body_block.data) + 2

    block.append_block(cond_block)
    branch = f'bn{line.branch_mnemonic}'
    block.append_branch(branch, finally_addr)
    block.append_block(loop_body_block)
    block.append_branch('br', cond_addr)

    for break_pos in loop_stack[-1][0]:
        block.data[break_pos - start_addr] = finally_addr
    for continue_pos in loop_stack[-1][1]:
        block.data[continue_pos - start_addr] = cond_addr
    loop_stack.pop()

    return block

def assemble_until_loop(line: UntilLoopNode, start_addr: int, loop_stack: list):
    loop_stack.append([[], []]) # Objects?
    block = CodeBlock()
    loop_body_addr = start_addr
    loop_body_block = assemble_code_block(line.lines, loop_body_addr, loop_stack)
    cond_addr = loop_body_addr + len(loop_body_block.data)
    finally_addr = cond_addr + 2

    block.append_block(loop_body_block)
    branch = f'bn{line.branch_mnemonic}'
    block.append_branch(branch, loop_body_addr)

    for break_pos in loop_stack[-1][0]:
        block.data[break_pos - start_addr] = finally_addr
    for continue_pos in loop_stack[-1][1]:
        block.data[continue_pos - start_addr] = cond_addr
    loop_stack.pop()

    return block

def assemble_save_restore_statement(line: SaveRestoreStatement, start_addr: int, loop_stack: list):
    block = CodeBlock()
    block.data.append(insset['unary']['push'] + line.saved_register.number)
    block.append_block(assemble_code_block(line.lines, start_addr + 1, loop_stack))
    block.data.append(insset['unary']['pop'] + line.restored_register.number)
    return block

def assemble_break_statement(start_addr: int, loop_stack: list):
    block = CodeBlock()
    block.append_branch('br', 0)
    if len(loop_stack) == 0:
        raise Exception('"break" not allowed outside of a loop')
    loop_stack[-1][0].append(start_addr + 1)
    return block

def assemble_continue_statement(start_addr: int, loop_stack: list):
    block = CodeBlock()
    block.append_branch('br', 0)
    if len(loop_stack) == 0:
        raise Exception('"continue" not allowed outside of a loop')
    loop_stack[-1][1].append(start_addr + 1)
    return block

def assemble_code_block(lines: list, start_addr: int, loop_stack: list):
    block = CodeBlock()
    for line in lines:
        if   isinstance(line, LabelDeclarationNode):
            block.append_block(assemble_label_declaration(line, start_addr + len(block.data)))
        elif isinstance(line, InstructionNode):
            block.append_block(assemble_instruction(line, start_addr + len(block.data)))
        elif isinstance(line, ConditionalStatementNode):
            block.append_block(assemble_conditional_statement(line, start_addr + len(block.data), loop_stack))
        elif isinstance(line, WhileLoopNode):
            block.append_block(assemble_while_loop(line, start_addr + len(block.data), loop_stack))
        elif isinstance(line, UntilLoopNode):
            block.append_block(assemble_until_loop(line, start_addr + len(block.data), loop_stack))
        elif isinstance(line, SaveRestoreStatement):
            block.append_block(assemble_save_restore_statement(line, start_addr + len(block.data), loop_stack))
        elif isinstance(line, BreakStatementNode):
            block.append_block(assemble_break_statement(start_addr + len(block.data), loop_stack))
        elif isinstance(line, ContinueStatementNode):
            block.append_block(assemble_continue_statement(start_addr + len(block.data), loop_stack))
    return block

def assemble_section(sn: SectionNode):
    section = Section()
    if isinstance(sn, AbsoluteSectionNode):
        section.address = sn.address
        section.name = '$abs'
    else:
        section.address = 0
        section.name = sn.name

    section.append_block(assemble_code_block(sn.lines, section.address, []))

    return section

def fill_labels(s: Section, local_labels: dict):
    print('labels')
    for label_pos, label_name in s.label_uses.items():
        if label_name in s.exts:
            print('nope')
            s.ext_uses[label_pos] = label_name
        elif label_name in s.labels or label_name in local_labels:
            if label_name in s.labels:
                value: int = s.labels[label_name]
            else:
                value: int = local_labels[label_name]

            print(value)
            if value > 255 and s.data[label_pos - s.address] != 0xff:
                # TODO: rewrite this
                bs = value.to_bytes(2, byteorder='little')
                s.data[label_pos - s.address] = bs[0]
                s.data[label_pos - s.address + 1] = bs[1]
            else:
                # not jsr
                print(s.data)
                if s.data[label_pos - s.address] == 0xff:
                    # branch
                    print(value, label_pos)
                    s.data[label_pos - s.address] = (value - label_pos).to_bytes(1, signed=True, byteorder='little')[0]
                else:
                    s.data[label_pos - s.address] = value
        
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

    # TODO: why assembler handles label resolution?
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
