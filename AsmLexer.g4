lexer grammar AsmLexer;

DOT : '.' ;
ANGLE_BRACKET : '>' ;
COMMA : ',' ;
IF : 'if' ;
IS : 'is' ;
THEN : 'then' ;
ELSE : 'else' ;
FI : 'fi' ;
WHILE : 'while' ;
STAYS : 'stays' ;
WEND : 'wend' ;
DO : 'do' ;
UNTIL : 'until' ;
BREAK : 'break' ;
CONTINUE : 'continue' ;
SAVE : 'save' ;
RESTORE : 'restore' ;
EXT : 'ext' ;
END : 'end' ;
ASECT : 'asect' ;
RSECT : 'rsect' ;
TPLATE : 'tplate' ;
REGISTER : 'r'[0-3] ;
WORD : [a-zA-Z_][a-zA-Z_0-9]* ;
SEMICOLON : ':' ;
MINUS : '-' ;
DECIMAL_NUMBER : [0-9]+  ;
BINARY_NUMBER : '0b'[01]+ ;
HEX_NUMBER : '0x'[0-9a-fA-F]+ ;
NEWLINE : '\r'? '\n' ;
COMMENT : '#'~[\n]* -> skip ;
STRING : '"'~["\\\n]*(('\\'.)~["\\\n]*)*'"' ;
CHAR : '\'' ('\\'. | ~[\\'\n]) '\'' ;
WS : (' ' | '\t') -> skip ;




//start: (statement|COMMENT)*;
//
//WS: [ \t]+ -> skip;
//WORD: [a-zA-Z_][a-zA-Z_0-9]*;
//NEWLINE: ([\r]?[\n])+;
//COMMENT: '//' .+? NEWLINE;
//
//
//
//
//
//prepend_label: WORD;
//label: WORD;
//
//statement: (prepend_label ':' | line) NEWLINE ;
//
//line: (label ':')? instruction args;
//
//instruction: WORD;
//
//args: (arg (',' arg)*)?;
//
////TODO: escaped chars/strings
//NUMBER: [-]?[0-9]+;
//CHAR: ['].['];
//STRING: ["].*?["];
//
//
//arg: NUMBER | CHAR | STRING;