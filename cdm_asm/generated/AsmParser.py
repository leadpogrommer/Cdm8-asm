# Generated from AsmParser.g4 by ANTLR 4.10.1
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
        4,1,45,425,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,5,0,98,8,0,10,0,12,0,101,9,0,1,0,4,0,104,8,0,
        11,0,12,0,105,1,0,5,0,109,8,0,10,0,12,0,112,9,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,125,8,1,1,2,1,2,1,2,4,2,130,8,2,
        11,2,12,2,131,1,3,1,3,1,3,4,3,137,8,3,11,3,12,3,138,1,4,1,4,1,4,
        4,4,144,8,4,11,4,12,4,145,1,5,1,5,1,6,1,6,3,6,152,8,6,1,6,1,6,5,
        6,156,8,6,10,6,12,6,159,9,6,1,7,1,7,1,7,3,7,164,8,7,1,7,4,7,167,
        8,7,11,7,12,7,168,1,7,1,7,1,7,4,7,174,8,7,11,7,12,7,175,3,7,178,
        8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,191,8,9,1,10,
        1,10,1,10,1,10,3,10,197,8,10,1,10,4,10,200,8,10,11,10,12,10,201,
        1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,4,13,212,8,13,11,13,12,13,
        213,1,14,1,14,4,14,218,8,14,11,14,12,14,219,1,15,1,15,3,15,224,8,
        15,1,15,4,15,227,8,15,11,15,12,15,228,1,16,1,16,1,16,1,17,1,17,1,
        17,5,17,237,8,17,10,17,12,17,240,9,17,1,18,1,18,4,18,244,8,18,11,
        18,12,18,245,1,18,1,18,1,18,3,18,251,8,18,1,18,1,18,4,18,255,8,18,
        11,18,12,18,256,1,19,5,19,260,8,19,10,19,12,19,263,9,19,1,19,1,19,
        4,19,267,8,19,11,19,12,19,268,1,19,1,19,4,19,273,8,19,11,19,12,19,
        274,3,19,277,8,19,1,20,1,20,1,20,1,20,4,20,283,8,20,11,20,12,20,
        284,1,21,1,21,1,21,1,21,1,22,1,22,4,22,293,8,22,11,22,12,22,294,
        1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,4,25,305,8,25,11,25,12,25,
        306,1,25,1,25,1,25,1,25,4,25,313,8,25,11,25,12,25,314,1,25,1,25,
        1,25,4,25,320,8,25,11,25,12,25,321,1,26,1,26,1,27,1,27,4,27,328,
        8,27,11,27,12,27,329,1,27,1,27,1,27,1,27,4,27,336,8,27,11,27,12,
        27,337,1,28,1,28,1,28,1,28,1,29,1,29,1,29,4,29,347,8,29,11,29,12,
        29,348,1,30,1,30,3,30,353,8,30,1,30,4,30,356,8,30,11,30,12,30,357,
        1,31,1,31,1,31,1,31,1,31,4,31,365,8,31,11,31,12,31,366,1,32,1,32,
        3,32,371,8,32,1,33,1,33,1,33,1,33,1,33,3,33,378,8,33,1,34,1,34,1,
        34,1,34,1,34,1,35,1,35,5,35,387,8,35,10,35,12,35,390,9,35,1,36,3,
        36,393,8,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,3,38,403,8,38,
        1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,
        1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,47,0,0,48,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,0,5,2,0,28,
        28,30,30,1,0,26,27,1,0,22,23,1,0,36,38,2,0,1,23,35,35,433,0,99,1,
        0,0,0,2,124,1,0,0,0,4,126,1,0,0,0,6,133,1,0,0,0,8,140,1,0,0,0,10,
        147,1,0,0,0,12,157,1,0,0,0,14,177,1,0,0,0,16,179,1,0,0,0,18,190,
        1,0,0,0,20,192,1,0,0,0,22,205,1,0,0,0,24,207,1,0,0,0,26,209,1,0,
        0,0,28,215,1,0,0,0,30,221,1,0,0,0,32,230,1,0,0,0,34,233,1,0,0,0,
        36,241,1,0,0,0,38,261,1,0,0,0,40,278,1,0,0,0,42,286,1,0,0,0,44,290,
        1,0,0,0,46,298,1,0,0,0,48,300,1,0,0,0,50,302,1,0,0,0,52,323,1,0,
        0,0,54,325,1,0,0,0,56,339,1,0,0,0,58,343,1,0,0,0,60,350,1,0,0,0,
        62,359,1,0,0,0,64,370,1,0,0,0,66,377,1,0,0,0,68,379,1,0,0,0,70,384,
        1,0,0,0,72,392,1,0,0,0,74,396,1,0,0,0,76,402,1,0,0,0,78,404,1,0,
        0,0,80,406,1,0,0,0,82,410,1,0,0,0,84,412,1,0,0,0,86,414,1,0,0,0,
        88,416,1,0,0,0,90,418,1,0,0,0,92,420,1,0,0,0,94,422,1,0,0,0,96,98,
        5,41,0,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,
        0,100,103,1,0,0,0,101,99,1,0,0,0,102,104,3,20,10,0,103,102,1,0,0,
        0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,110,1,0,0,
        0,107,109,3,2,1,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,
        0,110,111,1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,114,5,6,0,
        0,114,1,1,0,0,0,115,116,3,4,2,0,116,117,3,10,5,0,117,125,1,0,0,0,
        118,119,3,6,3,0,119,120,3,10,5,0,120,125,1,0,0,0,121,122,3,8,4,0,
        122,123,3,10,5,0,123,125,1,0,0,0,124,115,1,0,0,0,124,118,1,0,0,0,
        124,121,1,0,0,0,125,3,1,0,0,0,126,127,5,1,0,0,127,129,3,92,46,0,
        128,130,5,41,0,0,129,128,1,0,0,0,130,131,1,0,0,0,131,129,1,0,0,0,
        131,132,1,0,0,0,132,5,1,0,0,0,133,134,5,14,0,0,134,136,3,94,47,0,
        135,137,5,41,0,0,136,135,1,0,0,0,137,138,1,0,0,0,138,136,1,0,0,0,
        138,139,1,0,0,0,139,7,1,0,0,0,140,141,5,18,0,0,141,143,3,94,47,0,
        142,144,5,41,0,0,143,142,1,0,0,0,144,145,1,0,0,0,145,143,1,0,0,0,
        145,146,1,0,0,0,146,9,1,0,0,0,147,148,3,12,6,0,148,11,1,0,0,0,149,
        156,3,14,7,0,150,152,3,16,8,0,151,150,1,0,0,0,151,152,1,0,0,0,152,
        153,1,0,0,0,153,156,3,18,9,0,154,156,3,20,10,0,155,149,1,0,0,0,155,
        151,1,0,0,0,155,154,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,
        158,1,0,0,0,158,13,1,0,0,0,159,157,1,0,0,0,160,161,3,82,41,0,161,
        163,5,28,0,0,162,164,5,7,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,
        166,1,0,0,0,165,167,5,41,0,0,166,165,1,0,0,0,167,168,1,0,0,0,168,
        166,1,0,0,0,168,169,1,0,0,0,169,178,1,0,0,0,170,171,3,82,41,0,171,
        173,5,30,0,0,172,174,5,41,0,0,173,172,1,0,0,0,174,175,1,0,0,0,175,
        173,1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,160,1,0,0,0,177,
        170,1,0,0,0,178,15,1,0,0,0,179,180,3,82,41,0,180,181,7,0,0,0,181,
        17,1,0,0,0,182,191,3,26,13,0,183,191,3,28,14,0,184,191,3,30,15,0,
        185,191,3,36,18,0,186,191,3,50,25,0,187,191,3,54,27,0,188,191,3,
        56,28,0,189,191,3,62,31,0,190,182,1,0,0,0,190,183,1,0,0,0,190,184,
        1,0,0,0,190,185,1,0,0,0,190,186,1,0,0,0,190,187,1,0,0,0,190,188,
        1,0,0,0,190,189,1,0,0,0,191,19,1,0,0,0,192,193,5,33,0,0,193,194,
        3,22,11,0,194,196,3,24,12,0,195,197,5,35,0,0,196,195,1,0,0,0,196,
        197,1,0,0,0,197,199,1,0,0,0,198,200,5,41,0,0,199,198,1,0,0,0,200,
        201,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,203,1,0,0,0,203,
        204,6,10,-1,0,204,21,1,0,0,0,205,206,5,36,0,0,206,23,1,0,0,0,207,
        208,5,44,0,0,208,25,1,0,0,0,209,211,5,2,0,0,210,212,5,41,0,0,211,
        210,1,0,0,0,212,213,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,
        27,1,0,0,0,215,217,5,3,0,0,216,218,5,41,0,0,217,216,1,0,0,0,218,
        219,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,29,1,0,0,0,221,223,
        3,84,42,0,222,224,3,34,17,0,223,222,1,0,0,0,223,224,1,0,0,0,224,
        226,1,0,0,0,225,227,5,41,0,0,226,225,1,0,0,0,227,228,1,0,0,0,228,
        226,1,0,0,0,228,229,1,0,0,0,229,31,1,0,0,0,230,231,3,82,41,0,231,
        232,7,0,0,0,232,33,1,0,0,0,233,238,3,66,33,0,234,235,5,25,0,0,235,
        237,3,66,33,0,236,234,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,
        239,1,0,0,0,239,35,1,0,0,0,240,238,1,0,0,0,241,243,5,10,0,0,242,
        244,5,41,0,0,243,242,1,0,0,0,244,245,1,0,0,0,245,243,1,0,0,0,245,
        246,1,0,0,0,246,247,1,0,0,0,247,248,3,38,19,0,248,250,3,12,6,0,249,
        251,3,44,22,0,250,249,1,0,0,0,250,251,1,0,0,0,251,252,1,0,0,0,252,
        254,5,8,0,0,253,255,5,41,0,0,254,253,1,0,0,0,255,256,1,0,0,0,256,
        254,1,0,0,0,256,257,1,0,0,0,257,37,1,0,0,0,258,260,3,40,20,0,259,
        258,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,
        264,1,0,0,0,263,261,1,0,0,0,264,266,3,42,21,0,265,267,5,41,0,0,266,
        265,1,0,0,0,267,268,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,
        276,1,0,0,0,270,272,5,17,0,0,271,273,5,41,0,0,272,271,1,0,0,0,273,
        274,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,277,1,0,0,0,276,
        270,1,0,0,0,276,277,1,0,0,0,277,39,1,0,0,0,278,279,3,42,21,0,279,
        280,5,25,0,0,280,282,3,48,24,0,281,283,5,41,0,0,282,281,1,0,0,0,
        283,284,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,41,1,0,0,0,286,
        287,3,12,6,0,287,288,5,11,0,0,288,289,3,46,23,0,289,43,1,0,0,0,290,
        292,5,5,0,0,291,293,5,41,0,0,292,291,1,0,0,0,293,294,1,0,0,0,294,
        292,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,297,3,12,6,0,297,
        45,1,0,0,0,298,299,5,35,0,0,299,47,1,0,0,0,300,301,5,35,0,0,301,
        49,1,0,0,0,302,304,5,21,0,0,303,305,5,41,0,0,304,303,1,0,0,0,305,
        306,1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,308,1,0,0,0,308,
        309,3,52,26,0,309,310,5,16,0,0,310,312,3,46,23,0,311,313,5,41,0,
        0,312,311,1,0,0,0,313,314,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,
        0,315,316,1,0,0,0,316,317,3,12,6,0,317,319,5,20,0,0,318,320,5,41,
        0,0,319,318,1,0,0,0,320,321,1,0,0,0,321,319,1,0,0,0,321,322,1,0,
        0,0,322,51,1,0,0,0,323,324,3,12,6,0,324,53,1,0,0,0,325,327,5,4,0,
        0,326,328,5,41,0,0,327,326,1,0,0,0,328,329,1,0,0,0,329,327,1,0,0,
        0,329,330,1,0,0,0,330,331,1,0,0,0,331,332,3,12,6,0,332,333,5,19,
        0,0,333,335,3,46,23,0,334,336,5,41,0,0,335,334,1,0,0,0,336,337,1,
        0,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,55,1,0,0,0,339,340,3,58,
        29,0,340,341,3,12,6,0,341,342,3,60,30,0,342,57,1,0,0,0,343,344,5,
        15,0,0,344,346,3,88,44,0,345,347,5,41,0,0,346,345,1,0,0,0,347,348,
        1,0,0,0,348,346,1,0,0,0,348,349,1,0,0,0,349,59,1,0,0,0,350,352,5,
        13,0,0,351,353,3,88,44,0,352,351,1,0,0,0,352,353,1,0,0,0,353,355,
        1,0,0,0,354,356,5,41,0,0,355,354,1,0,0,0,356,357,1,0,0,0,357,355,
        1,0,0,0,357,358,1,0,0,0,358,61,1,0,0,0,359,360,5,9,0,0,360,361,3,
        46,23,0,361,362,5,25,0,0,362,364,3,64,32,0,363,365,5,41,0,0,364,
        363,1,0,0,0,365,366,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,
        63,1,0,0,0,368,371,3,70,35,0,369,371,3,68,34,0,370,368,1,0,0,0,370,
        369,1,0,0,0,371,65,1,0,0,0,372,378,3,90,45,0,373,378,3,86,43,0,374,
        378,3,88,44,0,375,378,3,70,35,0,376,378,3,68,34,0,377,372,1,0,0,
        0,377,373,1,0,0,0,377,374,1,0,0,0,377,375,1,0,0,0,377,376,1,0,0,
        0,378,67,1,0,0,0,379,380,3,78,39,0,380,381,5,31,0,0,381,382,3,70,
        35,0,382,383,5,32,0,0,383,69,1,0,0,0,384,388,3,72,36,0,385,387,3,
        74,37,0,386,385,1,0,0,0,387,390,1,0,0,0,388,386,1,0,0,0,388,389,
        1,0,0,0,389,71,1,0,0,0,390,388,1,0,0,0,391,393,7,1,0,0,392,391,1,
        0,0,0,392,393,1,0,0,0,393,394,1,0,0,0,394,395,3,76,38,0,395,73,1,
        0,0,0,396,397,7,1,0,0,397,398,3,76,38,0,398,75,1,0,0,0,399,403,3,
        92,46,0,400,403,3,80,40,0,401,403,3,82,41,0,402,399,1,0,0,0,402,
        400,1,0,0,0,402,401,1,0,0,0,403,77,1,0,0,0,404,405,7,2,0,0,405,79,
        1,0,0,0,406,407,3,94,47,0,407,408,5,24,0,0,408,409,3,94,47,0,409,
        81,1,0,0,0,410,411,3,94,47,0,411,83,1,0,0,0,412,413,5,35,0,0,413,
        85,1,0,0,0,414,415,5,39,0,0,415,87,1,0,0,0,416,417,5,34,0,0,417,
        89,1,0,0,0,418,419,5,40,0,0,419,91,1,0,0,0,420,421,7,3,0,0,421,93,
        1,0,0,0,422,423,7,4,0,0,423,95,1,0,0,0,45,99,105,110,124,131,138,
        145,151,155,157,163,168,175,177,190,196,201,213,219,223,228,238,
        245,250,256,261,268,274,276,284,294,306,314,321,329,337,348,352,
        357,366,370,377,388,392,402
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
    RULE_standalone_label = 7
    RULE_line_label = 8
    RULE_statement = 9
    RULE_line_mark = 10
    RULE_line_number = 11
    RULE_filepath = 12
    RULE_break_statement = 13
    RULE_continue_statement = 14
    RULE_instruction_line = 15
    RULE_label_declaration = 16
    RULE_arguments = 17
    RULE_conditional = 18
    RULE_conditions = 19
    RULE_connective_condition = 20
    RULE_condition = 21
    RULE_else_clause = 22
    RULE_branch_mnemonic = 23
    RULE_conjunction = 24
    RULE_while_loop = 25
    RULE_while_condition = 26
    RULE_until_loop = 27
    RULE_save_restore_statement = 28
    RULE_save_statement = 29
    RULE_restore_statement = 30
    RULE_goto_statement = 31
    RULE_goto_argument = 32
    RULE_argument = 33
    RULE_byte_expr = 34
    RULE_addr_expr = 35
    RULE_first_term = 36
    RULE_add_term = 37
    RULE_term = 38
    RULE_byte_specifier = 39
    RULE_template_field = 40
    RULE_label = 41
    RULE_instruction = 42
    RULE_string = 43
    RULE_register = 44
    RULE_character = 45
    RULE_number = 46
    RULE_name = 47

    ruleNames =  [ "program", "section", "asect_header", "rsect_header", 
                   "tplate_header", "section_body", "code_block", "standalone_label", 
                   "line_label", "statement", "line_mark", "line_number", 
                   "filepath", "break_statement", "continue_statement", 
                   "instruction_line", "label_declaration", "arguments", 
                   "conditional", "conditions", "connective_condition", 
                   "condition", "else_clause", "branch_mnemonic", "conjunction", 
                   "while_loop", "while_condition", "until_loop", "save_restore_statement", 
                   "save_statement", "restore_statement", "goto_statement", 
                   "goto_argument", "argument", "byte_expr", "addr_expr", 
                   "first_term", "add_term", "term", "byte_specifier", "template_field", 
                   "label", "instruction", "string", "register", "character", 
                   "number", "name" ]

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

        def End(self):
            return self.getToken(AsmParser.End, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def line_mark(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Line_markContext)
            else:
                return self.getTypedRuleContext(AsmParser.Line_markContext,i)


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
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.NEWLINE:
                self.state = 96
                self.match(AsmParser.NEWLINE)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.line_mark()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.LINE_MARK_MARKER):
                    break

            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Rsect) | (1 << AsmParser.Tplate))) != 0):
                self.state = 107
                self.section()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
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
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmParser.Asect]:
                localctx = AsmParser.AbsoluteSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.asect_header()
                self.state = 116
                self.section_body()
                pass
            elif token in [AsmParser.Rsect]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.rsect_header()
                self.state = 119
                self.section_body()
                pass
            elif token in [AsmParser.Tplate]:
                localctx = AsmParser.TemplateSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.tplate_header()
                self.state = 122
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
            self.state = 126
            self.match(AsmParser.Asect)
            self.state = 127
            self.number()
            self.state = 129 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 128
                self.match(AsmParser.NEWLINE)
                self.state = 131 
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
            self.state = 133
            self.match(AsmParser.Rsect)
            self.state = 134
            self.name()
            self.state = 136 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 135
                self.match(AsmParser.NEWLINE)
                self.state = 138 
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
            self.state = 140
            self.match(AsmParser.Tplate)
            self.state = 141
            self.name()
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.match(AsmParser.NEWLINE)
                self.state = 145 
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
            self.state = 147
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

        def standalone_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Standalone_labelContext)
            else:
                return self.getTypedRuleContext(AsmParser.Standalone_labelContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.StatementContext)
            else:
                return self.getTypedRuleContext(AsmParser.StatementContext,i)


        def line_mark(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Line_markContext)
            else:
                return self.getTypedRuleContext(AsmParser.Line_markContext,i)


        def line_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Line_labelContext)
            else:
                return self.getTypedRuleContext(AsmParser.Line_labelContext,i)


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
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 155
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        self.state = 149
                        self.standalone_label()
                        pass

                    elif la_ == 2:
                        self.state = 151
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                        if la_ == 1:
                            self.state = 150
                            self.line_label()


                        self.state = 153
                        self.statement()
                        pass

                    elif la_ == 3:
                        self.state = 154
                        self.line_mark()
                        pass

             
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Standalone_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(AsmParser.LabelContext,0)


        def COLON(self):
            return self.getToken(AsmParser.COLON, 0)

        def Ext(self):
            return self.getToken(AsmParser.Ext, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def ANGLE_BRACKET(self):
            return self.getToken(AsmParser.ANGLE_BRACKET, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_standalone_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStandalone_label" ):
                listener.enterStandalone_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStandalone_label" ):
                listener.exitStandalone_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStandalone_label" ):
                return visitor.visitStandalone_label(self)
            else:
                return visitor.visitChildren(self)




    def standalone_label(self):

        localctx = AsmParser.Standalone_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_standalone_label)
        self._la = 0 # Token type
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.label()
                self.state = 161
                self.match(AsmParser.COLON)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==AsmParser.Ext:
                    self.state = 162
                    self.match(AsmParser.Ext)


                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 165
                    self.match(AsmParser.NEWLINE)
                    self.state = 168 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==AsmParser.NEWLINE):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.label()
                self.state = 171
                self.match(AsmParser.ANGLE_BRACKET)
                self.state = 173 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 172
                    self.match(AsmParser.NEWLINE)
                    self.state = 175 
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


    class Line_labelContext(ParserRuleContext):
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
            return AsmParser.RULE_line_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_label" ):
                listener.enterLine_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_label" ):
                listener.exitLine_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_label" ):
                return visitor.visitLine_label(self)
            else:
                return visitor.visitChildren(self)




    def line_label(self):

        localctx = AsmParser.Line_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_line_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.label()
            self.state = 180
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def break_statement(self):
            return self.getTypedRuleContext(AsmParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(AsmParser.Continue_statementContext,0)


        def instruction_line(self):
            return self.getTypedRuleContext(AsmParser.Instruction_lineContext,0)


        def conditional(self):
            return self.getTypedRuleContext(AsmParser.ConditionalContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(AsmParser.While_loopContext,0)


        def until_loop(self):
            return self.getTypedRuleContext(AsmParser.Until_loopContext,0)


        def save_restore_statement(self):
            return self.getTypedRuleContext(AsmParser.Save_restore_statementContext,0)


        def goto_statement(self):
            return self.getTypedRuleContext(AsmParser.Goto_statementContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AsmParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmParser.Break]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.break_statement()
                pass
            elif token in [AsmParser.Continue]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.continue_statement()
                pass
            elif token in [AsmParser.WORD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.instruction_line()
                pass
            elif token in [AsmParser.If]:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.conditional()
                pass
            elif token in [AsmParser.While]:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.while_loop()
                pass
            elif token in [AsmParser.Do]:
                self.enterOuterAlt(localctx, 6)
                self.state = 187
                self.until_loop()
                pass
            elif token in [AsmParser.Save]:
                self.enterOuterAlt(localctx, 7)
                self.state = 188
                self.save_restore_statement()
                pass
            elif token in [AsmParser.Goto]:
                self.enterOuterAlt(localctx, 8)
                self.state = 189
                self.goto_statement()
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
        self.enterRule(localctx, 20, self.RULE_line_mark)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 193
            localctx._line_number = self.line_number()
            self.state = 194
            localctx._filepath = self.filepath()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.WORD:
                self.state = 195
                self.match(AsmParser.WORD)


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
        self.enterRule(localctx, 22, self.RULE_line_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
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
        self.enterRule(localctx, 24, self.RULE_filepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
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
        self.enterRule(localctx, 26, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(AsmParser.Break)
            self.state = 211 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 210
                self.match(AsmParser.NEWLINE)
                self.state = 213 
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
        self.enterRule(localctx, 28, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(AsmParser.Continue)
            self.state = 217 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 216
                self.match(AsmParser.NEWLINE)
                self.state = 219 
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


    class Instruction_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self):
            return self.getTypedRuleContext(AsmParser.InstructionContext,0)


        def arguments(self):
            return self.getTypedRuleContext(AsmParser.ArgumentsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_instruction_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction_line" ):
                listener.enterInstruction_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction_line" ):
                listener.exitInstruction_line(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction_line" ):
                return visitor.visitInstruction_line(self)
            else:
                return visitor.visitChildren(self)




    def instruction_line(self):

        localctx = AsmParser.Instruction_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_instruction_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.instruction()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Break) | (1 << AsmParser.Continue) | (1 << AsmParser.Do) | (1 << AsmParser.Else) | (1 << AsmParser.End) | (1 << AsmParser.Ext) | (1 << AsmParser.Fi) | (1 << AsmParser.Goto) | (1 << AsmParser.If) | (1 << AsmParser.Is) | (1 << AsmParser.Macro) | (1 << AsmParser.Restore) | (1 << AsmParser.Rsect) | (1 << AsmParser.Save) | (1 << AsmParser.Stays) | (1 << AsmParser.Then) | (1 << AsmParser.Tplate) | (1 << AsmParser.Until) | (1 << AsmParser.Wend) | (1 << AsmParser.While) | (1 << AsmParser.Low) | (1 << AsmParser.High) | (1 << AsmParser.PLUS) | (1 << AsmParser.MINUS) | (1 << AsmParser.REGISTER) | (1 << AsmParser.WORD) | (1 << AsmParser.DECIMAL_NUMBER) | (1 << AsmParser.BINARY_NUMBER) | (1 << AsmParser.HEX_NUMBER) | (1 << AsmParser.STRING) | (1 << AsmParser.CHAR))) != 0):
                self.state = 222
                self.arguments()


            self.state = 226 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 225
                self.match(AsmParser.NEWLINE)
                self.state = 228 
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
        self.enterRule(localctx, 32, self.RULE_label_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.label()
            self.state = 231
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
        self.enterRule(localctx, 34, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.argument()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.COMMA:
                self.state = 234
                self.match(AsmParser.COMMA)
                self.state = 235
                self.argument()
                self.state = 240
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
        self.enterRule(localctx, 36, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(AsmParser.If)
            self.state = 243 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 242
                self.match(AsmParser.NEWLINE)
                self.state = 245 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 247
            self.conditions()
            self.state = 248
            self.code_block()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.Else:
                self.state = 249
                self.else_clause()


            self.state = 252
            self.match(AsmParser.Fi)
            self.state = 254 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 253
                self.match(AsmParser.NEWLINE)
                self.state = 256 
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
        self.enterRule(localctx, 38, self.RULE_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 258
                    self.connective_condition() 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 264
            self.condition()
            self.state = 266 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 265
                self.match(AsmParser.NEWLINE)
                self.state = 268 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 270
                self.match(AsmParser.Then)
                self.state = 272 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 271
                    self.match(AsmParser.NEWLINE)
                    self.state = 274 
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
        self.enterRule(localctx, 40, self.RULE_connective_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.condition()
            self.state = 279
            self.match(AsmParser.COMMA)
            self.state = 280
            self.conjunction()
            self.state = 282 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 281
                self.match(AsmParser.NEWLINE)
                self.state = 284 
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
        self.enterRule(localctx, 42, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.code_block()
            self.state = 287
            self.match(AsmParser.Is)
            self.state = 288
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
        self.enterRule(localctx, 44, self.RULE_else_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(AsmParser.Else)
            self.state = 292 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 291
                self.match(AsmParser.NEWLINE)
                self.state = 294 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 296
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
        self.enterRule(localctx, 46, self.RULE_branch_mnemonic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
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
        self.enterRule(localctx, 48, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
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
        self.enterRule(localctx, 50, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(AsmParser.While)
            self.state = 304 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 303
                self.match(AsmParser.NEWLINE)
                self.state = 306 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 308
            self.while_condition()
            self.state = 309
            self.match(AsmParser.Stays)
            self.state = 310
            self.branch_mnemonic()
            self.state = 312 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 311
                self.match(AsmParser.NEWLINE)
                self.state = 314 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 316
            self.code_block()
            self.state = 317
            self.match(AsmParser.Wend)
            self.state = 319 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 318
                self.match(AsmParser.NEWLINE)
                self.state = 321 
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
        self.enterRule(localctx, 52, self.RULE_while_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
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
        self.enterRule(localctx, 54, self.RULE_until_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(AsmParser.Do)
            self.state = 327 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 326
                self.match(AsmParser.NEWLINE)
                self.state = 329 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 331
            self.code_block()
            self.state = 332
            self.match(AsmParser.Until)
            self.state = 333
            self.branch_mnemonic()
            self.state = 335 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 334
                self.match(AsmParser.NEWLINE)
                self.state = 337 
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
        self.enterRule(localctx, 56, self.RULE_save_restore_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.save_statement()
            self.state = 340
            self.code_block()
            self.state = 341
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
        self.enterRule(localctx, 58, self.RULE_save_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(AsmParser.Save)
            self.state = 344
            self.register()
            self.state = 346 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 345
                self.match(AsmParser.NEWLINE)
                self.state = 348 
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
        self.enterRule(localctx, 60, self.RULE_restore_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(AsmParser.Restore)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.REGISTER:
                self.state = 351
                self.register()


            self.state = 355 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 354
                self.match(AsmParser.NEWLINE)
                self.state = 357 
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
        self.enterRule(localctx, 62, self.RULE_goto_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(AsmParser.Goto)
            self.state = 360
            self.branch_mnemonic()
            self.state = 361
            self.match(AsmParser.COMMA)
            self.state = 362
            self.goto_argument()
            self.state = 364 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 363
                self.match(AsmParser.NEWLINE)
                self.state = 366 
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
        self.enterRule(localctx, 64, self.RULE_goto_argument)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.addr_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
        self.enterRule(localctx, 66, self.RULE_argument)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.character()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
                self.register()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                self.addr_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 376
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
        self.enterRule(localctx, 68, self.RULE_byte_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.byte_specifier()
            self.state = 380
            self.match(AsmParser.OPEN_PAREN)
            self.state = 381
            self.addr_expr()
            self.state = 382
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
        self.enterRule(localctx, 70, self.RULE_addr_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.first_term()
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.PLUS or _la==AsmParser.MINUS:
                self.state = 385
                self.add_term()
                self.state = 390
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
        self.enterRule(localctx, 72, self.RULE_first_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.PLUS or _la==AsmParser.MINUS:
                self.state = 391
                _la = self._input.LA(1)
                if not(_la==AsmParser.PLUS or _la==AsmParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 394
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
        self.enterRule(localctx, 74, self.RULE_add_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            _la = self._input.LA(1)
            if not(_la==AsmParser.PLUS or _la==AsmParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 397
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
        self.enterRule(localctx, 76, self.RULE_term)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.template_field()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
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
        self.enterRule(localctx, 78, self.RULE_byte_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
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
        self.enterRule(localctx, 80, self.RULE_template_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.name()
            self.state = 407
            self.match(AsmParser.DOT)
            self.state = 408
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
        self.enterRule(localctx, 82, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
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
        self.enterRule(localctx, 84, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
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
        self.enterRule(localctx, 86, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
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
        self.enterRule(localctx, 88, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
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
        self.enterRule(localctx, 90, self.RULE_character)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
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
        self.enterRule(localctx, 92, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
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
        self.enterRule(localctx, 94, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
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





