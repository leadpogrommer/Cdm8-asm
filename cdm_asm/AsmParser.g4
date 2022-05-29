parser grammar AsmParser;

options { tokenVocab=AsmLexer; }

@header {
from base64 import b64decode
}

@members {
    self.current_file = ''
    self.current_line = 0
    self.current_offset = 0
}

program : NEWLINE* line_mark* section* End ;

section
    :  asect_header section_body # absoluteSection
    |  rsect_header section_body # relocatableSection
    | tplate_header section_body # templateSection
    ;

asect_header  :  Asect number NEWLINE+ ;
rsect_header  :  Rsect name   NEWLINE+ ;
tplate_header : Tplate name   NEWLINE+ ;

section_body : code_block ;
code_block : (standalone_label | line_label? statement | line_mark)* ;
standalone_label : label COLON Ext? NEWLINE+ | label ANGLE_BRACKET NEWLINE+ ;
line_label: label (COLON | ANGLE_BRACKET) ;
statement
    : break_statement
    | continue_statement
    | instruction_line
    | define_constant
    | declare_space
    | conditional
    | while_loop
    | until_loop
    | save_restore_statement
    | goto_statement
    ;

line_mark locals [
source_file = '',
source_line = 0
] : LINE_MARK_MARKER  line_number filepath  WORD? NEWLINE+ {
    self.current_line = int($line_number.text)
    self.current_file =  b64decode($filepath.text[3:]).decode()
    $source_file = self.current_file
    $source_line = self.current_line
    self.current_offset = $line_number.start.line - self.current_line + 1
};

line_number: DECIMAL_NUMBER;
filepath: BASE64;

break_statement : Break NEWLINE+ ;
continue_statement : Continue NEWLINE+ ;

instruction_line : instruction arguments? NEWLINE+ ;

label_declaration: label (COLON | ANGLE_BRACKET) ;
arguments : argument (COMMA argument)* ;

define_constant : Dc dc_arguments NEWLINE+ ;
dc_arguments : dc_argument (COMMA dc_argument)* ;
dc_argument : string | addr_expr | byte_expr ;

declare_space : Ds number NEWLINE+ ;

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

goto_statement : Goto branch_mnemonic COMMA goto_argument NEWLINE+ ;
goto_argument : addr_expr | byte_expr ;

argument
    : character
    | string
    | register
    | addr_expr
    | byte_expr
    ;

byte_expr : byte_specifier OPEN_PAREN addr_expr CLOSE_PAREN ;
addr_expr : first_term add_term* ;
first_term : (PLUS | MINUS)? term ;
add_term : (PLUS | MINUS) term ;
term : number | template_field | label ;
byte_specifier : Low | High ;

template_field : name DOT name ;
label : name ;
instruction : WORD ;
string : STRING ;
register : REGISTER ;
character : CHAR ;
number
    : DECIMAL_NUMBER
    | HEX_NUMBER
    | BINARY_NUMBER
    ;

name
    : Asect
    | Break
    | Continue
    | Dc
    | Do
    | Ds
    | Else
    | End
    | Ext
    | Fi
    | Goto
    | High
    | If
    | Is
    | Low
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
