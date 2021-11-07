from collections import deque
from dataclasses import dataclass
import re

from antlr4.InputStream import InputStream

@dataclass
class Macro:
    arity: int
    lines: list[str]

def process_macros(input: InputStream):
    macros = dict()
    lines = deque(input.getText(0, input.size).split('\n'))
    output_lines = []
    in_macro = False
    while len(lines) > 0:
        line = lines.popleft()

        comment_match = re.match(r'((?:[^#"]|"[^"]*")*)#?', line)
        line_without_comment = comment_match.group(1)

        command_toks = re.split(r'\s+', line_without_comment.strip(), 1)
        command, line_remainder = command_toks[0], None
        if len(command_toks) == 2:
            line_remainder = command_toks[1]

        if command == 'macro':
            if in_macro:
                raise Exception('Macro inside a macro?')

            header_match = re.fullmatch(r'\s*([a-zA-Z_][a-zA-Z0-9_]*)/(\d)\s*', line_remainder)
            macro_name, macro_arity = header_match.group(1), header_match.group(2)
            macros[macro_name] = Macro(int(macro_arity), [])
            in_macro = True

        elif command == 'mend':
            if line_remainder is not None:
                raise Exception('Nothing allowed after "mend"')
            if not in_macro:
                raise Exception('Mend before macro')

            in_macro = False

        elif in_macro:
            macros[macro_name].lines.append(line)

        else:
            if command in macros:
                params = []
                if line_remainder is not None:
                    params = list(map(str.strip, line_remainder.split(',')))

                if len(params) != macros[command].arity:
                    raise Exception('Incorrect number of arguments')

                for macro_line in macros[command].lines[::-1]:
                    lps = macro_line.split('"')
                    for i in range(0, len(lps), 2):
                        lps[i] = re.sub(r'\$(\d)', lambda m: params[int(m.group(1)) - 1], lps[i])
                    lines.appendleft('"'.join(lps))
            else:
                output_lines.append(line)

    return InputStream('\n'.join(output_lines))
