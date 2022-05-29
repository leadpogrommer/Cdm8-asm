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
        4,1,47,463,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,1,0,5,0,106,
        8,0,10,0,12,0,109,9,0,1,0,5,0,112,8,0,10,0,12,0,115,9,0,1,0,5,0,
        118,8,0,10,0,12,0,121,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,134,8,1,1,2,1,2,1,2,4,2,139,8,2,11,2,12,2,140,1,3,1,3,
        1,3,4,3,146,8,3,11,3,12,3,147,1,4,1,4,1,4,4,4,153,8,4,11,4,12,4,
        154,1,5,1,5,1,6,1,6,3,6,161,8,6,1,6,1,6,5,6,165,8,6,10,6,12,6,168,
        9,6,1,7,1,7,1,7,3,7,173,8,7,1,7,4,7,176,8,7,11,7,12,7,177,1,7,1,
        7,1,7,4,7,183,8,7,11,7,12,7,184,3,7,187,8,7,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,202,8,9,1,10,1,10,1,10,1,10,
        3,10,208,8,10,1,10,4,10,211,8,10,11,10,12,10,212,1,10,1,10,1,11,
        1,11,1,12,1,12,1,13,1,13,4,13,223,8,13,11,13,12,13,224,1,14,1,14,
        4,14,229,8,14,11,14,12,14,230,1,15,1,15,3,15,235,8,15,1,15,4,15,
        238,8,15,11,15,12,15,239,1,16,1,16,1,16,1,17,1,17,1,17,5,17,248,
        8,17,10,17,12,17,251,9,17,1,18,1,18,1,18,4,18,256,8,18,11,18,12,
        18,257,1,19,1,19,1,19,5,19,263,8,19,10,19,12,19,266,9,19,1,20,1,
        20,1,20,3,20,271,8,20,1,21,1,21,1,21,4,21,276,8,21,11,21,12,21,277,
        1,22,1,22,4,22,282,8,22,11,22,12,22,283,1,22,1,22,1,22,3,22,289,
        8,22,1,22,1,22,4,22,293,8,22,11,22,12,22,294,1,23,5,23,298,8,23,
        10,23,12,23,301,9,23,1,23,1,23,4,23,305,8,23,11,23,12,23,306,1,23,
        1,23,4,23,311,8,23,11,23,12,23,312,3,23,315,8,23,1,24,1,24,1,24,
        1,24,4,24,321,8,24,11,24,12,24,322,1,25,1,25,1,25,1,25,1,26,1,26,
        4,26,331,8,26,11,26,12,26,332,1,26,1,26,1,27,1,27,1,28,1,28,1,29,
        1,29,4,29,343,8,29,11,29,12,29,344,1,29,1,29,1,29,1,29,4,29,351,
        8,29,11,29,12,29,352,1,29,1,29,1,29,4,29,358,8,29,11,29,12,29,359,
        1,30,1,30,1,31,1,31,4,31,366,8,31,11,31,12,31,367,1,31,1,31,1,31,
        1,31,4,31,374,8,31,11,31,12,31,375,1,32,1,32,1,32,1,32,1,33,1,33,
        1,33,4,33,385,8,33,11,33,12,33,386,1,34,1,34,3,34,391,8,34,1,34,
        4,34,394,8,34,11,34,12,34,395,1,35,1,35,1,35,1,35,1,35,4,35,403,
        8,35,11,35,12,35,404,1,36,1,36,3,36,409,8,36,1,37,1,37,1,37,1,37,
        1,37,3,37,416,8,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,5,39,425,8,
        39,10,39,12,39,428,9,39,1,40,3,40,431,8,40,1,40,1,40,1,41,1,41,1,
        41,1,42,1,42,1,42,3,42,441,8,42,1,43,1,43,1,44,1,44,1,44,1,44,1,
        45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,
        51,1,51,0,0,52,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,92,94,96,98,100,102,0,5,2,0,30,30,32,32,1,0,28,
        29,1,0,24,25,1,0,38,40,2,0,1,25,37,37,474,0,107,1,0,0,0,2,133,1,
        0,0,0,4,135,1,0,0,0,6,142,1,0,0,0,8,149,1,0,0,0,10,156,1,0,0,0,12,
        166,1,0,0,0,14,186,1,0,0,0,16,188,1,0,0,0,18,201,1,0,0,0,20,203,
        1,0,0,0,22,216,1,0,0,0,24,218,1,0,0,0,26,220,1,0,0,0,28,226,1,0,
        0,0,30,232,1,0,0,0,32,241,1,0,0,0,34,244,1,0,0,0,36,252,1,0,0,0,
        38,259,1,0,0,0,40,270,1,0,0,0,42,272,1,0,0,0,44,279,1,0,0,0,46,299,
        1,0,0,0,48,316,1,0,0,0,50,324,1,0,0,0,52,328,1,0,0,0,54,336,1,0,
        0,0,56,338,1,0,0,0,58,340,1,0,0,0,60,361,1,0,0,0,62,363,1,0,0,0,
        64,377,1,0,0,0,66,381,1,0,0,0,68,388,1,0,0,0,70,397,1,0,0,0,72,408,
        1,0,0,0,74,415,1,0,0,0,76,417,1,0,0,0,78,422,1,0,0,0,80,430,1,0,
        0,0,82,434,1,0,0,0,84,440,1,0,0,0,86,442,1,0,0,0,88,444,1,0,0,0,
        90,448,1,0,0,0,92,450,1,0,0,0,94,452,1,0,0,0,96,454,1,0,0,0,98,456,
        1,0,0,0,100,458,1,0,0,0,102,460,1,0,0,0,104,106,5,43,0,0,105,104,
        1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,113,
        1,0,0,0,109,107,1,0,0,0,110,112,3,20,10,0,111,110,1,0,0,0,112,115,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,119,1,0,0,0,115,113,
        1,0,0,0,116,118,3,2,1,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,119,1,0,0,0,122,123,
        5,8,0,0,123,1,1,0,0,0,124,125,3,4,2,0,125,126,3,10,5,0,126,134,1,
        0,0,0,127,128,3,6,3,0,128,129,3,10,5,0,129,134,1,0,0,0,130,131,3,
        8,4,0,131,132,3,10,5,0,132,134,1,0,0,0,133,124,1,0,0,0,133,127,1,
        0,0,0,133,130,1,0,0,0,134,3,1,0,0,0,135,136,5,1,0,0,136,138,3,100,
        50,0,137,139,5,43,0,0,138,137,1,0,0,0,139,140,1,0,0,0,140,138,1,
        0,0,0,140,141,1,0,0,0,141,5,1,0,0,0,142,143,5,16,0,0,143,145,3,102,
        51,0,144,146,5,43,0,0,145,144,1,0,0,0,146,147,1,0,0,0,147,145,1,
        0,0,0,147,148,1,0,0,0,148,7,1,0,0,0,149,150,5,20,0,0,150,152,3,102,
        51,0,151,153,5,43,0,0,152,151,1,0,0,0,153,154,1,0,0,0,154,152,1,
        0,0,0,154,155,1,0,0,0,155,9,1,0,0,0,156,157,3,12,6,0,157,11,1,0,
        0,0,158,165,3,14,7,0,159,161,3,16,8,0,160,159,1,0,0,0,160,161,1,
        0,0,0,161,162,1,0,0,0,162,165,3,18,9,0,163,165,3,20,10,0,164,158,
        1,0,0,0,164,160,1,0,0,0,164,163,1,0,0,0,165,168,1,0,0,0,166,164,
        1,0,0,0,166,167,1,0,0,0,167,13,1,0,0,0,168,166,1,0,0,0,169,170,3,
        90,45,0,170,172,5,30,0,0,171,173,5,9,0,0,172,171,1,0,0,0,172,173,
        1,0,0,0,173,175,1,0,0,0,174,176,5,43,0,0,175,174,1,0,0,0,176,177,
        1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,187,1,0,0,0,179,180,
        3,90,45,0,180,182,5,32,0,0,181,183,5,43,0,0,182,181,1,0,0,0,183,
        184,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,
        169,1,0,0,0,186,179,1,0,0,0,187,15,1,0,0,0,188,189,3,90,45,0,189,
        190,7,0,0,0,190,17,1,0,0,0,191,202,3,26,13,0,192,202,3,28,14,0,193,
        202,3,30,15,0,194,202,3,36,18,0,195,202,3,42,21,0,196,202,3,44,22,
        0,197,202,3,58,29,0,198,202,3,62,31,0,199,202,3,64,32,0,200,202,
        3,70,35,0,201,191,1,0,0,0,201,192,1,0,0,0,201,193,1,0,0,0,201,194,
        1,0,0,0,201,195,1,0,0,0,201,196,1,0,0,0,201,197,1,0,0,0,201,198,
        1,0,0,0,201,199,1,0,0,0,201,200,1,0,0,0,202,19,1,0,0,0,203,204,5,
        35,0,0,204,205,3,22,11,0,205,207,3,24,12,0,206,208,5,37,0,0,207,
        206,1,0,0,0,207,208,1,0,0,0,208,210,1,0,0,0,209,211,5,43,0,0,210,
        209,1,0,0,0,211,212,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,
        214,1,0,0,0,214,215,6,10,-1,0,215,21,1,0,0,0,216,217,5,38,0,0,217,
        23,1,0,0,0,218,219,5,46,0,0,219,25,1,0,0,0,220,222,5,2,0,0,221,223,
        5,43,0,0,222,221,1,0,0,0,223,224,1,0,0,0,224,222,1,0,0,0,224,225,
        1,0,0,0,225,27,1,0,0,0,226,228,5,3,0,0,227,229,5,43,0,0,228,227,
        1,0,0,0,229,230,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,29,1,
        0,0,0,232,234,3,92,46,0,233,235,3,34,17,0,234,233,1,0,0,0,234,235,
        1,0,0,0,235,237,1,0,0,0,236,238,5,43,0,0,237,236,1,0,0,0,238,239,
        1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,31,1,0,0,0,241,242,3,
        90,45,0,242,243,7,0,0,0,243,33,1,0,0,0,244,249,3,74,37,0,245,246,
        5,27,0,0,246,248,3,74,37,0,247,245,1,0,0,0,248,251,1,0,0,0,249,247,
        1,0,0,0,249,250,1,0,0,0,250,35,1,0,0,0,251,249,1,0,0,0,252,253,5,
        4,0,0,253,255,3,38,19,0,254,256,5,43,0,0,255,254,1,0,0,0,256,257,
        1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,0,258,37,1,0,0,0,259,264,3,
        40,20,0,260,261,5,27,0,0,261,263,3,40,20,0,262,260,1,0,0,0,263,266,
        1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,39,1,0,0,0,266,264,1,
        0,0,0,267,271,3,94,47,0,268,271,3,78,39,0,269,271,3,76,38,0,270,
        267,1,0,0,0,270,268,1,0,0,0,270,269,1,0,0,0,271,41,1,0,0,0,272,273,
        5,6,0,0,273,275,3,100,50,0,274,276,5,43,0,0,275,274,1,0,0,0,276,
        277,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,43,1,0,0,0,279,281,
        5,12,0,0,280,282,5,43,0,0,281,280,1,0,0,0,282,283,1,0,0,0,283,281,
        1,0,0,0,283,284,1,0,0,0,284,285,1,0,0,0,285,286,3,46,23,0,286,288,
        3,12,6,0,287,289,3,52,26,0,288,287,1,0,0,0,288,289,1,0,0,0,289,290,
        1,0,0,0,290,292,5,10,0,0,291,293,5,43,0,0,292,291,1,0,0,0,293,294,
        1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,45,1,0,0,0,296,298,3,
        48,24,0,297,296,1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,
        1,0,0,0,300,302,1,0,0,0,301,299,1,0,0,0,302,304,3,50,25,0,303,305,
        5,43,0,0,304,303,1,0,0,0,305,306,1,0,0,0,306,304,1,0,0,0,306,307,
        1,0,0,0,307,314,1,0,0,0,308,310,5,19,0,0,309,311,5,43,0,0,310,309,
        1,0,0,0,311,312,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,315,
        1,0,0,0,314,308,1,0,0,0,314,315,1,0,0,0,315,47,1,0,0,0,316,317,3,
        50,25,0,317,318,5,27,0,0,318,320,3,56,28,0,319,321,5,43,0,0,320,
        319,1,0,0,0,321,322,1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,323,
        49,1,0,0,0,324,325,3,12,6,0,325,326,5,13,0,0,326,327,3,54,27,0,327,
        51,1,0,0,0,328,330,5,7,0,0,329,331,5,43,0,0,330,329,1,0,0,0,331,
        332,1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,334,1,0,0,0,334,
        335,3,12,6,0,335,53,1,0,0,0,336,337,5,37,0,0,337,55,1,0,0,0,338,
        339,5,37,0,0,339,57,1,0,0,0,340,342,5,23,0,0,341,343,5,43,0,0,342,
        341,1,0,0,0,343,344,1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,
        346,1,0,0,0,346,347,3,60,30,0,347,348,5,18,0,0,348,350,3,54,27,0,
        349,351,5,43,0,0,350,349,1,0,0,0,351,352,1,0,0,0,352,350,1,0,0,0,
        352,353,1,0,0,0,353,354,1,0,0,0,354,355,3,12,6,0,355,357,5,22,0,
        0,356,358,5,43,0,0,357,356,1,0,0,0,358,359,1,0,0,0,359,357,1,0,0,
        0,359,360,1,0,0,0,360,59,1,0,0,0,361,362,3,12,6,0,362,61,1,0,0,0,
        363,365,5,5,0,0,364,366,5,43,0,0,365,364,1,0,0,0,366,367,1,0,0,0,
        367,365,1,0,0,0,367,368,1,0,0,0,368,369,1,0,0,0,369,370,3,12,6,0,
        370,371,5,21,0,0,371,373,3,54,27,0,372,374,5,43,0,0,373,372,1,0,
        0,0,374,375,1,0,0,0,375,373,1,0,0,0,375,376,1,0,0,0,376,63,1,0,0,
        0,377,378,3,66,33,0,378,379,3,12,6,0,379,380,3,68,34,0,380,65,1,
        0,0,0,381,382,5,17,0,0,382,384,3,96,48,0,383,385,5,43,0,0,384,383,
        1,0,0,0,385,386,1,0,0,0,386,384,1,0,0,0,386,387,1,0,0,0,387,67,1,
        0,0,0,388,390,5,15,0,0,389,391,3,96,48,0,390,389,1,0,0,0,390,391,
        1,0,0,0,391,393,1,0,0,0,392,394,5,43,0,0,393,392,1,0,0,0,394,395,
        1,0,0,0,395,393,1,0,0,0,395,396,1,0,0,0,396,69,1,0,0,0,397,398,5,
        11,0,0,398,399,3,54,27,0,399,400,5,27,0,0,400,402,3,72,36,0,401,
        403,5,43,0,0,402,401,1,0,0,0,403,404,1,0,0,0,404,402,1,0,0,0,404,
        405,1,0,0,0,405,71,1,0,0,0,406,409,3,78,39,0,407,409,3,76,38,0,408,
        406,1,0,0,0,408,407,1,0,0,0,409,73,1,0,0,0,410,416,3,98,49,0,411,
        416,3,94,47,0,412,416,3,96,48,0,413,416,3,78,39,0,414,416,3,76,38,
        0,415,410,1,0,0,0,415,411,1,0,0,0,415,412,1,0,0,0,415,413,1,0,0,
        0,415,414,1,0,0,0,416,75,1,0,0,0,417,418,3,86,43,0,418,419,5,33,
        0,0,419,420,3,78,39,0,420,421,5,34,0,0,421,77,1,0,0,0,422,426,3,
        80,40,0,423,425,3,82,41,0,424,423,1,0,0,0,425,428,1,0,0,0,426,424,
        1,0,0,0,426,427,1,0,0,0,427,79,1,0,0,0,428,426,1,0,0,0,429,431,7,
        1,0,0,430,429,1,0,0,0,430,431,1,0,0,0,431,432,1,0,0,0,432,433,3,
        84,42,0,433,81,1,0,0,0,434,435,7,1,0,0,435,436,3,84,42,0,436,83,
        1,0,0,0,437,441,3,100,50,0,438,441,3,88,44,0,439,441,3,90,45,0,440,
        437,1,0,0,0,440,438,1,0,0,0,440,439,1,0,0,0,441,85,1,0,0,0,442,443,
        7,2,0,0,443,87,1,0,0,0,444,445,3,102,51,0,445,446,5,26,0,0,446,447,
        3,102,51,0,447,89,1,0,0,0,448,449,3,102,51,0,449,91,1,0,0,0,450,
        451,5,37,0,0,451,93,1,0,0,0,452,453,5,41,0,0,453,95,1,0,0,0,454,
        455,5,36,0,0,455,97,1,0,0,0,456,457,5,42,0,0,457,99,1,0,0,0,458,
        459,7,3,0,0,459,101,1,0,0,0,460,461,7,4,0,0,461,103,1,0,0,0,49,107,
        113,119,133,140,147,154,160,164,166,172,177,184,186,201,207,212,
        224,230,234,239,249,257,264,270,277,283,288,294,299,306,312,314,
        322,332,344,352,359,367,375,386,390,395,404,408,415,426,430,440
    ]

class AsmParser ( Parser ):

    grammarFileName = "AsmParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'asect'", "'break'", "'continue'", "'dc'", 
                     "'do'", "'ds'", "'else'", "'end'", "'ext'", "'fi'", 
                     "'goto'", "'if'", "'is'", "'macro'", "'restore'", "'rsect'", 
                     "'save'", "'stays'", "'then'", "'tplate'", "'until'", 
                     "'wend'", "'while'", "'low'", "'high'", "'.'", "','", 
                     "'+'", "'-'", "':'", "'*'", "'>'", "'('", "')'", "'-|'" ]

    symbolicNames = [ "<INVALID>", "Asect", "Break", "Continue", "Dc", "Do", 
                      "Ds", "Else", "End", "Ext", "Fi", "Goto", "If", "Is", 
                      "Macro", "Restore", "Rsect", "Save", "Stays", "Then", 
                      "Tplate", "Until", "Wend", "While", "Low", "High", 
                      "DOT", "COMMA", "PLUS", "MINUS", "COLON", "ASTERISK", 
                      "ANGLE_BRACKET", "OPEN_PAREN", "CLOSE_PAREN", "LINE_MARK_MARKER", 
                      "REGISTER", "WORD", "DECIMAL_NUMBER", "BINARY_NUMBER", 
                      "HEX_NUMBER", "STRING", "CHAR", "NEWLINE", "COMMENT", 
                      "WS", "BASE64", "UNEXPECTED_TOKEN" ]

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
    RULE_define_constant = 18
    RULE_dc_arguments = 19
    RULE_dc_argument = 20
    RULE_declare_space = 21
    RULE_conditional = 22
    RULE_conditions = 23
    RULE_connective_condition = 24
    RULE_condition = 25
    RULE_else_clause = 26
    RULE_branch_mnemonic = 27
    RULE_conjunction = 28
    RULE_while_loop = 29
    RULE_while_condition = 30
    RULE_until_loop = 31
    RULE_save_restore_statement = 32
    RULE_save_statement = 33
    RULE_restore_statement = 34
    RULE_goto_statement = 35
    RULE_goto_argument = 36
    RULE_argument = 37
    RULE_byte_expr = 38
    RULE_addr_expr = 39
    RULE_first_term = 40
    RULE_add_term = 41
    RULE_term = 42
    RULE_byte_specifier = 43
    RULE_template_field = 44
    RULE_label = 45
    RULE_instruction = 46
    RULE_string = 47
    RULE_register = 48
    RULE_character = 49
    RULE_number = 50
    RULE_name = 51

    ruleNames =  [ "program", "section", "asect_header", "rsect_header", 
                   "tplate_header", "section_body", "code_block", "standalone_label", 
                   "line_label", "statement", "line_mark", "line_number", 
                   "filepath", "break_statement", "continue_statement", 
                   "instruction_line", "label_declaration", "arguments", 
                   "define_constant", "dc_arguments", "dc_argument", "declare_space", 
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
    Dc=4
    Do=5
    Ds=6
    Else=7
    End=8
    Ext=9
    Fi=10
    Goto=11
    If=12
    Is=13
    Macro=14
    Restore=15
    Rsect=16
    Save=17
    Stays=18
    Then=19
    Tplate=20
    Until=21
    Wend=22
    While=23
    Low=24
    High=25
    DOT=26
    COMMA=27
    PLUS=28
    MINUS=29
    COLON=30
    ASTERISK=31
    ANGLE_BRACKET=32
    OPEN_PAREN=33
    CLOSE_PAREN=34
    LINE_MARK_MARKER=35
    REGISTER=36
    WORD=37
    DECIMAL_NUMBER=38
    BINARY_NUMBER=39
    HEX_NUMBER=40
    STRING=41
    CHAR=42
    NEWLINE=43
    COMMENT=44
    WS=45
    BASE64=46
    UNEXPECTED_TOKEN=47

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
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.NEWLINE:
                self.state = 104
                self.match(AsmParser.NEWLINE)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.LINE_MARK_MARKER:
                self.state = 110
                self.line_mark()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Rsect) | (1 << AsmParser.Tplate))) != 0):
                self.state = 116
                self.section()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
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
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmParser.Asect]:
                localctx = AsmParser.AbsoluteSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.asect_header()
                self.state = 125
                self.section_body()
                pass
            elif token in [AsmParser.Rsect]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.rsect_header()
                self.state = 128
                self.section_body()
                pass
            elif token in [AsmParser.Tplate]:
                localctx = AsmParser.TemplateSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.tplate_header()
                self.state = 131
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
            self.state = 135
            self.match(AsmParser.Asect)
            self.state = 136
            self.number()
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.match(AsmParser.NEWLINE)
                self.state = 140 
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
            self.state = 142
            self.match(AsmParser.Rsect)
            self.state = 143
            self.name()
            self.state = 145 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 144
                self.match(AsmParser.NEWLINE)
                self.state = 147 
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
            self.state = 149
            self.match(AsmParser.Tplate)
            self.state = 150
            self.name()
            self.state = 152 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 151
                self.match(AsmParser.NEWLINE)
                self.state = 154 
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
            self.state = 156
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
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 164
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        self.state = 158
                        self.standalone_label()
                        pass

                    elif la_ == 2:
                        self.state = 160
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                        if la_ == 1:
                            self.state = 159
                            self.line_label()


                        self.state = 162
                        self.statement()
                        pass

                    elif la_ == 3:
                        self.state = 163
                        self.line_mark()
                        pass

             
                self.state = 168
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.label()
                self.state = 170
                self.match(AsmParser.COLON)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==AsmParser.Ext:
                    self.state = 171
                    self.match(AsmParser.Ext)


                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 174
                    self.match(AsmParser.NEWLINE)
                    self.state = 177 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==AsmParser.NEWLINE):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.label()
                self.state = 180
                self.match(AsmParser.ANGLE_BRACKET)
                self.state = 182 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 181
                    self.match(AsmParser.NEWLINE)
                    self.state = 184 
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
            self.state = 188
            self.label()
            self.state = 189
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


        def define_constant(self):
            return self.getTypedRuleContext(AsmParser.Define_constantContext,0)


        def declare_space(self):
            return self.getTypedRuleContext(AsmParser.Declare_spaceContext,0)


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
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmParser.Break]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.break_statement()
                pass
            elif token in [AsmParser.Continue]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.continue_statement()
                pass
            elif token in [AsmParser.WORD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.instruction_line()
                pass
            elif token in [AsmParser.Dc]:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.define_constant()
                pass
            elif token in [AsmParser.Ds]:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.declare_space()
                pass
            elif token in [AsmParser.If]:
                self.enterOuterAlt(localctx, 6)
                self.state = 196
                self.conditional()
                pass
            elif token in [AsmParser.While]:
                self.enterOuterAlt(localctx, 7)
                self.state = 197
                self.while_loop()
                pass
            elif token in [AsmParser.Do]:
                self.enterOuterAlt(localctx, 8)
                self.state = 198
                self.until_loop()
                pass
            elif token in [AsmParser.Save]:
                self.enterOuterAlt(localctx, 9)
                self.state = 199
                self.save_restore_statement()
                pass
            elif token in [AsmParser.Goto]:
                self.enterOuterAlt(localctx, 10)
                self.state = 200
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
            self.state = 203
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 204
            localctx._line_number = self.line_number()
            self.state = 205
            localctx._filepath = self.filepath()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.WORD:
                self.state = 206
                self.match(AsmParser.WORD)


            self.state = 210 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 209
                self.match(AsmParser.NEWLINE)
                self.state = 212 
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
            self.state = 216
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
            self.state = 218
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
            self.state = 220
            self.match(AsmParser.Break)
            self.state = 222 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 221
                self.match(AsmParser.NEWLINE)
                self.state = 224 
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
            self.state = 226
            self.match(AsmParser.Continue)
            self.state = 228 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 227
                self.match(AsmParser.NEWLINE)
                self.state = 230 
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
            self.state = 232
            self.instruction()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Break) | (1 << AsmParser.Continue) | (1 << AsmParser.Dc) | (1 << AsmParser.Do) | (1 << AsmParser.Ds) | (1 << AsmParser.Else) | (1 << AsmParser.End) | (1 << AsmParser.Ext) | (1 << AsmParser.Fi) | (1 << AsmParser.Goto) | (1 << AsmParser.If) | (1 << AsmParser.Is) | (1 << AsmParser.Macro) | (1 << AsmParser.Restore) | (1 << AsmParser.Rsect) | (1 << AsmParser.Save) | (1 << AsmParser.Stays) | (1 << AsmParser.Then) | (1 << AsmParser.Tplate) | (1 << AsmParser.Until) | (1 << AsmParser.Wend) | (1 << AsmParser.While) | (1 << AsmParser.Low) | (1 << AsmParser.High) | (1 << AsmParser.PLUS) | (1 << AsmParser.MINUS) | (1 << AsmParser.REGISTER) | (1 << AsmParser.WORD) | (1 << AsmParser.DECIMAL_NUMBER) | (1 << AsmParser.BINARY_NUMBER) | (1 << AsmParser.HEX_NUMBER) | (1 << AsmParser.STRING) | (1 << AsmParser.CHAR))) != 0):
                self.state = 233
                self.arguments()


            self.state = 237 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 236
                self.match(AsmParser.NEWLINE)
                self.state = 239 
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
            self.state = 241
            self.label()
            self.state = 242
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
            self.state = 244
            self.argument()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.COMMA:
                self.state = 245
                self.match(AsmParser.COMMA)
                self.state = 246
                self.argument()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_constantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Dc(self):
            return self.getToken(AsmParser.Dc, 0)

        def dc_arguments(self):
            return self.getTypedRuleContext(AsmParser.Dc_argumentsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_define_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_constant" ):
                listener.enterDefine_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_constant" ):
                listener.exitDefine_constant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_constant" ):
                return visitor.visitDefine_constant(self)
            else:
                return visitor.visitChildren(self)




    def define_constant(self):

        localctx = AsmParser.Define_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_define_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(AsmParser.Dc)
            self.state = 253
            self.dc_arguments()
            self.state = 255 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 254
                self.match(AsmParser.NEWLINE)
                self.state = 257 
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


    class Dc_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dc_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Dc_argumentContext)
            else:
                return self.getTypedRuleContext(AsmParser.Dc_argumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.COMMA)
            else:
                return self.getToken(AsmParser.COMMA, i)

        def getRuleIndex(self):
            return AsmParser.RULE_dc_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDc_arguments" ):
                listener.enterDc_arguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDc_arguments" ):
                listener.exitDc_arguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDc_arguments" ):
                return visitor.visitDc_arguments(self)
            else:
                return visitor.visitChildren(self)




    def dc_arguments(self):

        localctx = AsmParser.Dc_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dc_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.dc_argument()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.COMMA:
                self.state = 260
                self.match(AsmParser.COMMA)
                self.state = 261
                self.dc_argument()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dc_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(AsmParser.StringContext,0)


        def addr_expr(self):
            return self.getTypedRuleContext(AsmParser.Addr_exprContext,0)


        def byte_expr(self):
            return self.getTypedRuleContext(AsmParser.Byte_exprContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_dc_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDc_argument" ):
                listener.enterDc_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDc_argument" ):
                listener.exitDc_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDc_argument" ):
                return visitor.visitDc_argument(self)
            else:
                return visitor.visitChildren(self)




    def dc_argument(self):

        localctx = AsmParser.Dc_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dc_argument)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.addr_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.byte_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_spaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ds(self):
            return self.getToken(AsmParser.Ds, 0)

        def number(self):
            return self.getTypedRuleContext(AsmParser.NumberContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_declare_space

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_space" ):
                listener.enterDeclare_space(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_space" ):
                listener.exitDeclare_space(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_space" ):
                return visitor.visitDeclare_space(self)
            else:
                return visitor.visitChildren(self)




    def declare_space(self):

        localctx = AsmParser.Declare_spaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_declare_space)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(AsmParser.Ds)
            self.state = 273
            self.number()
            self.state = 275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 274
                self.match(AsmParser.NEWLINE)
                self.state = 277 
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
        self.enterRule(localctx, 44, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(AsmParser.If)
            self.state = 281 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 280
                self.match(AsmParser.NEWLINE)
                self.state = 283 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 285
            self.conditions()
            self.state = 286
            self.code_block()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.Else:
                self.state = 287
                self.else_clause()


            self.state = 290
            self.match(AsmParser.Fi)
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
        self.enterRule(localctx, 46, self.RULE_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 296
                    self.connective_condition() 
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 302
            self.condition()
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

            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 308
                self.match(AsmParser.Then)
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
        self.enterRule(localctx, 48, self.RULE_connective_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.condition()
            self.state = 317
            self.match(AsmParser.COMMA)
            self.state = 318
            self.conjunction()
            self.state = 320 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 319
                self.match(AsmParser.NEWLINE)
                self.state = 322 
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
        self.enterRule(localctx, 50, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.code_block()
            self.state = 325
            self.match(AsmParser.Is)
            self.state = 326
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
        self.enterRule(localctx, 52, self.RULE_else_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(AsmParser.Else)
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

            self.state = 334
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
        self.enterRule(localctx, 54, self.RULE_branch_mnemonic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
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
        self.enterRule(localctx, 56, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
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
        self.enterRule(localctx, 58, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(AsmParser.While)
            self.state = 342 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 341
                self.match(AsmParser.NEWLINE)
                self.state = 344 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 346
            self.while_condition()
            self.state = 347
            self.match(AsmParser.Stays)
            self.state = 348
            self.branch_mnemonic()
            self.state = 350 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 349
                self.match(AsmParser.NEWLINE)
                self.state = 352 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 354
            self.code_block()
            self.state = 355
            self.match(AsmParser.Wend)
            self.state = 357 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 356
                self.match(AsmParser.NEWLINE)
                self.state = 359 
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
        self.enterRule(localctx, 60, self.RULE_while_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
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
        self.enterRule(localctx, 62, self.RULE_until_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(AsmParser.Do)
            self.state = 365 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 364
                self.match(AsmParser.NEWLINE)
                self.state = 367 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 369
            self.code_block()
            self.state = 370
            self.match(AsmParser.Until)
            self.state = 371
            self.branch_mnemonic()
            self.state = 373 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 372
                self.match(AsmParser.NEWLINE)
                self.state = 375 
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
        self.enterRule(localctx, 64, self.RULE_save_restore_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.save_statement()
            self.state = 378
            self.code_block()
            self.state = 379
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
        self.enterRule(localctx, 66, self.RULE_save_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(AsmParser.Save)
            self.state = 382
            self.register()
            self.state = 384 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 383
                self.match(AsmParser.NEWLINE)
                self.state = 386 
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
        self.enterRule(localctx, 68, self.RULE_restore_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(AsmParser.Restore)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.REGISTER:
                self.state = 389
                self.register()


            self.state = 393 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 392
                self.match(AsmParser.NEWLINE)
                self.state = 395 
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
        self.enterRule(localctx, 70, self.RULE_goto_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(AsmParser.Goto)
            self.state = 398
            self.branch_mnemonic()
            self.state = 399
            self.match(AsmParser.COMMA)
            self.state = 400
            self.goto_argument()
            self.state = 402 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 401
                self.match(AsmParser.NEWLINE)
                self.state = 404 
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
        self.enterRule(localctx, 72, self.RULE_goto_argument)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.addr_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
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
        self.enterRule(localctx, 74, self.RULE_argument)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.character()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 412
                self.register()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 413
                self.addr_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 414
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
        self.enterRule(localctx, 76, self.RULE_byte_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.byte_specifier()
            self.state = 418
            self.match(AsmParser.OPEN_PAREN)
            self.state = 419
            self.addr_expr()
            self.state = 420
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
        self.enterRule(localctx, 78, self.RULE_addr_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.first_term()
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.PLUS or _la==AsmParser.MINUS:
                self.state = 423
                self.add_term()
                self.state = 428
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
        self.enterRule(localctx, 80, self.RULE_first_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.PLUS or _la==AsmParser.MINUS:
                self.state = 429
                _la = self._input.LA(1)
                if not(_la==AsmParser.PLUS or _la==AsmParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 432
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
        self.enterRule(localctx, 82, self.RULE_add_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            _la = self._input.LA(1)
            if not(_la==AsmParser.PLUS or _la==AsmParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 435
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
        self.enterRule(localctx, 84, self.RULE_term)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.template_field()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
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
        self.enterRule(localctx, 86, self.RULE_byte_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
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
        self.enterRule(localctx, 88, self.RULE_template_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.name()
            self.state = 445
            self.match(AsmParser.DOT)
            self.state = 446
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
        self.enterRule(localctx, 90, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
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
        self.enterRule(localctx, 92, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
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
        self.enterRule(localctx, 94, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
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
        self.enterRule(localctx, 96, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
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
        self.enterRule(localctx, 98, self.RULE_character)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
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
        self.enterRule(localctx, 100, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
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

        def Dc(self):
            return self.getToken(AsmParser.Dc, 0)

        def Do(self):
            return self.getToken(AsmParser.Do, 0)

        def Ds(self):
            return self.getToken(AsmParser.Ds, 0)

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
        self.enterRule(localctx, 102, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Break) | (1 << AsmParser.Continue) | (1 << AsmParser.Dc) | (1 << AsmParser.Do) | (1 << AsmParser.Ds) | (1 << AsmParser.Else) | (1 << AsmParser.End) | (1 << AsmParser.Ext) | (1 << AsmParser.Fi) | (1 << AsmParser.Goto) | (1 << AsmParser.If) | (1 << AsmParser.Is) | (1 << AsmParser.Macro) | (1 << AsmParser.Restore) | (1 << AsmParser.Rsect) | (1 << AsmParser.Save) | (1 << AsmParser.Stays) | (1 << AsmParser.Then) | (1 << AsmParser.Tplate) | (1 << AsmParser.Until) | (1 << AsmParser.Wend) | (1 << AsmParser.While) | (1 << AsmParser.Low) | (1 << AsmParser.High) | (1 << AsmParser.WORD))) != 0)):
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





