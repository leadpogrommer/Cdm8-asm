parser grammar AsmParser;

options { tokenVocab=AsmLexer; }

program : line_mark NEWLINE* section* End ;

section
    :  asect_header section_body # absoluteSection
    |  rsect_header section_body # relocatableSection
    | tplate_header section_body # templateSection
    ;

asect_header  :  Asect number NEWLINE+ ;
rsect_header  :  Rsect name   NEWLINE+ ;
tplate_header : Tplate name   NEWLINE+ ;

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
    | line_mark
    )*
    ;

line_mark : LINE_MARK_MARKER  line_number filepath  NEWLINE+;

line_number: DECIMAL_NUMBER;
filepath: BASE64;

break_statement : Break NEWLINE+ ;
continue_statement : Continue NEWLINE+ ;

line
    : label_declaration Ext? NEWLINE+                    # standaloneLabel
    | label_declaration? instruction arguments? NEWLINE+ # instructionLine
    ;

label_declaration: label (COLON | ANGLE_BRACKET) ;
arguments : argument (COMMA argument)* ;

conditional : If NEWLINE+ conditions code_block else_clause? Fi NEWLINE+ ;
conditions : connective_condition* condition NEWLINE+ (Then NEWLINE+)? ;
connective_condition : condition COMMA conjunction NEWLINE+ ;
condition : code_block Is branch_mnemonic ;
else_clause : Else NEWLINE+ code_block ;

branch_mnemonic : WORD ;
conjunction : WORD ;

while_loop : While NEWLINE+ while_condition Stays branch_mnemonic NEWLINE+ code_block Wend NEWLINE+ ;
while_condition : code_block ;

until_loop : Do NEWLINE+ code_block Until branch_mnemonic NEWLINE+ ;

save_restore_statement : save_statement code_block restore_statement ;
save_statement : Save register NEWLINE+ ;
restore_statement : Restore register? NEWLINE+ ;

argument
    : number
    | character
    | string
    | register
    | label
    | template_field
    ;

template_field : MINUS? name DOT name ;
label : name ;
instruction : WORD ;
string : STRING ;
register : REGISTER ;
character : CHAR ;
number
    : MINUS? DECIMAL_NUMBER
    | HEX_NUMBER
    | BINARY_NUMBER
    ;

name
    : Asect
    | Break
    | Continue
    | Do
    | Else
    | End
    | Ext
    | Fi
    | If
    | Is
    | Macro
    | Restore
    | Rsect
    | Save
    | Stays
    | Then
    | Tplate
    | Until
    | Wend
    | While
    | WORD
    ;
