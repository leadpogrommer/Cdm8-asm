from antlr4.InputStream import InputStream
from collections import deque
import re


def unique(params: list[str]):
    register_available = [True] * 4
    for param in params:
        param_match = re.fullmatch(r'r(\d)', param)
        if not param_match:
            raise Exception(f'unique: {param} is not a register name')
        register_number = int(param_match.group(1))
        if not register_available[register_number]:
            raise Exception(f'unique: {param} appears multiple times')
        register_available[register_number] = False
    for i in range(4):
        if register_available[i]:
            return f'r{i}'
    raise Exception('unique: no registers available')

macro_instructions = {
    'unique': unique,
}


def partition_line(line: str):
    comment_match = re.match(r'((?:[^#"]|"[^"]*")*)#?', line)
    line_without_comment = comment_match.group(1)

    command_toks = re.split(r'\s+', line_without_comment.strip(), 1)
    command, line_remainder = command_toks[0], None
    if len(command_toks) == 2:
        line_remainder = command_toks[1]
    
    return command, line_remainder

def split_params(s: str):
    if s is None:
        return []
    return list(map(str.strip, s.split(',')))


def read_mlb(filename='standard.mlb'):
    library_macros = dict()
    with open(filename, 'r') as mlb:
        for line in mlb:
            if line == '' or line.startswith('#'):
                continue

            elif line.startswith('*'):
                macro_match = re.match(r'\*([a-zA-Z_][a-zA-Z0-9_]*)/(\d)\s*#?', line)
                if not macro_match:
                    raise Exception('Could not read macro header')
                macro_name, macro_arity = macro_match.group(1), int(macro_match.group(2))
                if macro_name not in library_macros:
                    library_macros[macro_name] = dict()
                library_macros[macro_name][macro_arity] = []

            else:
                library_macros[macro_name][macro_arity].append(line.removesuffix('\n'))
    return library_macros


def process_macros(input: InputStream, library_macros=dict()):
    lines = deque(input.getText(0, input.size).split('\n'))
    output_lines = []
    macros = library_macros.copy()
    in_macro = False
    nonce = 1

    while len(lines) > 0:
        line = lines.popleft()
        command, line_remainder = partition_line(line)
        params = split_params(line_remainder)

        if command == 'macro':
            if in_macro:
                raise Exception('Macro definition inside macro')

            header_match = re.fullmatch(r'\s*([a-zA-Z_][a-zA-Z0-9_]*)/(\d)\s*', line_remainder)
            macro_name, macro_arity = header_match.group(1), int(header_match.group(2))
            if macro_name not in macros:
                macros[macro_name] = dict()
            macros[macro_name][macro_arity] = []
            in_macro = True

        elif command == 'mend':
            if line_remainder is not None:
                raise Exception('Nothing allowed after "mend"')
            if not in_macro:
                raise Exception('Mend before macro')

            in_macro = False

        elif in_macro:
            macros[macro_name][macro_arity].append(line)

        else:
            if command in macros:
                if len(params) not in macros[command]:
                    raise Exception('Incorrect number of arguments')

                variables = dict()
                expanded_lines = []
                for macro_line in macros[command][len(params)]:
                    lps = macro_line.split('"')
                    for i in range(0, len(lps), 2):
                        lps[i] = re.sub(r'\$(\d)', lambda m: params[int(m.group(1)) - 1], lps[i])
                        lps[i] = re.sub(r'\?([a-zA-Z_][a-zA-Z0-9_]*)', lambda m: variables[m.group(1)], lps[i]) #Exception?
                        lps[i] = re.sub(r'\'', str(nonce), lps[i])
                    substitute_line = '"'.join(lps)

                    m_command, m_line_remainder = partition_line(substitute_line)
                    m_params = split_params(m_line_remainder)
                    if m_command in macro_instructions:
                        var_name = m_params[-1]
                        variables[var_name] = macro_instructions[m_command](m_params[:-1])
                    else:
                        expanded_lines.append(substitute_line)

                lines.extendleft(expanded_lines[::-1])
                nonce += 1

            else:
                output_lines.append(line)

    return InputStream('\n'.join(output_lines))
