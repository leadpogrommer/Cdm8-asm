parser grammar AsmParser;

options { tokenVocab=AsmLexer; }

program : NEWLINE* section* END ;

section
    : asect_header  section_body    # absoluteSection
    | rsect_header  section_body    # relocatableSection
    | tplate_header section_body    # templateSection
    ;

asect_header : ASECT number NEWLINE+ ;
rsect_header : RSECT name NEWLINE+ ;
tplate_header : TPLATE name NEWLINE+ ;

section_body : line* ;

name : ASECT | RSECT | TPLATE | EXT | END | WORD ;
template_field : MINUS? name DOT name ;
label : name ;
instruction : WORD ;
string : STRING ;
register : REGISTER ;

number
    : MINUS? DECIMAL_NUMBER
    | HEX_NUMBER
    | BINARY_NUMBER
    | CHAR
    ;

argument
    : number
    | string
    | register
    | label
    | template_field
    ;

arguments : (argument (COMMA argument)*) ;

label_declaration: label (SEMICOLON | ANGLE_BRACKET) ;

line
    : label_declaration EXT? NEWLINE+                    # standaloneLabel
    | label_declaration? instruction arguments? NEWLINE+ # instructionLine
    ;
