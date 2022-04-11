from asm_commands import instructions as insset, assembly_directives as dirset
from ast_nodes import *
from code_segments import *
from command_handlers import assemble_command
from dataclasses import dataclass


@dataclass
class Template:
    def __init__(self, sn: TemplateSectionNode):
        self.name: str = sn.name
        self.labels: dict[str, int] = dict()

        size = 0
        for line in sn.lines:
            if isinstance(line, LabelDeclarationNode):
                label_name = line.label.name
                if label_name in self.labels:
                    raise Exception(f'Duplicate label "{label_name}" declaration')

                if line.external:
                    raise Exception('External labels not allowed in templates')
                elif line.entry:
                    raise Exception('Ents not allowed in templates')
                else:
                    self.labels[label_name] = size

            elif isinstance(line, InstructionNode):
                if line.mnemonic not in dirset:
                    raise Exception('Only "dc" and "ds" allowed in templates')
                for seg in assemble_command(line):
                    size += seg.base_size

        self.labels['_'] = size

@dataclass
class CodeBlock:
    def __init__(self, address: int, lines: list):
        self.address = address
        self.size: int = 0
        self.loop_stack: list = []
        self.segments: list[CodeSegment] = []
        self.labels: dict[str, int] = dict()
        self.ents: set[str] = set()
        self.exts: set[str] = set()
        self.code_locations: dict[int, CodeLocation] = dict()
        self.assemble_lines(lines)

    def append_label(self, label_name):
        self.labels[label_name] = self.address + self.size

    def append_goto(self, mnemonic, label_name):
        self.segments.append(GotoSegment(mnemonic, LabelNode(label_name)))
        self.size += GotoSegment.base_size

    def assemble_lines(self, lines: list):
        ast_node_handlers = {
            LabelDeclarationNode:       self.assemble_label_declaration,
            InstructionNode:            self.assemble_instruction,
            ConditionalStatementNode:   self.assemble_conditional_statement,
            WhileLoopNode:              self.assemble_while_loop,
            UntilLoopNode:              self.assemble_until_loop,
            SaveRestoreStatementNode:   self.assemble_save_restore_statement,
            BreakStatementNode:         self.assemble_break_statement,
            ContinueStatementNode:      self.assemble_continue_statement,
            GotoStatementNode:          self.assemble_goto_statement
        }
        for line in lines:
            ast_node_handlers[type(line)](line)

    def assemble_label_declaration(self, line: LabelDeclarationNode):
        label_name = line.label.name
        if (label_name in self.labels or
            label_name in self.ents or
            label_name in self.exts):
            raise Exception(f'Duplicate label "{label_name}" declaration')

        if line.external:
            self.exts.add(label_name)
        else:
            self.append_label(label_name)
            if line.entry:
                self.ents.add(label_name)

    def assemble_instruction(self, line: InstructionNode):
        if line.location is not None:
            self.code_locations[self.size] = line.location
        for seg in assemble_command(line):
            self.segments.append(seg)
            self.size += seg.base_size

    def assemble_conditional_statement(self, line: ConditionalStatementNode):
        nonce = self.address + self.size
        or_label = f'${nonce}_or'
        then_label = f'${nonce}_then'
        else_label = f'${nonce}_else'
        finally_label = f'${nonce}_finally'

        next_or = 0
        for cond in line.conditions:
            self.assemble_lines(cond.lines)
            next_or_label = f'{or_label}{next_or}'
            if cond.conjunction is None:
                self.append_goto(f'n{cond.branch_mnemonic}', else_label)
            elif cond.conjunction == 'or':
                self.append_goto(cond.branch_mnemonic, then_label)
                self.append_label(next_or_label)
                next_or += 1
            elif cond.conjunction == 'and':
                self.append_goto(f'n{cond.branch_mnemonic}', next_or_label)

        self.append_label(then_label)
        self.assemble_lines(line.then_lines)

        if len(line.else_lines) > 0:
            self.append_goto('anything', finally_label)
            self.append_label(else_label)
            self.assemble_lines(line.else_lines)
            self.append_label(finally_label)
        else:
            self.append_label(else_label)

    def assemble_while_loop(self, line: WhileLoopNode):
        nonce = self.address + self.size
        cond_label = f'${nonce}_cond'
        finally_label = f'${nonce}_finally'

        self.loop_stack.append((cond_label, finally_label))
        self.append_label(cond_label)
        self.assemble_lines(line.condition_lines)
        self.append_goto(f'n{line.branch_mnemonic}', finally_label)
        self.assemble_lines(line.lines)
        self.append_goto('anything', cond_label)
        self.append_label(finally_label)
        self.loop_stack.pop()

    def assemble_until_loop(self, line: UntilLoopNode):
        nonce = self.address + self.size
        loop_body_label = f'${nonce}_loop_body'
        cond_label = f'${nonce}_cond'
        finally_label = f'${nonce}_finally'

        self.loop_stack.append((cond_label, finally_label))
        self.append_label(loop_body_label)
        self.assemble_lines(line.lines)
        self.append_label(cond_label)
        self.append_goto(f'n{line.branch_mnemonic}', loop_body_label)
        self.append_label(finally_label)
        self.loop_stack.pop()

    def assemble_save_restore_statement(self, line: SaveRestoreStatementNode):
        rn = line.saved_register.number
        push = InstructionNode('push', [RegisterNode(rn)], None)
        pop  = InstructionNode('pop',  [RegisterNode(rn)], None)
        self.assemble_instruction(push)
        self.assemble_lines(line.lines)
        self.assemble_instruction(pop)

    def assemble_break_statement(self, _: BreakStatementNode):
        if len(self.loop_stack) == 0:
            raise Exception('"break" not allowed outside of a loop')
        _, finally_label = self.loop_stack[-1]
        self.append_goto('anything', finally_label)

    def assemble_continue_statement(self, _: ContinueStatementNode):
        if len(self.loop_stack) == 0:
            raise Exception('"continue" not allowed outside of a loop')
        cond_label, _ = self.loop_stack[-1]
        self.append_goto('anything', cond_label)

    def assemble_goto_statement(self, line: GotoStatementNode):
        self.segments.append(GotoSegment(line.branch_mnemonic, line.label))
        self.size += GotoSegment.base_size

@dataclass
class Section(CodeBlock):
    def __init__(self, sn: SectionNode):
        if isinstance(sn, AbsoluteSectionNode):
            self.name = '$abs'
            address = sn.address
        elif isinstance(sn, RelocatableSectionNode):
            self.name = sn.name
            address = 0
        super().__init__(address, sn.lines)

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
            elif isinstance(seg, GotoSegment):
                self.fill_goto(seg, s, local_labels)
            elif isinstance(seg, TemplateFieldSegment):
                self.fill_tfield(seg, template_fields)

    def fill_short_address(self, seg: ShortAddressSegment, s: Section, local_labels: dict[str, int]):
        label_name = seg.label.name
        if label_name in local_labels:
            self.data += bytearray([local_labels[label_name]])
        elif label_name in s.labels:
            # self.rel.add(s.address + len(self.data))
            self.data += bytearray([s.labels[label_name]])
        elif label_name in s.exts:
            # self.ext_uses.setdefault(label_name, []).append(s.address + len(self.data))
            self.data += bytearray([0])
        else:
            raise Exception(f'Label "{label_name}" not found')

    def fill_long_address(self, seg: LongAddressSegment, s: Section, local_labels: dict[str, int]):
        label_name = seg.label.name
        if label_name in local_labels:
            self.data += local_labels[label_name].to_bytes(2, 'little')
        elif label_name in s.labels:
            # Add rel (2 bytes long)
            self.data += s.labels[label_name].to_bytes(2, 'little')
        elif label_name in s.exts:
            # Add external label use (2 bytes long)
            self.data += bytearray([0, 0])
        else:
            raise Exception(f'Label "{label_name}" not found')

    def fill_goto(self, seg: GotoSegment, s: Section, local_labels: dict[str, int]):
        label_name = seg.label.name
        if label_name in local_labels:
            addr = local_labels[label_name]
        elif label_name in s.labels:
            # Add rel (2 bytes long)
            addr = s.labels[label_name]
        elif label_name in s.exts:
            # Add external label use (2 bytes long)
            addr = 0
        else:
            raise Exception(f'Label "{label_name}" not found')

        if seg.is_expanded:
            branch_opcode = insset['branch'][f'bn{seg.branch_mnemonic}']
            jmp_opcode = insset['long']['jmp']
            self.data += bytearray([branch_opcode, 4, jmp_opcode]) + addr.to_bytes(2, 'little')
        else:
            branch_opcode = insset['branch'][f'b{seg.branch_mnemonic}']
            offset = addr - self.address - len(self.data) - 1
            self.data += bytearray([branch_opcode]) + offset.to_bytes(1, 'little', signed=True)

    def fill_tfield(self, seg: TemplateFieldSegment, template_fields: dict[str, dict[str, int]]):
        tf = seg.tfield
        if tf.template_name in template_fields:
            if tf.field_name in template_fields[tf.template_name]:
                value = template_fields[tf.template_name][tf.field_name]
                self.data += value.to_bytes(1, 'little')
                if tf.negative:
                    self.data += (-value).to_bytes(1, 'little', signed=True)
            else:
                raise Exception(f'Template field "{tf.template_name}.{tf.field_name}" not found')
        else:
            raise Exception(f'Template "{tf.template_name}" not found')

@dataclass
class ObjectModule:
    def __init__(self):
        self.asects: list[ObjectSectionRecord] = []
        self.rsects: list[ObjectSectionRecord] = []
        self.exts: dict[str, dict[str, list[int]]] = dict()


def gather_local_labels(sects: list[Section]):
    local_labels = dict()
    for sect in sects:
        local_labels |= dict(filter(lambda p: not p[0].startswith('$') and p[0] not in sect.ents, sect.labels.items()))
    return local_labels

def expand_goto_segments(sects: list[Section]):
    @dataclass
    class GotoSegmentEntry:
        seg: GotoSegment
        sect: Section
        pos: int

    gotos: list[GotoSegmentEntry] = []
    local_labels = gather_local_labels(sects)

    for sect in sects:
        pos = sect.address
        for seg in sect.segments:
            if isinstance(seg, GotoSegment):
                gotos.append(GotoSegmentEntry(seg, sect, pos + 1))
            pos += seg.base_size

    while True:
        for goto in gotos:
            if goto.seg.is_expanded:
                continue

            label_name = goto.seg.label.name
            if label_name in goto.sect.labels:
                offset = goto.sect.labels[label_name] - goto.pos
            elif label_name in local_labels:
                offset = local_labels[label_name] - goto.pos

            if not -128 <= offset < 128:
                shift_length = GotoSegment.expanded_size - GotoSegment.base_size
                goto.seg.is_expanded = True
                for label_name in goto.sect.labels:
                    if goto.sect.labels[label_name] > goto.pos:
                        goto.sect.labels[label_name] += shift_length
                for other_goto in gotos:
                    if other_goto.sect is goto.sect and other_goto.pos > goto.pos:
                        other_goto.pos += shift_length
                break
        else:
            break



def assemble(pn: ProgramNode):
    templates = [Template(t) for t in pn.template_sections]
    template_fields = dict([(t.name, t.labels) for t in templates])

    asects = [Section(asect) for asect in pn.absolute_sections]
    rsects = [Section(rsect) for rsect in pn.relocatable_sections]
    asects.sort(key=lambda s: s.address)

    expand_goto_segments(asects)
    for rsect in rsects:
        expand_goto_segments([rsect])

    local_labels = gather_local_labels(asects)

    obj = ObjectModule()
    obj.asects = [ObjectSectionRecord(asect, local_labels, template_fields) for asect in asects]
    obj.rsects = [ObjectSectionRecord(rsect, local_labels, template_fields) for rsect in rsects]
    return obj
