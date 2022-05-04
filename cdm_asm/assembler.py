from cdm_asm.asm_commands import instructions as insset, assembly_directives as dirset
from cdm_asm.ast_nodes import *
from cdm_asm.code_segments import *
from cdm_asm.command_handlers import assemble_command
from dataclasses import dataclass
from cdm_asm.error import CdmException, CdmExceptionTag

TAG = CdmExceptionTag.ASM

@dataclass
class Template:
    def __init__(self):
        self.name: str = ''
        self.labels: dict[str, int] = dict()

@dataclass
class CodeBlock:
    def __init__(self, address: int):
        self.address = address
        self.size: int = 0
        self.segments: list[CodeSegment] = []
        self.labels: dict[str, int] = dict()
        self.ents: set[str] = set()
        self.exts: set[str] = set()
        self.code_locations: dict[int, CodeLocation] = dict()

    def append_block(self, other):
        self.size += other.size
        self.segments += other.segments
        self.labels.update(other.labels)
        self.ents.update(other.ents)
        self.exts.update(other.exts)
        self.code_locations.update(other.code_locations)

    def append_bytes(self, data):
        self.segments.append(BytesSegment(bytearray(data)))
        self.size += len(data)

    def append_label(self, label_name):
        self.labels[label_name] = self.address + self.size

    def append_branch(self, mnemonic, label_name):
        self.segments.append(LabelBranchSegment(insset['branch'][mnemonic], LabelNode(label_name)))
        self.size += 2

@dataclass
class Section(CodeBlock):
    def __init__(self, address: int, name: str):
        self.name = name
        super().__init__(address)

@dataclass
class ObjectSectionRecord:
    def __init__(self, s: Section, local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        self.address: int = s.address
        self.name: str = s.name
        self.data = bytearray()
        self.rel: set[int] = set()
        self.ents: dict[str, int] = dict(filter(lambda p: p[0] in s.ents, s.labels.items()))
        self.ext_uses: dict[str, list[int]] = dict()
        self.code_locations = s.code_locations

        for seg in s.segments:
            if isinstance(seg, BytesSegment):
                self.data += seg.data
            elif isinstance(seg, ShortAddressSegment):
                self.fill_short_address(seg, s, local_labels)
            elif isinstance(seg, LongAddressSegment):
                self.fill_long_address(seg, s, local_labels)
            elif isinstance(seg, LongBranchSegment):
                self.fill_long_branch(seg, s, local_labels)
            elif isinstance(seg, LabelBranchSegment):
                self.fill_branch(seg, s, local_labels)
            elif isinstance(seg, OffsetBranchSegment):
                self.fill_offset_branch(seg)
            elif isinstance(seg, TemplateFieldSegment):
                self.fill_tfield(seg, template_fields)

    def _error(self, segment: CodeSegment, message: str):
        raise CdmException(TAG, segment.location.file, segment.location.line, message)

    def fill_short_address(self, seg: ShortAddressSegment, s: Section, local_labels: dict[str, int]):
        label_name = seg.label.name
        if label_name in local_labels:
            self.data += bytearray([local_labels[label_name]])
        elif label_name in s.labels:
            self.rel.add(s.address + len(self.data))
            self.data += bytearray([s.labels[label_name]])
        elif label_name in s.exts:
            self.data += bytearray([0])
            self.ext_uses.setdefault(label_name, []).append(s.address + len(self.data))
        else:
            self._error(seg, f'Label "{label_name}" not found')

    def fill_long_address(self, seg: LongAddressSegment, s: Section, local_labels: dict[str, int]):
        label_name = seg.label.name
        if label_name in local_labels:
            self.data += local_labels[label_name].to_bytes(2, 'little')
        elif label_name in s.labels:
            # Add rel (2 bytes long)
            self.data += s.labels[label_name].to_bytes(2, 'little')
        elif label_name in s.exts:
            # TODO: Where is actual ext definition?
            # Add external label use (2 bytes long)
            self.data += bytearray([0, 0])
        else:
            self._error(seg, f'Label "{label_name}" not found')

    def fill_branch(self, seg: LabelBranchSegment, s: Section, local_labels: dict[str, int]):
        label_name = seg.label.name
        if label_name in local_labels:
            addr = local_labels[label_name]
        elif label_name in s.labels:
            addr = s.labels[label_name]
        elif label_name in s.exts:
            self._error(seg, f'Cannot branch to an external label "{label_name}"')
        else:
            self._error(seg, f'Label "{label_name}" not found')

        offset = addr - s.address - len(self.data) - 1
        if not -128 <= offset < 128:
            self._error(seg, 'Branch offset too far')

        self.data += seg.opcode.to_bytes(1, 'little')
        self.data += offset.to_bytes(1, 'little', signed=True)

    def fill_offset_branch(self, seg: OffsetBranchSegment):
        if not -128 <= seg.offset < 128:
            self._error(seg, 'Branch offset too far')
        self.data += seg.opcode.to_bytes(1, 'little')
        self.data += seg.offset.to_bytes(1, 'little', signed=True)

    def fill_long_branch(self, seg: LabelBranchSegment, s: Section, local_labels: dict[str, int]):
        label_name = seg.label.name
        if label_name in local_labels:
            addr = local_labels[label_name]
        elif label_name in s.labels:
            # Add rel (2 bytes are apart)
            addr = s.labels[label_name]
        elif label_name in s.exts:
            # Add external label use (2 bytes are apart)
            addr = 0
        self.data += LongBranchSegment.expand_long_jump(seg.opcode, addr)

    def fill_tfield(self, seg: TemplateFieldSegment, template_fields: dict[str, dict[str, int]]):
        tf = seg.tfield
        if tf.template_name in template_fields:
            if tf.field_name in template_fields[tf.template_name]:
                value = template_fields[tf.template_name][tf.field_name]
                self.data += value.to_bytes(1, 'little')
                if tf.negative:
                    self.data += (-value).to_bytes(1, 'little', signed=True)
            else:
                self._error(seg, f'Template field "{tf.template_name}.{tf.field_name}" not found')
        else:
            self._error(seg, f'Template "{tf.template_name}" not found')

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
    for line_number, line in enumerate(sn.lines):
        location = sn.locations[line_number]
        if isinstance(line, LabelDeclarationNode):
            label_name = line.label.name
            if label_name in template.labels:
                raise CdmException(TAG,location.file, location.line, f'Duplicate label "{label_name}" declaration')

            if line.external:
                raise CdmException(TAG,location.file, location.line, 'External labels not allowed in templates')
            elif line.entry:
                raise CdmException(TAG,location.file, location.line, 'Ents not allowed in templates')
            else:
                template.labels[label_name] = size

        elif isinstance(line, InstructionNode):
            if line.mnemonic not in dirset:
                raise CdmException(TAG,location.file, location.line, 'Only "dc" and "ds" allowed in templates')
            cmd_piece = assemble_instruction(line)
            size += cmd_piece.segments[0].size
    template.labels['_'] = size
    return template


def assemble_label_declaration(line: LabelDeclarationNode, start_addr: int):
    block = CodeBlock(start_addr)
    label_name = line.label.name
    if (label_name in block.labels or
        label_name in block.ents or
        label_name in block.exts):
        # TODO: use CdmException
        raise Exception(f'Duplicate label "{label_name}" declaration')

    if line.external:
        block.exts.add(label_name)
    else:
        block.labels[label_name] = start_addr
        if line.entry:
            block.ents.add(label_name)
    return block


def assemble_instruction(line: InstructionNode):
    block = CodeBlock(0)
    block.segments += assemble_command(line)
    for seg in block.segments:
        block.size += seg.size
    return block


def assemble_conditional_statement(line: ConditionalStatementNode, start_addr: int, loop_stack: list):
    block = CodeBlock(start_addr)

    or_label = f'${start_addr}_or'
    then_label = f'${start_addr}_then'
    else_label = f'${start_addr}_else'
    finally_label = f'${start_addr}_finally'

    next_or = 0
    for cond in line.conditions:
        block.append_block(assemble_code_block(cond.lines, start_addr + block.size, loop_stack))
        next_or_label = f'{or_label}{next_or}'
        if cond.conjunction is None:
            block.append_branch(f'bn{cond.branch_mnemonic}', else_label)
        elif cond.conjunction == 'or':
            block.append_branch(f'b{cond.branch_mnemonic}', then_label)
            block.append_label(next_or_label)
            next_or += 1
        elif cond.conjunction == 'and':
            block.append_branch(f'bn{cond.branch_mnemonic}', next_or_label)

    block.append_label(then_label)
    block.append_block(assemble_code_block(line.then_lines, start_addr + block.size, loop_stack))

    if len(line.else_lines) > 0:
        block.append_branch('br', finally_label)
        block.append_label(else_label)
        block.append_block(assemble_code_block(line.else_lines, start_addr + block.size, loop_stack))
        block.append_label(finally_label)
    else:
        block.append_label(else_label)

    return block


def assemble_while_loop(line: WhileLoopNode, start_addr: int, loop_stack: list):
    block = CodeBlock(start_addr)

    cond_label = f'${start_addr}_cond'
    finally_label = f'${start_addr}_finally'

    loop_stack.append((cond_label, finally_label))
    block.append_label(cond_label)
    block.append_block(assemble_code_block(line.condition_lines, start_addr + block.size, loop_stack))
    block.append_branch(f'bn{line.branch_mnemonic}', finally_label)
    block.append_block(assemble_code_block(line.lines, start_addr + block.size, loop_stack))
    block.append_branch('br', cond_label)
    block.append_label(finally_label)
    loop_stack.pop()

    return block

def assemble_until_loop(line: UntilLoopNode, start_addr: int, loop_stack: list):
    block = CodeBlock(start_addr)

    loop_body_label = f'${start_addr}_loop_body'
    cond_label = f'${start_addr}_cond'
    finally_label = f'${start_addr}_finally'

    loop_stack.append((cond_label, finally_label))
    block.append_label(loop_body_label)
    block.append_block(assemble_code_block(line.lines, start_addr + block.size, loop_stack))
    block.append_label(cond_label)
    block.append_branch(f'bn{line.branch_mnemonic}', loop_body_label)
    block.append_label(finally_label)
    loop_stack.pop()

    return block

def assemble_save_restore_statement(line: SaveRestoreStatement, start_addr: int, loop_stack: list):
    block = CodeBlock(start_addr)
    block.append_bytes([insset['unary']['push'] + line.saved_register.number])
    block.append_block(assemble_code_block(line.lines, start_addr + block.size, loop_stack))
    block.append_bytes([insset['unary']['pop'] + line.restored_register.number])
    return block

def assemble_break_statement(loop_stack: list):
    block = CodeBlock(0)
    if len(loop_stack) == 0:
        # TODO: use CdmException
        raise Exception('"break" not allowed outside of a loop')
    _, finally_label = loop_stack[-1]
    block.append_branch('br', finally_label)
    return block

def assemble_continue_statement(loop_stack: list):
    block = CodeBlock(0)
    if len(loop_stack) == 0:
        # TODO: use CdmException
        raise Exception('"continue" not allowed outside of a loop')
    cond_label, _ = loop_stack[-1]
    block.append_branch('br', cond_label)
    return block

def assemble_code_block(lines: list, start_addr: int, loop_stack: list):
    block = CodeBlock(start_addr)
    for line in lines:
        if isinstance(line, LabelDeclarationNode):
            block.append_block(assemble_label_declaration(line, start_addr + block.size))
        elif isinstance(line, InstructionNode):
            new_block = assemble_instruction(line)
            new_block.code_locations[block.size] = line.location
            block.append_block(new_block)
        elif isinstance(line, ConditionalStatementNode):
            block.append_block(assemble_conditional_statement(line, start_addr + block.size, loop_stack))
        elif isinstance(line, WhileLoopNode):
            block.append_block(assemble_while_loop(line, start_addr + block.size, loop_stack))
        elif isinstance(line, UntilLoopNode):
            block.append_block(assemble_until_loop(line, start_addr + block.size, loop_stack))
        elif isinstance(line, SaveRestoreStatement):
            block.append_block(assemble_save_restore_statement(line, start_addr + block.size, loop_stack))
        elif isinstance(line, BreakStatementNode):
            block.append_block(assemble_break_statement(loop_stack))
        elif isinstance(line, ContinueStatementNode):
            block.append_block(assemble_continue_statement(loop_stack))
    return block

def assemble_section(sn: SectionNode):
    if isinstance(sn, AbsoluteSectionNode):
        section = Section(sn.address, '$abs')
    else:
        section = Section(0, sn.name)
    section.append_block(assemble_code_block(sn.lines, section.address, []))
    return section

def gather_local_labels(sects: list[Section]):
    local_labels = dict()
    for sect in sects:
        local_labels |= dict(filter(lambda p: not p[0].startswith('$') and p[0] not in sect.ents, sect.labels.items()))
    return local_labels

def expand_long_branches(sects: list[Section]):
    branch_pos: list[int] = []
    branch_ind: list[int] = []
    branch_sect: list[Section] = []
    branch_label: list[str] = []

    local_labels = gather_local_labels(sects)

    for s in sects:
        pos = s.address
        for i in range(len(s.segments)):
            if isinstance(s.segments[i], OffsetBranchSegment):
                label_name = f'$offset{i}'
                s.labels[label_name] = pos + s.segments[i].offset + 1
                s.segments[i] = LabelBranchSegment(s.segments[i].opcode, LabelNode(label_name))
            if isinstance(s.segments[i], LabelBranchSegment):
                branch_pos.append(pos + 1)
                branch_ind.append(i)
                branch_sect.append(s)
                branch_label.append(s.segments[i].label.name)
            pos += s.segments[i].size

    all_expanded = False
    while not all_expanded:
        for i in range(len(branch_label)):
            seg = branch_sect[i].segments[branch_ind[i]]
            if isinstance(seg, LongBranchSegment):
                continue
            if branch_label[i] in branch_sect[i].labels:
                offset = branch_sect[i].labels[branch_label[i]] - branch_pos[i]
                if -128 <= offset < 128:
                    continue
            if branch_label[i] in local_labels:
                offset = local_labels[branch_label[i]] - branch_pos[i]
                if -128 <= offset < 128:
                    continue
            branch_sect[i].segments[branch_ind[i]] = LongBranchSegment(seg.opcode, seg.label)
            break
        else:
            all_expanded = True
            break

        shift_length = LongBranchSegment.size - LabelBranchSegment.size
        for label_name in branch_sect[i].labels:
            if branch_sect[i].labels[label_name] > branch_pos[i]:
                branch_sect[i].labels[label_name] += shift_length
        for j in range(len(branch_label)):
            if branch_sect[j] is branch_sect[i] and branch_pos[j] > branch_pos[i]:
                branch_pos[j] += shift_length


def assemble(pn: ProgramNode):
    templates = [assemble_template(t) for t in pn.template_sections]
    template_fields = dict([(t.name, t.labels) for t in templates])

    asects = [assemble_section(asect) for asect in pn.absolute_sections]
    rsects = [assemble_section(rsect) for rsect in pn.relocatable_sections]
    asects.sort(key=lambda s: s.address)

    # expand_long_branches(asects)
    # for rsect in rsects:
    #     expand_long_branches([rsect])

    local_labels = gather_local_labels(asects)

    obj = ObjectModule()
    obj.asects = [ObjectSectionRecord(asect, local_labels, template_fields) for asect in asects]
    obj.rsects = [ObjectSectionRecord(rsect, local_labels, template_fields) for rsect in rsects]
    return obj
