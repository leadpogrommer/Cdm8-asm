# Generated from /home/ilya/work/cdm8e/ORiGinalASM/cdm_asm/AsmParser.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from base64 import b64decode

def serializedATN():
    return [
        4,1,45,400,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,1,0,5,0,93,
        8,0,10,0,12,0,96,9,0,1,0,5,0,99,8,0,10,0,12,0,102,9,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,115,8,1,1,2,1,2,1,2,4,2,120,
        8,2,11,2,12,2,121,1,3,1,3,1,3,4,3,127,8,3,11,3,12,3,128,1,4,1,4,
        1,4,4,4,134,8,4,11,4,12,4,135,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,5,6,149,8,6,10,6,12,6,152,9,6,1,7,1,7,1,7,1,7,3,7,158,
        8,7,1,7,4,7,161,8,7,11,7,12,7,162,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,
        10,4,10,173,8,10,11,10,12,10,174,1,11,1,11,4,11,179,8,11,11,11,12,
        11,180,1,12,1,12,3,12,185,8,12,1,12,4,12,188,8,12,11,12,12,12,189,
        1,12,3,12,193,8,12,1,12,1,12,3,12,197,8,12,1,12,4,12,200,8,12,11,
        12,12,12,201,3,12,204,8,12,1,13,1,13,1,13,1,14,1,14,1,14,5,14,212,
        8,14,10,14,12,14,215,9,14,1,15,1,15,4,15,219,8,15,11,15,12,15,220,
        1,15,1,15,1,15,3,15,226,8,15,1,15,1,15,4,15,230,8,15,11,15,12,15,
        231,1,16,5,16,235,8,16,10,16,12,16,238,9,16,1,16,1,16,4,16,242,8,
        16,11,16,12,16,243,1,16,1,16,4,16,248,8,16,11,16,12,16,249,3,16,
        252,8,16,1,17,1,17,1,17,1,17,4,17,258,8,17,11,17,12,17,259,1,18,
        1,18,1,18,1,18,1,19,1,19,4,19,268,8,19,11,19,12,19,269,1,19,1,19,
        1,20,1,20,1,21,1,21,1,22,1,22,4,22,280,8,22,11,22,12,22,281,1,22,
        1,22,1,22,1,22,4,22,288,8,22,11,22,12,22,289,1,22,1,22,1,22,4,22,
        295,8,22,11,22,12,22,296,1,23,1,23,1,24,1,24,4,24,303,8,24,11,24,
        12,24,304,1,24,1,24,1,24,1,24,4,24,311,8,24,11,24,12,24,312,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,4,26,322,8,26,11,26,12,26,323,1,27,
        1,27,3,27,328,8,27,1,27,4,27,331,8,27,11,27,12,27,332,1,28,1,28,
        1,28,1,28,1,28,4,28,340,8,28,11,28,12,28,341,1,29,1,29,3,29,346,
        8,29,1,30,1,30,1,30,1,30,1,30,3,30,353,8,30,1,31,1,31,1,31,1,31,
        1,31,1,32,1,32,5,32,362,8,32,10,32,12,32,365,9,32,1,33,3,33,368,
        8,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,3,35,378,8,35,1,36,
        1,36,1,37,1,37,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,
        1,42,1,42,1,43,1,43,1,44,1,44,1,44,0,0,45,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,0,5,2,0,28,28,30,30,1,
        0,26,27,1,0,22,23,1,0,36,38,2,0,1,23,35,35,408,0,90,1,0,0,0,2,114,
        1,0,0,0,4,116,1,0,0,0,6,123,1,0,0,0,8,130,1,0,0,0,10,137,1,0,0,0,
        12,150,1,0,0,0,14,153,1,0,0,0,16,166,1,0,0,0,18,168,1,0,0,0,20,170,
        1,0,0,0,22,176,1,0,0,0,24,203,1,0,0,0,26,205,1,0,0,0,28,208,1,0,
        0,0,30,216,1,0,0,0,32,236,1,0,0,0,34,253,1,0,0,0,36,261,1,0,0,0,
        38,265,1,0,0,0,40,273,1,0,0,0,42,275,1,0,0,0,44,277,1,0,0,0,46,298,
        1,0,0,0,48,300,1,0,0,0,50,314,1,0,0,0,52,318,1,0,0,0,54,325,1,0,
        0,0,56,334,1,0,0,0,58,345,1,0,0,0,60,352,1,0,0,0,62,354,1,0,0,0,
        64,359,1,0,0,0,66,367,1,0,0,0,68,371,1,0,0,0,70,377,1,0,0,0,72,379,
        1,0,0,0,74,381,1,0,0,0,76,385,1,0,0,0,78,387,1,0,0,0,80,389,1,0,
        0,0,82,391,1,0,0,0,84,393,1,0,0,0,86,395,1,0,0,0,88,397,1,0,0,0,
        90,94,3,14,7,0,91,93,5,41,0,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,
        1,0,0,0,94,95,1,0,0,0,95,100,1,0,0,0,96,94,1,0,0,0,97,99,3,2,1,0,
        98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,
        103,1,0,0,0,102,100,1,0,0,0,103,104,5,6,0,0,104,1,1,0,0,0,105,106,
        3,4,2,0,106,107,3,10,5,0,107,115,1,0,0,0,108,109,3,6,3,0,109,110,
        3,10,5,0,110,115,1,0,0,0,111,112,3,8,4,0,112,113,3,10,5,0,113,115,
        1,0,0,0,114,105,1,0,0,0,114,108,1,0,0,0,114,111,1,0,0,0,115,3,1,
        0,0,0,116,117,5,1,0,0,117,119,3,86,43,0,118,120,5,41,0,0,119,118,
        1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,5,1,
        0,0,0,123,124,5,14,0,0,124,126,3,88,44,0,125,127,5,41,0,0,126,125,
        1,0,0,0,127,128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,7,1,
        0,0,0,130,131,5,18,0,0,131,133,3,88,44,0,132,134,5,41,0,0,133,132,
        1,0,0,0,134,135,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,9,1,
        0,0,0,137,138,3,12,6,0,138,11,1,0,0,0,139,149,3,20,10,0,140,149,
        3,22,11,0,141,149,3,24,12,0,142,149,3,30,15,0,143,149,3,44,22,0,
        144,149,3,48,24,0,145,149,3,50,25,0,146,149,3,56,28,0,147,149,3,
        14,7,0,148,139,1,0,0,0,148,140,1,0,0,0,148,141,1,0,0,0,148,142,1,
        0,0,0,148,143,1,0,0,0,148,144,1,0,0,0,148,145,1,0,0,0,148,146,1,
        0,0,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,
        0,0,0,151,13,1,0,0,0,152,150,1,0,0,0,153,154,5,33,0,0,154,155,3,
        16,8,0,155,157,3,18,9,0,156,158,5,35,0,0,157,156,1,0,0,0,157,158,
        1,0,0,0,158,160,1,0,0,0,159,161,5,41,0,0,160,159,1,0,0,0,161,162,
        1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,
        6,7,-1,0,165,15,1,0,0,0,166,167,5,36,0,0,167,17,1,0,0,0,168,169,
        5,44,0,0,169,19,1,0,0,0,170,172,5,2,0,0,171,173,5,41,0,0,172,171,
        1,0,0,0,173,174,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,21,1,
        0,0,0,176,178,5,3,0,0,177,179,5,41,0,0,178,177,1,0,0,0,179,180,1,
        0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,23,1,0,0,0,182,184,3,26,
        13,0,183,185,5,7,0,0,184,183,1,0,0,0,184,185,1,0,0,0,185,187,1,0,
        0,0,186,188,5,41,0,0,187,186,1,0,0,0,188,189,1,0,0,0,189,187,1,0,
        0,0,189,190,1,0,0,0,190,204,1,0,0,0,191,193,3,26,13,0,192,191,1,
        0,0,0,192,193,1,0,0,0,193,194,1,0,0,0,194,196,3,78,39,0,195,197,
        3,28,14,0,196,195,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,200,
        5,41,0,0,199,198,1,0,0,0,200,201,1,0,0,0,201,199,1,0,0,0,201,202,
        1,0,0,0,202,204,1,0,0,0,203,182,1,0,0,0,203,192,1,0,0,0,204,25,1,
        0,0,0,205,206,3,76,38,0,206,207,7,0,0,0,207,27,1,0,0,0,208,213,3,
        60,30,0,209,210,5,25,0,0,210,212,3,60,30,0,211,209,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,29,1,0,0,0,215,213,1,
        0,0,0,216,218,5,10,0,0,217,219,5,41,0,0,218,217,1,0,0,0,219,220,
        1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,222,1,0,0,0,222,223,
        3,32,16,0,223,225,3,12,6,0,224,226,3,38,19,0,225,224,1,0,0,0,225,
        226,1,0,0,0,226,227,1,0,0,0,227,229,5,8,0,0,228,230,5,41,0,0,229,
        228,1,0,0,0,230,231,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,
        31,1,0,0,0,233,235,3,34,17,0,234,233,1,0,0,0,235,238,1,0,0,0,236,
        234,1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,236,1,0,0,0,239,
        241,3,36,18,0,240,242,5,41,0,0,241,240,1,0,0,0,242,243,1,0,0,0,243,
        241,1,0,0,0,243,244,1,0,0,0,244,251,1,0,0,0,245,247,5,17,0,0,246,
        248,5,41,0,0,247,246,1,0,0,0,248,249,1,0,0,0,249,247,1,0,0,0,249,
        250,1,0,0,0,250,252,1,0,0,0,251,245,1,0,0,0,251,252,1,0,0,0,252,
        33,1,0,0,0,253,254,3,36,18,0,254,255,5,25,0,0,255,257,3,42,21,0,
        256,258,5,41,0,0,257,256,1,0,0,0,258,259,1,0,0,0,259,257,1,0,0,0,
        259,260,1,0,0,0,260,35,1,0,0,0,261,262,3,12,6,0,262,263,5,11,0,0,
        263,264,3,40,20,0,264,37,1,0,0,0,265,267,5,5,0,0,266,268,5,41,0,
        0,267,266,1,0,0,0,268,269,1,0,0,0,269,267,1,0,0,0,269,270,1,0,0,
        0,270,271,1,0,0,0,271,272,3,12,6,0,272,39,1,0,0,0,273,274,5,35,0,
        0,274,41,1,0,0,0,275,276,5,35,0,0,276,43,1,0,0,0,277,279,5,21,0,
        0,278,280,5,41,0,0,279,278,1,0,0,0,280,281,1,0,0,0,281,279,1,0,0,
        0,281,282,1,0,0,0,282,283,1,0,0,0,283,284,3,46,23,0,284,285,5,16,
        0,0,285,287,3,40,20,0,286,288,5,41,0,0,287,286,1,0,0,0,288,289,1,
        0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,291,1,0,0,0,291,292,3,
        12,6,0,292,294,5,20,0,0,293,295,5,41,0,0,294,293,1,0,0,0,295,296,
        1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,45,1,0,0,0,298,299,3,
        12,6,0,299,47,1,0,0,0,300,302,5,4,0,0,301,303,5,41,0,0,302,301,1,
        0,0,0,303,304,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,306,1,
        0,0,0,306,307,3,12,6,0,307,308,5,19,0,0,308,310,3,40,20,0,309,311,
        5,41,0,0,310,309,1,0,0,0,311,312,1,0,0,0,312,310,1,0,0,0,312,313,
        1,0,0,0,313,49,1,0,0,0,314,315,3,52,26,0,315,316,3,12,6,0,316,317,
        3,54,27,0,317,51,1,0,0,0,318,319,5,15,0,0,319,321,3,82,41,0,320,
        322,5,41,0,0,321,320,1,0,0,0,322,323,1,0,0,0,323,321,1,0,0,0,323,
        324,1,0,0,0,324,53,1,0,0,0,325,327,5,13,0,0,326,328,3,82,41,0,327,
        326,1,0,0,0,327,328,1,0,0,0,328,330,1,0,0,0,329,331,5,41,0,0,330,
        329,1,0,0,0,331,332,1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,
        55,1,0,0,0,334,335,5,9,0,0,335,336,3,40,20,0,336,337,5,25,0,0,337,
        339,3,58,29,0,338,340,5,41,0,0,339,338,1,0,0,0,340,341,1,0,0,0,341,
        339,1,0,0,0,341,342,1,0,0,0,342,57,1,0,0,0,343,346,3,64,32,0,344,
        346,3,62,31,0,345,343,1,0,0,0,345,344,1,0,0,0,346,59,1,0,0,0,347,
        353,3,84,42,0,348,353,3,80,40,0,349,353,3,82,41,0,350,353,3,64,32,
        0,351,353,3,62,31,0,352,347,1,0,0,0,352,348,1,0,0,0,352,349,1,0,
        0,0,352,350,1,0,0,0,352,351,1,0,0,0,353,61,1,0,0,0,354,355,3,72,
        36,0,355,356,5,31,0,0,356,357,3,64,32,0,357,358,5,32,0,0,358,63,
        1,0,0,0,359,363,3,66,33,0,360,362,3,68,34,0,361,360,1,0,0,0,362,
        365,1,0,0,0,363,361,1,0,0,0,363,364,1,0,0,0,364,65,1,0,0,0,365,363,
        1,0,0,0,366,368,7,1,0,0,367,366,1,0,0,0,367,368,1,0,0,0,368,369,
        1,0,0,0,369,370,3,70,35,0,370,67,1,0,0,0,371,372,7,1,0,0,372,373,
        3,70,35,0,373,69,1,0,0,0,374,378,3,86,43,0,375,378,3,74,37,0,376,
        378,3,76,38,0,377,374,1,0,0,0,377,375,1,0,0,0,377,376,1,0,0,0,378,
        71,1,0,0,0,379,380,7,2,0,0,380,73,1,0,0,0,381,382,3,88,44,0,382,
        383,5,24,0,0,383,384,3,88,44,0,384,75,1,0,0,0,385,386,3,88,44,0,
        386,77,1,0,0,0,387,388,5,35,0,0,388,79,1,0,0,0,389,390,5,39,0,0,
        390,81,1,0,0,0,391,392,5,34,0,0,392,83,1,0,0,0,393,394,5,40,0,0,
        394,85,1,0,0,0,395,396,7,3,0,0,396,87,1,0,0,0,397,398,7,4,0,0,398,
        89,1,0,0,0,42,94,100,114,121,128,135,148,150,157,162,174,180,184,
        189,192,196,201,203,213,220,225,231,236,243,249,251,259,269,281,
        289,296,304,312,323,327,332,341,345,352,363,367,377
    ]

class AsmParser ( Parser ):

    grammarFileName = "AsmParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'asect'", "'break'", "'continue'", "'do'", 
                     "'else'", "'end'", "'ext'", "'fi'", "'goto'", "'if'", 
                     "'is'", "'macro'", "'restore'", "'rsect'", "'save'", 
                     "'stays'", "'then'", "'tplate'", "'until'", "'wend'", 
                     "'while'", "'low'", "'high'", "'.'", "','", "'+'", 
                     "'-'", "':'", "'*'", "'>'", "'('", "')'", "'-|'" ]

    symbolicNames = [ "<INVALID>", "Asect", "Break", "Continue", "Do", "Else", 
                      "End", "Ext", "Fi", "Goto", "If", "Is", "Macro", "Restore", 
                      "Rsect", "Save", "Stays", "Then", "Tplate", "Until", 
                      "Wend", "While", "Low", "High", "DOT", "COMMA", "PLUS", 
                      "MINUS", "COLON", "ASTERISK", "ANGLE_BRACKET", "OPEN_PAREN", 
                      "CLOSE_PAREN", "LINE_MARK_MARKER", "REGISTER", "WORD", 
                      "DECIMAL_NUMBER", "BINARY_NUMBER", "HEX_NUMBER", "STRING", 
                      "CHAR", "NEWLINE", "COMMENT", "WS", "BASE64", "UNEXPECTED_TOKEN" ]

    RULE_program = 0
    RULE_section = 1
    RULE_asect_header = 2
    RULE_rsect_header = 3
    RULE_tplate_header = 4
    RULE_section_body = 5
    RULE_code_block = 6
    RULE_line_mark = 7
    RULE_line_number = 8
    RULE_filepath = 9
    RULE_break_statement = 10
    RULE_continue_statement = 11
    RULE_line = 12
    RULE_label_declaration = 13
    RULE_arguments = 14
    RULE_conditional = 15
    RULE_conditions = 16
    RULE_connective_condition = 17
    RULE_condition = 18
    RULE_else_clause = 19
    RULE_branch_mnemonic = 20
    RULE_conjunction = 21
    RULE_while_loop = 22
    RULE_while_condition = 23
    RULE_until_loop = 24
    RULE_save_restore_statement = 25
    RULE_save_statement = 26
    RULE_restore_statement = 27
    RULE_goto_statement = 28
    RULE_goto_argument = 29
    RULE_argument = 30
    RULE_byte_expr = 31
    RULE_addr_expr = 32
    RULE_first_term = 33
    RULE_add_term = 34
    RULE_term = 35
    RULE_byte_specifier = 36
    RULE_template_field = 37
    RULE_label = 38
    RULE_instruction = 39
    RULE_string = 40
    RULE_register = 41
    RULE_character = 42
    RULE_number = 43
    RULE_name = 44

    ruleNames =  [ "program", "section", "asect_header", "rsect_header", 
                   "tplate_header", "section_body", "code_block", "line_mark", 
                   "line_number", "filepath", "break_statement", "continue_statement", 
                   "line", "label_declaration", "arguments", "conditional", 
                   "conditions", "connective_condition", "condition", "else_clause", 
                   "branch_mnemonic", "conjunction", "while_loop", "while_condition", 
                   "until_loop", "save_restore_statement", "save_statement", 
                   "restore_statement", "goto_statement", "goto_argument", 
                   "argument", "byte_expr", "addr_expr", "first_term", "add_term", 
                   "term", "byte_specifier", "template_field", "label", 
                   "instruction", "string", "register", "character", "number", 
                   "name" ]

    EOF = Token.EOF
    Asect=1
    Break=2
    Continue=3
    Do=4
    Else=5
    End=6
    Ext=7
    Fi=8
    Goto=9
    If=10
    Is=11
    Macro=12
    Restore=13
    Rsect=14
    Save=15
    Stays=16
    Then=17
    Tplate=18
    Until=19
    Wend=20
    While=21
    Low=22
    High=23
    DOT=24
    COMMA=25
    PLUS=26
    MINUS=27
    COLON=28
    ASTERISK=29
    ANGLE_BRACKET=30
    OPEN_PAREN=31
    CLOSE_PAREN=32
    LINE_MARK_MARKER=33
    REGISTER=34
    WORD=35
    DECIMAL_NUMBER=36
    BINARY_NUMBER=37
    HEX_NUMBER=38
    STRING=39
    CHAR=40
    NEWLINE=41
    COMMENT=42
    WS=43
    BASE64=44
    UNEXPECTED_TOKEN=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self.current_file = ''
        self.current_line = 0
        self.current_offset = 0



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line_mark(self):
            return self.getTypedRuleContext(AsmParser.Line_markContext,0)


        def End(self):
            return self.getToken(AsmParser.End, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.SectionContext)
            else:
                return self.getTypedRuleContext(AsmParser.SectionContext,i)


        def getRuleIndex(self):
            return AsmParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AsmParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.line_mark()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.NEWLINE:
                self.state = 91
                self.match(AsmParser.NEWLINE)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Rsect) | (1 << AsmParser.Tplate))) != 0):
                self.state = 97
                self.section()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(AsmParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AsmParser.RULE_section

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AbsoluteSectionContext(SectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.SectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asect_header(self):
            return self.getTypedRuleContext(AsmParser.Asect_headerContext,0)

        def section_body(self):
            return self.getTypedRuleContext(AsmParser.Section_bodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbsoluteSection" ):
                listener.enterAbsoluteSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbsoluteSection" ):
                listener.exitAbsoluteSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbsoluteSection" ):
                return visitor.visitAbsoluteSection(self)
            else:
                return visitor.visitChildren(self)


    class TemplateSectionContext(SectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.SectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tplate_header(self):
            return self.getTypedRuleContext(AsmParser.Tplate_headerContext,0)

        def section_body(self):
            return self.getTypedRuleContext(AsmParser.Section_bodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateSection" ):
                listener.enterTemplateSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateSection" ):
                listener.exitTemplateSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateSection" ):
                return visitor.visitTemplateSection(self)
            else:
                return visitor.visitChildren(self)


    class RelocatableSectionContext(SectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.SectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def rsect_header(self):
            return self.getTypedRuleContext(AsmParser.Rsect_headerContext,0)

        def section_body(self):
            return self.getTypedRuleContext(AsmParser.Section_bodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelocatableSection" ):
                listener.enterRelocatableSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelocatableSection" ):
                listener.exitRelocatableSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelocatableSection" ):
                return visitor.visitRelocatableSection(self)
            else:
                return visitor.visitChildren(self)



    def section(self):

        localctx = AsmParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmParser.Asect]:
                localctx = AsmParser.AbsoluteSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.asect_header()
                self.state = 106
                self.section_body()
                pass
            elif token in [AsmParser.Rsect]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.rsect_header()
                self.state = 109
                self.section_body()
                pass
            elif token in [AsmParser.Tplate]:
                localctx = AsmParser.TemplateSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.tplate_header()
                self.state = 112
                self.section_body()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asect_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asect(self):
            return self.getToken(AsmParser.Asect, 0)

        def number(self):
            return self.getTypedRuleContext(AsmParser.NumberContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_asect_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsect_header" ):
                listener.enterAsect_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsect_header" ):
                listener.exitAsect_header(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsect_header" ):
                return visitor.visitAsect_header(self)
            else:
                return visitor.visitChildren(self)




    def asect_header(self):

        localctx = AsmParser.Asect_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asect_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(AsmParser.Asect)
            self.state = 117
            self.number()
            self.state = 119 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 118
                self.match(AsmParser.NEWLINE)
                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rsect_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Rsect(self):
            return self.getToken(AsmParser.Rsect, 0)

        def name(self):
            return self.getTypedRuleContext(AsmParser.NameContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_rsect_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRsect_header" ):
                listener.enterRsect_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRsect_header" ):
                listener.exitRsect_header(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRsect_header" ):
                return visitor.visitRsect_header(self)
            else:
                return visitor.visitChildren(self)




    def rsect_header(self):

        localctx = AsmParser.Rsect_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rsect_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(AsmParser.Rsect)
            self.state = 124
            self.name()
            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 125
                self.match(AsmParser.NEWLINE)
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tplate_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Tplate(self):
            return self.getToken(AsmParser.Tplate, 0)

        def name(self):
            return self.getTypedRuleContext(AsmParser.NameContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_tplate_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTplate_header" ):
                listener.enterTplate_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTplate_header" ):
                listener.exitTplate_header(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTplate_header" ):
                return visitor.visitTplate_header(self)
            else:
                return visitor.visitChildren(self)




    def tplate_header(self):

        localctx = AsmParser.Tplate_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tplate_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(AsmParser.Tplate)
            self.state = 131
            self.name()
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.match(AsmParser.NEWLINE)
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_section_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_body" ):
                listener.enterSection_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_body" ):
                listener.exitSection_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection_body" ):
                return visitor.visitSection_body(self)
            else:
                return visitor.visitChildren(self)




    def section_body(self):

        localctx = AsmParser.Section_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_section_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def break_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Break_statementContext)
            else:
                return self.getTypedRuleContext(AsmParser.Break_statementContext,i)


        def continue_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Continue_statementContext)
            else:
                return self.getTypedRuleContext(AsmParser.Continue_statementContext,i)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.LineContext)
            else:
                return self.getTypedRuleContext(AsmParser.LineContext,i)


        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(AsmParser.ConditionalContext,i)


        def while_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.While_loopContext)
            else:
                return self.getTypedRuleContext(AsmParser.While_loopContext,i)


        def until_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Until_loopContext)
            else:
                return self.getTypedRuleContext(AsmParser.Until_loopContext,i)


        def save_restore_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Save_restore_statementContext)
            else:
                return self.getTypedRuleContext(AsmParser.Save_restore_statementContext,i)


        def goto_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Goto_statementContext)
            else:
                return self.getTypedRuleContext(AsmParser.Goto_statementContext,i)


        def line_mark(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Line_markContext)
            else:
                return self.getTypedRuleContext(AsmParser.Line_markContext,i)


        def getRuleIndex(self):
            return AsmParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = AsmParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 148
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 139
                        self.break_statement()
                        pass

                    elif la_ == 2:
                        self.state = 140
                        self.continue_statement()
                        pass

                    elif la_ == 3:
                        self.state = 141
                        self.line()
                        pass

                    elif la_ == 4:
                        self.state = 142
                        self.conditional()
                        pass

                    elif la_ == 5:
                        self.state = 143
                        self.while_loop()
                        pass

                    elif la_ == 6:
                        self.state = 144
                        self.until_loop()
                        pass

                    elif la_ == 7:
                        self.state = 145
                        self.save_restore_statement()
                        pass

                    elif la_ == 8:
                        self.state = 146
                        self.goto_statement()
                        pass

                    elif la_ == 9:
                        self.state = 147
                        self.line_mark()
                        pass

             
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_markContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.source_file = ''
            self.source_line = 0
            self._line_number = None # Line_numberContext
            self._filepath = None # FilepathContext

        def LINE_MARK_MARKER(self):
            return self.getToken(AsmParser.LINE_MARK_MARKER, 0)

        def line_number(self):
            return self.getTypedRuleContext(AsmParser.Line_numberContext,0)


        def filepath(self):
            return self.getTypedRuleContext(AsmParser.FilepathContext,0)


        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_line_mark

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_mark" ):
                listener.enterLine_mark(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_mark" ):
                listener.exitLine_mark(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_mark" ):
                return visitor.visitLine_mark(self)
            else:
                return visitor.visitChildren(self)




    def line_mark(self):

        localctx = AsmParser.Line_markContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_line_mark)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 154
            localctx._line_number = self.line_number()
            self.state = 155
            localctx._filepath = self.filepath()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.WORD:
                self.state = 156
                self.match(AsmParser.WORD)


            self.state = 160 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 159
                    self.match(AsmParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 162 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)


                self.current_line = int((None if localctx._line_number is None else self._input.getText(localctx._line_number.start,localctx._line_number.stop)))
                self.current_file =  b64decode((None if localctx._filepath is None else self._input.getText(localctx._filepath.start,localctx._filepath.stop))[3:]).decode()
                localctx.source_file = self.current_file
                localctx.source_line = self.current_line
                self.current_offset = (None if localctx._line_number is None else localctx._line_number.start).line - self.current_line + 1

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_NUMBER(self):
            return self.getToken(AsmParser.DECIMAL_NUMBER, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_line_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_number" ):
                listener.enterLine_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_number" ):
                listener.exitLine_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_number" ):
                return visitor.visitLine_number(self)
            else:
                return visitor.visitChildren(self)




    def line_number(self):

        localctx = AsmParser.Line_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_line_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(AsmParser.DECIMAL_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilepathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BASE64(self):
            return self.getToken(AsmParser.BASE64, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_filepath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilepath" ):
                listener.enterFilepath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilepath" ):
                listener.exitFilepath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilepath" ):
                return visitor.visitFilepath(self)
            else:
                return visitor.visitChildren(self)




    def filepath(self):

        localctx = AsmParser.FilepathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_filepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(AsmParser.BASE64)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(AsmParser.Break, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_break_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = AsmParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(AsmParser.Break)
            self.state = 172 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 171
                self.match(AsmParser.NEWLINE)
                self.state = 174 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(AsmParser.Continue, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_continue_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_statement" ):
                listener.enterContinue_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_statement" ):
                listener.exitContinue_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = AsmParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(AsmParser.Continue)
            self.state = 178 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 177
                self.match(AsmParser.NEWLINE)
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AsmParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StandaloneLabelContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label_declaration(self):
            return self.getTypedRuleContext(AsmParser.Label_declarationContext,0)

        def Ext(self):
            return self.getToken(AsmParser.Ext, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStandaloneLabel" ):
                listener.enterStandaloneLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStandaloneLabel" ):
                listener.exitStandaloneLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStandaloneLabel" ):
                return visitor.visitStandaloneLabel(self)
            else:
                return visitor.visitChildren(self)


    class InstructionLineContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instruction(self):
            return self.getTypedRuleContext(AsmParser.InstructionContext,0)

        def label_declaration(self):
            return self.getTypedRuleContext(AsmParser.Label_declarationContext,0)

        def arguments(self):
            return self.getTypedRuleContext(AsmParser.ArgumentsContext,0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructionLine" ):
                listener.enterInstructionLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructionLine" ):
                listener.exitInstructionLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructionLine" ):
                return visitor.visitInstructionLine(self)
            else:
                return visitor.visitChildren(self)



    def line(self):

        localctx = AsmParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = AsmParser.StandaloneLabelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.label_declaration()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==AsmParser.Ext:
                    self.state = 183
                    self.match(AsmParser.Ext)


                self.state = 187 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 186
                    self.match(AsmParser.NEWLINE)
                    self.state = 189 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==AsmParser.NEWLINE):
                        break

                pass

            elif la_ == 2:
                localctx = AsmParser.InstructionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 191
                    self.label_declaration()


                self.state = 194
                self.instruction()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Break) | (1 << AsmParser.Continue) | (1 << AsmParser.Do) | (1 << AsmParser.Else) | (1 << AsmParser.End) | (1 << AsmParser.Ext) | (1 << AsmParser.Fi) | (1 << AsmParser.Goto) | (1 << AsmParser.If) | (1 << AsmParser.Is) | (1 << AsmParser.Macro) | (1 << AsmParser.Restore) | (1 << AsmParser.Rsect) | (1 << AsmParser.Save) | (1 << AsmParser.Stays) | (1 << AsmParser.Then) | (1 << AsmParser.Tplate) | (1 << AsmParser.Until) | (1 << AsmParser.Wend) | (1 << AsmParser.While) | (1 << AsmParser.Low) | (1 << AsmParser.High) | (1 << AsmParser.PLUS) | (1 << AsmParser.MINUS) | (1 << AsmParser.REGISTER) | (1 << AsmParser.WORD) | (1 << AsmParser.DECIMAL_NUMBER) | (1 << AsmParser.BINARY_NUMBER) | (1 << AsmParser.HEX_NUMBER) | (1 << AsmParser.STRING) | (1 << AsmParser.CHAR))) != 0):
                    self.state = 195
                    self.arguments()


                self.state = 199 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 198
                    self.match(AsmParser.NEWLINE)
                    self.state = 201 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==AsmParser.NEWLINE):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Label_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(AsmParser.LabelContext,0)


        def COLON(self):
            return self.getToken(AsmParser.COLON, 0)

        def ANGLE_BRACKET(self):
            return self.getToken(AsmParser.ANGLE_BRACKET, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_label_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel_declaration" ):
                listener.enterLabel_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel_declaration" ):
                listener.exitLabel_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel_declaration" ):
                return visitor.visitLabel_declaration(self)
            else:
                return visitor.visitChildren(self)




    def label_declaration(self):

        localctx = AsmParser.Label_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_label_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.label()
            self.state = 206
            _la = self._input.LA(1)
            if not(_la==AsmParser.COLON or _la==AsmParser.ANGLE_BRACKET):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(AsmParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.COMMA)
            else:
                return self.getToken(AsmParser.COMMA, i)

        def getRuleIndex(self):
            return AsmParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = AsmParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.argument()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.COMMA:
                self.state = 209
                self.match(AsmParser.COMMA)
                self.state = 210
                self.argument()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(AsmParser.If, 0)

        def conditions(self):
            return self.getTypedRuleContext(AsmParser.ConditionsContext,0)


        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def Fi(self):
            return self.getToken(AsmParser.Fi, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def else_clause(self):
            return self.getTypedRuleContext(AsmParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = AsmParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(AsmParser.If)
            self.state = 218 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 217
                self.match(AsmParser.NEWLINE)
                self.state = 220 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 222
            self.conditions()
            self.state = 223
            self.code_block()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.Else:
                self.state = 224
                self.else_clause()


            self.state = 227
            self.match(AsmParser.Fi)
            self.state = 229 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 228
                self.match(AsmParser.NEWLINE)
                self.state = 231 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AsmParser.ConditionContext,0)


        def connective_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Connective_conditionContext)
            else:
                return self.getTypedRuleContext(AsmParser.Connective_conditionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def Then(self):
            return self.getToken(AsmParser.Then, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_conditions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditions" ):
                listener.enterConditions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditions" ):
                listener.exitConditions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditions" ):
                return visitor.visitConditions(self)
            else:
                return visitor.visitChildren(self)




    def conditions(self):

        localctx = AsmParser.ConditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 233
                    self.connective_condition() 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 239
            self.condition()
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 240
                self.match(AsmParser.NEWLINE)
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 245
                self.match(AsmParser.Then)
                self.state = 247 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 246
                    self.match(AsmParser.NEWLINE)
                    self.state = 249 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==AsmParser.NEWLINE):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Connective_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AsmParser.ConditionContext,0)


        def COMMA(self):
            return self.getToken(AsmParser.COMMA, 0)

        def conjunction(self):
            return self.getTypedRuleContext(AsmParser.ConjunctionContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_connective_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConnective_condition" ):
                listener.enterConnective_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConnective_condition" ):
                listener.exitConnective_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConnective_condition" ):
                return visitor.visitConnective_condition(self)
            else:
                return visitor.visitChildren(self)




    def connective_condition(self):

        localctx = AsmParser.Connective_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_connective_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.condition()
            self.state = 254
            self.match(AsmParser.COMMA)
            self.state = 255
            self.conjunction()
            self.state = 257 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 256
                self.match(AsmParser.NEWLINE)
                self.state = 259 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def Is(self):
            return self.getToken(AsmParser.Is, 0)

        def branch_mnemonic(self):
            return self.getTypedRuleContext(AsmParser.Branch_mnemonicContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = AsmParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.code_block()
            self.state = 262
            self.match(AsmParser.Is)
            self.state = 263
            self.branch_mnemonic()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Else(self):
            return self.getToken(AsmParser.Else, 0)

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_else_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_clause" ):
                listener.enterElse_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_clause" ):
                listener.exitElse_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = AsmParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_else_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(AsmParser.Else)
            self.state = 267 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 266
                self.match(AsmParser.NEWLINE)
                self.state = 269 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 271
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Branch_mnemonicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_branch_mnemonic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch_mnemonic" ):
                listener.enterBranch_mnemonic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch_mnemonic" ):
                listener.exitBranch_mnemonic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch_mnemonic" ):
                return visitor.visitBranch_mnemonic(self)
            else:
                return visitor.visitChildren(self)




    def branch_mnemonic(self):

        localctx = AsmParser.Branch_mnemonicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_branch_mnemonic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(AsmParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_conjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)




    def conjunction(self):

        localctx = AsmParser.ConjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(AsmParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(AsmParser.While, 0)

        def while_condition(self):
            return self.getTypedRuleContext(AsmParser.While_conditionContext,0)


        def Stays(self):
            return self.getToken(AsmParser.Stays, 0)

        def branch_mnemonic(self):
            return self.getTypedRuleContext(AsmParser.Branch_mnemonicContext,0)


        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def Wend(self):
            return self.getToken(AsmParser.Wend, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = AsmParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(AsmParser.While)
            self.state = 279 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self.match(AsmParser.NEWLINE)
                self.state = 281 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 283
            self.while_condition()
            self.state = 284
            self.match(AsmParser.Stays)
            self.state = 285
            self.branch_mnemonic()
            self.state = 287 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 286
                self.match(AsmParser.NEWLINE)
                self.state = 289 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 291
            self.code_block()
            self.state = 292
            self.match(AsmParser.Wend)
            self.state = 294 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 293
                self.match(AsmParser.NEWLINE)
                self.state = 296 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_while_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_condition" ):
                listener.enterWhile_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_condition" ):
                listener.exitWhile_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_condition" ):
                return visitor.visitWhile_condition(self)
            else:
                return visitor.visitChildren(self)




    def while_condition(self):

        localctx = AsmParser.While_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_while_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Until_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Do(self):
            return self.getToken(AsmParser.Do, 0)

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def Until(self):
            return self.getToken(AsmParser.Until, 0)

        def branch_mnemonic(self):
            return self.getTypedRuleContext(AsmParser.Branch_mnemonicContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_until_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntil_loop" ):
                listener.enterUntil_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntil_loop" ):
                listener.exitUntil_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntil_loop" ):
                return visitor.visitUntil_loop(self)
            else:
                return visitor.visitChildren(self)




    def until_loop(self):

        localctx = AsmParser.Until_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_until_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(AsmParser.Do)
            self.state = 302 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 301
                self.match(AsmParser.NEWLINE)
                self.state = 304 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 306
            self.code_block()
            self.state = 307
            self.match(AsmParser.Until)
            self.state = 308
            self.branch_mnemonic()
            self.state = 310 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 309
                self.match(AsmParser.NEWLINE)
                self.state = 312 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Save_restore_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def save_statement(self):
            return self.getTypedRuleContext(AsmParser.Save_statementContext,0)


        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def restore_statement(self):
            return self.getTypedRuleContext(AsmParser.Restore_statementContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_save_restore_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSave_restore_statement" ):
                listener.enterSave_restore_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSave_restore_statement" ):
                listener.exitSave_restore_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSave_restore_statement" ):
                return visitor.visitSave_restore_statement(self)
            else:
                return visitor.visitChildren(self)




    def save_restore_statement(self):

        localctx = AsmParser.Save_restore_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_save_restore_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.save_statement()
            self.state = 315
            self.code_block()
            self.state = 316
            self.restore_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Save_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Save(self):
            return self.getToken(AsmParser.Save, 0)

        def register(self):
            return self.getTypedRuleContext(AsmParser.RegisterContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_save_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSave_statement" ):
                listener.enterSave_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSave_statement" ):
                listener.exitSave_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSave_statement" ):
                return visitor.visitSave_statement(self)
            else:
                return visitor.visitChildren(self)




    def save_statement(self):

        localctx = AsmParser.Save_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_save_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(AsmParser.Save)
            self.state = 319
            self.register()
            self.state = 321 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 320
                self.match(AsmParser.NEWLINE)
                self.state = 323 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Restore_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Restore(self):
            return self.getToken(AsmParser.Restore, 0)

        def register(self):
            return self.getTypedRuleContext(AsmParser.RegisterContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_restore_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestore_statement" ):
                listener.enterRestore_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestore_statement" ):
                listener.exitRestore_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestore_statement" ):
                return visitor.visitRestore_statement(self)
            else:
                return visitor.visitChildren(self)




    def restore_statement(self):

        localctx = AsmParser.Restore_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_restore_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(AsmParser.Restore)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.REGISTER:
                self.state = 326
                self.register()


            self.state = 330 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 329
                self.match(AsmParser.NEWLINE)
                self.state = 332 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Goto_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Goto(self):
            return self.getToken(AsmParser.Goto, 0)

        def branch_mnemonic(self):
            return self.getTypedRuleContext(AsmParser.Branch_mnemonicContext,0)


        def COMMA(self):
            return self.getToken(AsmParser.COMMA, 0)

        def goto_argument(self):
            return self.getTypedRuleContext(AsmParser.Goto_argumentContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_goto_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto_statement" ):
                listener.enterGoto_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto_statement" ):
                listener.exitGoto_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto_statement" ):
                return visitor.visitGoto_statement(self)
            else:
                return visitor.visitChildren(self)




    def goto_statement(self):

        localctx = AsmParser.Goto_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_goto_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(AsmParser.Goto)
            self.state = 335
            self.branch_mnemonic()
            self.state = 336
            self.match(AsmParser.COMMA)
            self.state = 337
            self.goto_argument()
            self.state = 339 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 338
                self.match(AsmParser.NEWLINE)
                self.state = 341 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Goto_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addr_expr(self):
            return self.getTypedRuleContext(AsmParser.Addr_exprContext,0)


        def byte_expr(self):
            return self.getTypedRuleContext(AsmParser.Byte_exprContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_goto_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto_argument" ):
                listener.enterGoto_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto_argument" ):
                listener.exitGoto_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto_argument" ):
                return visitor.visitGoto_argument(self)
            else:
                return visitor.visitChildren(self)




    def goto_argument(self):

        localctx = AsmParser.Goto_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_goto_argument)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.addr_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.byte_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def character(self):
            return self.getTypedRuleContext(AsmParser.CharacterContext,0)


        def string(self):
            return self.getTypedRuleContext(AsmParser.StringContext,0)


        def register(self):
            return self.getTypedRuleContext(AsmParser.RegisterContext,0)


        def addr_expr(self):
            return self.getTypedRuleContext(AsmParser.Addr_exprContext,0)


        def byte_expr(self):
            return self.getTypedRuleContext(AsmParser.Byte_exprContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = AsmParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_argument)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.character()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.register()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 350
                self.addr_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 351
                self.byte_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Byte_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def byte_specifier(self):
            return self.getTypedRuleContext(AsmParser.Byte_specifierContext,0)


        def OPEN_PAREN(self):
            return self.getToken(AsmParser.OPEN_PAREN, 0)

        def addr_expr(self):
            return self.getTypedRuleContext(AsmParser.Addr_exprContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(AsmParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_byte_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterByte_expr" ):
                listener.enterByte_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitByte_expr" ):
                listener.exitByte_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByte_expr" ):
                return visitor.visitByte_expr(self)
            else:
                return visitor.visitChildren(self)




    def byte_expr(self):

        localctx = AsmParser.Byte_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_byte_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.byte_specifier()
            self.state = 355
            self.match(AsmParser.OPEN_PAREN)
            self.state = 356
            self.addr_expr()
            self.state = 357
            self.match(AsmParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Addr_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def first_term(self):
            return self.getTypedRuleContext(AsmParser.First_termContext,0)


        def add_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Add_termContext)
            else:
                return self.getTypedRuleContext(AsmParser.Add_termContext,i)


        def getRuleIndex(self):
            return AsmParser.RULE_addr_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddr_expr" ):
                listener.enterAddr_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddr_expr" ):
                listener.exitAddr_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddr_expr" ):
                return visitor.visitAddr_expr(self)
            else:
                return visitor.visitChildren(self)




    def addr_expr(self):

        localctx = AsmParser.Addr_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_addr_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.first_term()
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.PLUS or _la==AsmParser.MINUS:
                self.state = 360
                self.add_term()
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class First_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(AsmParser.TermContext,0)


        def PLUS(self):
            return self.getToken(AsmParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(AsmParser.MINUS, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_first_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirst_term" ):
                listener.enterFirst_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirst_term" ):
                listener.exitFirst_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFirst_term" ):
                return visitor.visitFirst_term(self)
            else:
                return visitor.visitChildren(self)




    def first_term(self):

        localctx = AsmParser.First_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_first_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.PLUS or _la==AsmParser.MINUS:
                self.state = 366
                _la = self._input.LA(1)
                if not(_la==AsmParser.PLUS or _la==AsmParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 369
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(AsmParser.TermContext,0)


        def PLUS(self):
            return self.getToken(AsmParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(AsmParser.MINUS, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_add_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_term" ):
                listener.enterAdd_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_term" ):
                listener.exitAdd_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_term" ):
                return visitor.visitAdd_term(self)
            else:
                return visitor.visitChildren(self)




    def add_term(self):

        localctx = AsmParser.Add_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_add_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            _la = self._input.LA(1)
            if not(_la==AsmParser.PLUS or _la==AsmParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 372
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(AsmParser.NumberContext,0)


        def template_field(self):
            return self.getTypedRuleContext(AsmParser.Template_fieldContext,0)


        def label(self):
            return self.getTypedRuleContext(AsmParser.LabelContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = AsmParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_term)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.template_field()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.label()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Byte_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Low(self):
            return self.getToken(AsmParser.Low, 0)

        def High(self):
            return self.getToken(AsmParser.High, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_byte_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterByte_specifier" ):
                listener.enterByte_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitByte_specifier" ):
                listener.exitByte_specifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByte_specifier" ):
                return visitor.visitByte_specifier(self)
            else:
                return visitor.visitChildren(self)




    def byte_specifier(self):

        localctx = AsmParser.Byte_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_byte_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            _la = self._input.LA(1)
            if not(_la==AsmParser.Low or _la==AsmParser.High):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Template_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.NameContext)
            else:
                return self.getTypedRuleContext(AsmParser.NameContext,i)


        def DOT(self):
            return self.getToken(AsmParser.DOT, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_template_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate_field" ):
                listener.enterTemplate_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate_field" ):
                listener.exitTemplate_field(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplate_field" ):
                return visitor.visitTemplate_field(self)
            else:
                return visitor.visitChildren(self)




    def template_field(self):

        localctx = AsmParser.Template_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_template_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.name()
            self.state = 382
            self.match(AsmParser.DOT)
            self.state = 383
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(AsmParser.NameContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = AsmParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = AsmParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(AsmParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AsmParser.STRING, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = AsmParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(AsmParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegisterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGISTER(self):
            return self.getToken(AsmParser.REGISTER, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_register

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegister" ):
                listener.enterRegister(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegister" ):
                listener.exitRegister(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegister" ):
                return visitor.visitRegister(self)
            else:
                return visitor.visitChildren(self)




    def register(self):

        localctx = AsmParser.RegisterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(AsmParser.REGISTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(AsmParser.CHAR, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_character

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacter" ):
                listener.enterCharacter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacter" ):
                listener.exitCharacter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacter" ):
                return visitor.visitCharacter(self)
            else:
                return visitor.visitChildren(self)




    def character(self):

        localctx = AsmParser.CharacterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_character)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(AsmParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_NUMBER(self):
            return self.getToken(AsmParser.DECIMAL_NUMBER, 0)

        def HEX_NUMBER(self):
            return self.getToken(AsmParser.HEX_NUMBER, 0)

        def BINARY_NUMBER(self):
            return self.getToken(AsmParser.BINARY_NUMBER, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = AsmParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.DECIMAL_NUMBER) | (1 << AsmParser.BINARY_NUMBER) | (1 << AsmParser.HEX_NUMBER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asect(self):
            return self.getToken(AsmParser.Asect, 0)

        def Break(self):
            return self.getToken(AsmParser.Break, 0)

        def Continue(self):
            return self.getToken(AsmParser.Continue, 0)

        def Do(self):
            return self.getToken(AsmParser.Do, 0)

        def Else(self):
            return self.getToken(AsmParser.Else, 0)

        def End(self):
            return self.getToken(AsmParser.End, 0)

        def Ext(self):
            return self.getToken(AsmParser.Ext, 0)

        def Fi(self):
            return self.getToken(AsmParser.Fi, 0)

        def Goto(self):
            return self.getToken(AsmParser.Goto, 0)

        def High(self):
            return self.getToken(AsmParser.High, 0)

        def If(self):
            return self.getToken(AsmParser.If, 0)

        def Is(self):
            return self.getToken(AsmParser.Is, 0)

        def Low(self):
            return self.getToken(AsmParser.Low, 0)

        def Macro(self):
            return self.getToken(AsmParser.Macro, 0)

        def Restore(self):
            return self.getToken(AsmParser.Restore, 0)

        def Rsect(self):
            return self.getToken(AsmParser.Rsect, 0)

        def Save(self):
            return self.getToken(AsmParser.Save, 0)

        def Stays(self):
            return self.getToken(AsmParser.Stays, 0)

        def Then(self):
            return self.getToken(AsmParser.Then, 0)

        def Tplate(self):
            return self.getToken(AsmParser.Tplate, 0)

        def Until(self):
            return self.getToken(AsmParser.Until, 0)

        def Wend(self):
            return self.getToken(AsmParser.Wend, 0)

        def While(self):
            return self.getToken(AsmParser.While, 0)

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = AsmParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Break) | (1 << AsmParser.Continue) | (1 << AsmParser.Do) | (1 << AsmParser.Else) | (1 << AsmParser.End) | (1 << AsmParser.Ext) | (1 << AsmParser.Fi) | (1 << AsmParser.Goto) | (1 << AsmParser.If) | (1 << AsmParser.Is) | (1 << AsmParser.Macro) | (1 << AsmParser.Restore) | (1 << AsmParser.Rsect) | (1 << AsmParser.Save) | (1 << AsmParser.Stays) | (1 << AsmParser.Then) | (1 << AsmParser.Tplate) | (1 << AsmParser.Until) | (1 << AsmParser.Wend) | (1 << AsmParser.While) | (1 << AsmParser.Low) | (1 << AsmParser.High) | (1 << AsmParser.WORD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





