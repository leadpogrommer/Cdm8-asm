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

section_body : code_block ;
code_block
    :
    ( break_statement
    | continue_statement
    | line
    | conditional
    | while_loop
    | until_loop
    | save_restore_statement
    )*
    ;
break_statement : BREAK NEWLINE+ ;
continue_statement : CONTINUE NEWLINE+ ;

name
    : ASECT | RSECT | TPLATE
    | EXT
    | IF | IS | THEN | ELSE | FI
    | WHILE | STAYS | WEND
    | DO | UNTIL
    | BREAK | CONTINUE
    | SAVE | RESTORE
    | END
    | WORD
    ;

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

arguments : argument (COMMA argument)* ;

label_declaration: label (SEMICOLON | ANGLE_BRACKET) ;

line
    : label_declaration EXT? NEWLINE+                    # standaloneLabel
    | label_declaration? instruction arguments? NEWLINE+ # instructionLine
    ;

conjunction : WORD ;
branch_mnemonic : WORD ;
else_clause : ELSE NEWLINE+ code_block ;
condition : code_block IS branch_mnemonic ;
connective_condition : condition COMMA conjunction NEWLINE+ ;
conditions : connective_condition* condition NEWLINE+ (THEN NEWLINE+)? ;
conditional : IF NEWLINE+ conditions code_block else_clause? FI NEWLINE+ ;

while_condition : code_block ;
while_loop : WHILE NEWLINE+ while_condition STAYS branch_mnemonic NEWLINE+ code_block WEND NEWLINE+ ;

until_loop : DO NEWLINE+ code_block UNTIL branch_mnemonic NEWLINE+ ;

save_statement : SAVE register NEWLINE+ ;
restore_statement : RESTORE register? NEWLINE+ ;
save_restore_statement : save_statement code_block restore_statement ;
