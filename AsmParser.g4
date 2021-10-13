parser grammar AsmParser;

options { tokenVocab=AsmLexer; }

program: NEWLINE* section*;
section: section_header section_body;
section_header: SECTION_TYPE number NEWLINE+;
section_body: line*;

label: WORD;
instruction: WORD;
string: STRING;
register: REGISTER;
number: MINUS? DECIMAL_NUMBER | HEX_NUMBER | BINARY_NUMBER | CHAR;
argument: number | string | register | label;

arguments: (argument (COMMA argument)*);

line: label SEMICOLON NEWLINE+ # standaloneLabel
    | (label SEMICOLON)? instruction arguments? NEWLINE+ # instructionLine;