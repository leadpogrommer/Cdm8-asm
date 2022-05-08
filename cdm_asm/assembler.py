from cdm_asm.asm_commands import instructions as insset, assembly_directives as dirset
from cdm_asm.ast_nodes import *
from cdm_asm.code_segments import *
from cdm_asm.command_handlers import assemble_command
from dataclasses import dataclass
from cdm_asm.error import CdmException, CdmExceptionTag

TAG = CdmExceptionTag.ASM

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
        self.segments.append(GotoSegment(mnemonic, RelocatableExpressionNode(None, [LabelNode(label_name)], [], 0)))
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
            if isinstance(line, LocatableNode):
                self.code_locations[self.size] = line.location
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
        self.segments.append(GotoSegment(line.branch_mnemonic, line.expr))
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
        self.rell: set[int] = set()
        self.relh: set[tuple[int, int]] = set()
        self.ents: dict[str, int] = dict(filter(lambda p: p[0] in s.ents, s.labels.items()))
        self.xtrl: dict[str, list[int]] = dict()
        self.xtrh: dict[str, list[tuple[int, int]]] = dict()
        self.code_locations = s.code_locations

        for seg in s.segments:
            if isinstance(seg, BytesSegment):
                self.data += seg.data
            elif isinstance(seg, ByteExpressionSegment):
                self.fill_byte_expr(seg, s, local_labels, template_fields)
            elif isinstance(seg, AddressExpressionSegment):
                self.fill_addr_expr(seg, s, local_labels, template_fields)
            elif isinstance(seg, GotoSegment):
                self.fill_goto(seg, s, local_labels, template_fields)
            elif isinstance(seg, TemplateFieldSegment):
                self.fill_tfield(seg, template_fields)


    def _error(self, segment: CodeSegment, message: str):
        raise CdmException(TAG, segment.location.file, segment.location.line, message)

    def fill_byte_expr(self, seg: ByteExpressionSegment, s: Section,
                       local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        res, is_rel, ext = eval_rel_expr(seg.expr, s, local_labels, template_fields)

        if (is_rel or ext is not None) and (seg.const or seg.expr.byte_specifier is None):
            self._error(seg, 'Number expected but label found')

        res_lo, res_hi = res.to_bytes(2, 'little', signed=(res<0))

        if ext is not None:
            if seg.expr.byte_specifier == 'low':
                self.xtrl.setdefault(ext, []).append(s.address + len(self.data))
                self.data.append(res_lo)
            elif seg.expr.byte_specifier == 'high':
                self.xtrh.setdefault(ext, []).append((s.address + len(self.data), res_lo))
                self.data.append(res_hi)
        elif is_rel:
            if seg.expr.byte_specifier == 'low':
                self.rell.add(s.address + len(self.data))
                self.data.append(res_lo)
            elif seg.expr.byte_specifier == 'high':
                self.relh.add((s.address + len(self.data), res_lo))
                self.data.append(res_hi)
        else:
            if seg.expr.byte_specifier == 'low':
                self.data.append(res_lo)
            elif seg.expr.byte_specifier == 'high':
                self.data.append(res_hi)
            elif -2**7 <= res < 2**8:
                self.data.append(res_lo)
            else:
                self._error(seg, 'Number out of range')

    def fill_addr_expr(self, seg: AddressExpressionSegment, s: Section,
                       local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        res, is_rel, ext = eval_rel_expr(seg.expr, s, local_labels, template_fields)

        res_lo, res_hi = res.to_bytes(2, 'little', signed=(res<0))

        if ext is not None:
            if seg.expr.byte_specifier == 'low':
                self.xtrl.setdefault(ext, []).append(s.address + len(self.data))
                self.data += bytearray([res_lo, 0])
            elif seg.expr.byte_specifier == 'high':
                self.xtrh.setdefault(ext, []).append((s.address + len(self.data), res_lo))
                self.data += bytearray([res_hi, 0])
            else:
                self.xtrl.setdefault(ext, []).append(s.address + len(self.data))
                self.xtrh.setdefault(ext, []).append((s.address + len(self.data) + 1, res_lo))
                self.data += bytearray([res_lo, res_hi])
        elif is_rel:
            if seg.expr.byte_specifier == 'low':
                self.rell.add(s.address + len(self.data))
                self.data += bytearray([res_lo, 0])
            elif seg.expr.byte_specifier == 'high':
                self.relh.add((s.address + len(self.data), res_lo))
                self.data += bytearray([res_hi, 0])
            else:
                self.rell.add(s.address + len(self.data))
                self.relh.add((s.address + len(self.data) + 1, res_lo))
                self.data += bytearray([res_lo, res_hi])
        else:
            if seg.expr.byte_specifier == 'low':
                self.data += bytearray([res_lo, 0])
            elif seg.expr.byte_specifier == 'high':
                self.data += bytearray([res_hi, 0])
            elif -2**15 <= res < 2**16:
                self.data += bytearray([res_lo, res_hi])
            else:
                self._error(seg, 'Number out of range')

    def fill_goto(self, seg: GotoSegment, s: Section,
                  local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
        if seg.is_expanded:
            branch_opcode = insset['branch'][f'bn{seg.branch_mnemonic}']
            jmp_opcode = insset['long']['jmp']
            self.data += bytearray([branch_opcode, 4, jmp_opcode])
            self.fill_addr_expr(AddressExpressionSegment(seg.expr), s, local_labels, template_fields)
        else:
            branch_opcode = insset['branch'][f'b{seg.branch_mnemonic}']
            self.data += bytearray([branch_opcode])
            offset = seg.expr.const_term - self.address - len(self.data)
            offset_expr = RelocatableExpressionNode('low', seg.expr.add_terms, seg.expr.sub_terms, offset)
            self.fill_byte_expr(ByteExpressionSegment(offset_expr, signed=True), s, local_labels, template_fields)

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


def gather_local_labels(sects: list[Section]):
    local_labels = dict()
    for sect in sects:
        local_labels |= dict(filter(lambda p: not p[0].startswith('$'), sect.labels.items()))
    return local_labels

def eval_rel_expr(expr: RelocatableExpressionNode, s: Section,
                  local_labels: dict[str, int], template_fields: dict[str, dict[str, int]]):
    res = expr.const_term
    used_exts = dict()
    s_dim = 0
    local_dim = 0
    for term in expr.add_terms:
        if isinstance(term, LabelNode):
            if term.name in s.labels:
                s_dim += 1
                res += s.labels[term.name]
            elif term.name in local_labels:
                local_dim += 1
                res += local_labels[term.name]
            elif term.name in s.exts:
                used_exts.setdefault(term.name, 0)
                used_exts[term.name] += 1
            else:
                raise Exception(f'Label "{term.name}" not found')
        elif isinstance(term, TemplateFieldNode):
            res += template_fields[term.template_name][term.field_name]

    for term in expr.sub_terms:
        if isinstance(term, LabelNode):
            if term.name in s.labels:
                s_dim -= 1
                res -= s.labels[term.name]
            elif term.name in local_labels:
                local_dim -= 1
                res -= local_labels[term.name]
            elif term.name in s.exts:
                used_exts.setdefault(term.name, 0)
                used_exts[term.name] -= 1
            else:
                raise Exception(f'Label "{term.name}" not found')
        elif isinstance(term, TemplateFieldNode):
            res -= template_fields[term.template_name][term.field_name]

    if s.name == '$abs':
        s_dim += local_dim
        local_dim = 0

    used_exts = dict(filter(lambda x: x[1] != 0, used_exts.items()))
    if len(used_exts) > 1:
        raise Exception('Cannot use multiple external labels in an address expression')

    if len(used_exts) == 1:
        ext, ext_dim = used_exts.popitem()
        if local_dim == 0 and s_dim == 0 and ext_dim == 1:
            return (res, False, ext)
        else:
            raise Exception('Result is not a label or a number')
    else:
        if s_dim == 0 and local_dim in [0, 1]:
            return (res, False, None)
        elif local_dim == 0 and s_dim == 1:
            return (res, True, None)
        else:
            raise Exception('Result is not a label or a number')

def expand_goto_segments(sects: list[Section], local_labels: dict[str, int],
                         template_fields: dict[str, dict[str, int]]):
    @dataclass
    class GotoSegmentEntry:
        seg: GotoSegment
        sect: Section
        pos: int

    gotos: list[GotoSegmentEntry] = []
    labels = gather_local_labels(sects)
    labels.update(local_labels)

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

            addr, is_rel, ext = eval_rel_expr(goto.seg.expr, goto.sect, labels, template_fields)

            if (not -128 <= addr - goto.pos < 128) or not is_rel or ext is not None:
                shift_length = GotoSegment.expanded_size - GotoSegment.base_size
                goto.seg.is_expanded = True
                # print("shif")
                old_locations = goto.sect.code_locations
                goto.sect.code_locations = dict()
                for PC, location in old_locations.items():
                    if PC > goto.pos:
                        PC += shift_length
                    goto.sect.code_locations[PC] = location

                for label_name in goto.sect.labels:
                    if goto.sect.labels[label_name] > goto.pos:
                        goto.sect.labels[label_name] += shift_length
                        labels[label_name] += shift_length
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

    expand_goto_segments(asects, dict(), template_fields)
    local_labels = gather_local_labels(asects)
    for rsect in rsects:
        expand_goto_segments([rsect], local_labels, template_fields)

    obj = ObjectModule()
    obj.asects = [ObjectSectionRecord(asect, local_labels, template_fields) for asect in asects]
    obj.rsects = [ObjectSectionRecord(rsect, local_labels, template_fields) for rsect in rsects]
    return obj
