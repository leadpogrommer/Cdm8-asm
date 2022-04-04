# Generated from /home/ilya/work/cdm8e/ORiGinalASM/assembler/AsmLexer.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&")
        buf.write("\u0111\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\7\35\u00c7\n\35\f\35\16\35\u00ca\13\35")
        buf.write("\3\36\6\36\u00cd\n\36\r\36\16\36\u00ce\3\37\3\37\3\37")
        buf.write("\3\37\6\37\u00d5\n\37\r\37\16\37\u00d6\3 \3 \3 \3 \6 ")
        buf.write("\u00dd\n \r \16 \u00de\3!\3!\7!\u00e3\n!\f!\16!\u00e6")
        buf.write("\13!\3!\3!\3!\3!\7!\u00ec\n!\f!\16!\u00ef\13!\7!\u00f1")
        buf.write("\n!\f!\16!\u00f4\13!\3!\3!\3\"\3\"\3\"\3\"\5\"\u00fc\n")
        buf.write("\"\3\"\3\"\3#\5#\u0101\n#\3#\3#\3$\3$\7$\u0107\n$\f$\16")
        buf.write("$\u010a\13$\3$\3$\3%\3%\3%\3%\2\2&\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&\3\2\f\3\2\62\65\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\3\2\62;\3\2\62\63\5\2\62;CHch\5\2\f")
        buf.write("\f$$^^\5\2\f\f))^^\3\2\f\f\4\2\13\13\"\"\2\u011a\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\3K")
        buf.write("\3\2\2\2\5Q\3\2\2\2\7W\3\2\2\2\t`\3\2\2\2\13c\3\2\2\2")
        buf.write("\rh\3\2\2\2\17l\3\2\2\2\21p\3\2\2\2\23s\3\2\2\2\25v\3")
        buf.write("\2\2\2\27y\3\2\2\2\31\177\3\2\2\2\33\u0087\3\2\2\2\35")
        buf.write("\u008d\3\2\2\2\37\u0092\3\2\2\2!\u0098\3\2\2\2#\u009d")
        buf.write("\3\2\2\2%\u00a4\3\2\2\2\'\u00aa\3\2\2\2)\u00af\3\2\2\2")
        buf.write("+\u00b5\3\2\2\2-\u00b7\3\2\2\2/\u00b9\3\2\2\2\61\u00bb")
        buf.write("\3\2\2\2\63\u00bd\3\2\2\2\65\u00bf\3\2\2\2\67\u00c1\3")
        buf.write("\2\2\29\u00c4\3\2\2\2;\u00cc\3\2\2\2=\u00d0\3\2\2\2?\u00d8")
        buf.write("\3\2\2\2A\u00e0\3\2\2\2C\u00f7\3\2\2\2E\u0100\3\2\2\2")
        buf.write("G\u0104\3\2\2\2I\u010d\3\2\2\2KL\7c\2\2LM\7u\2\2MN\7g")
        buf.write("\2\2NO\7e\2\2OP\7v\2\2P\4\3\2\2\2QR\7d\2\2RS\7t\2\2ST")
        buf.write("\7g\2\2TU\7c\2\2UV\7m\2\2V\6\3\2\2\2WX\7e\2\2XY\7q\2\2")
        buf.write("YZ\7p\2\2Z[\7v\2\2[\\\7k\2\2\\]\7p\2\2]^\7w\2\2^_\7g\2")
        buf.write("\2_\b\3\2\2\2`a\7f\2\2ab\7q\2\2b\n\3\2\2\2cd\7g\2\2de")
        buf.write("\7n\2\2ef\7u\2\2fg\7g\2\2g\f\3\2\2\2hi\7g\2\2ij\7p\2\2")
        buf.write("jk\7f\2\2k\16\3\2\2\2lm\7g\2\2mn\7z\2\2no\7v\2\2o\20\3")
        buf.write("\2\2\2pq\7h\2\2qr\7k\2\2r\22\3\2\2\2st\7k\2\2tu\7h\2\2")
        buf.write("u\24\3\2\2\2vw\7k\2\2wx\7u\2\2x\26\3\2\2\2yz\7o\2\2z{")
        buf.write("\7c\2\2{|\7e\2\2|}\7t\2\2}~\7q\2\2~\30\3\2\2\2\177\u0080")
        buf.write("\7t\2\2\u0080\u0081\7g\2\2\u0081\u0082\7u\2\2\u0082\u0083")
        buf.write("\7v\2\2\u0083\u0084\7q\2\2\u0084\u0085\7t\2\2\u0085\u0086")
        buf.write("\7g\2\2\u0086\32\3\2\2\2\u0087\u0088\7t\2\2\u0088\u0089")
        buf.write("\7u\2\2\u0089\u008a\7g\2\2\u008a\u008b\7e\2\2\u008b\u008c")
        buf.write("\7v\2\2\u008c\34\3\2\2\2\u008d\u008e\7u\2\2\u008e\u008f")
        buf.write("\7c\2\2\u008f\u0090\7x\2\2\u0090\u0091\7g\2\2\u0091\36")
        buf.write("\3\2\2\2\u0092\u0093\7u\2\2\u0093\u0094\7v\2\2\u0094\u0095")
        buf.write("\7c\2\2\u0095\u0096\7{\2\2\u0096\u0097\7u\2\2\u0097 \3")
        buf.write("\2\2\2\u0098\u0099\7v\2\2\u0099\u009a\7j\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7p\2\2\u009c\"\3\2\2\2\u009d\u009e")
        buf.write("\7v\2\2\u009e\u009f\7r\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1")
        buf.write("\7c\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3\7g\2\2\u00a3$\3")
        buf.write("\2\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7n\2\2\u00a9&\3")
        buf.write("\2\2\2\u00aa\u00ab\7y\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7f\2\2\u00ae(\3\2\2\2\u00af\u00b0")
        buf.write("\7y\2\2\u00b0\u00b1\7j\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7g\2\2\u00b4*\3\2\2\2\u00b5\u00b6")
        buf.write("\7\60\2\2\u00b6,\3\2\2\2\u00b7\u00b8\7.\2\2\u00b8.\3\2")
        buf.write("\2\2\u00b9\u00ba\7/\2\2\u00ba\60\3\2\2\2\u00bb\u00bc\7")
        buf.write("<\2\2\u00bc\62\3\2\2\2\u00bd\u00be\7,\2\2\u00be\64\3\2")
        buf.write("\2\2\u00bf\u00c0\7@\2\2\u00c0\66\3\2\2\2\u00c1\u00c2\7")
        buf.write("t\2\2\u00c2\u00c3\t\2\2\2\u00c38\3\2\2\2\u00c4\u00c8\t")
        buf.write("\3\2\2\u00c5\u00c7\t\4\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00ca")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write(":\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cd\t\5\2\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf<\3\2\2\2\u00d0\u00d1\7\62\2")
        buf.write("\2\u00d1\u00d2\7d\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00d5")
        buf.write("\t\6\2\2\u00d4\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7>\3\2\2\2\u00d8")
        buf.write("\u00d9\7\62\2\2\u00d9\u00da\7z\2\2\u00da\u00dc\3\2\2\2")
        buf.write("\u00db\u00dd\t\7\2\2\u00dc\u00db\3\2\2\2\u00dd\u00de\3")
        buf.write("\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df@")
        buf.write("\3\2\2\2\u00e0\u00e4\7$\2\2\u00e1\u00e3\n\b\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\u00f2\3\2\2\2\u00e6\u00e4\3")
        buf.write("\2\2\2\u00e7\u00e8\7^\2\2\u00e8\u00e9\13\2\2\2\u00e9\u00ed")
        buf.write("\3\2\2\2\u00ea\u00ec\n\b\2\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00e7\3")
        buf.write("\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3")
        buf.write("\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5")
        buf.write("\u00f6\7$\2\2\u00f6B\3\2\2\2\u00f7\u00fb\7)\2\2\u00f8")
        buf.write("\u00f9\7^\2\2\u00f9\u00fc\13\2\2\2\u00fa\u00fc\n\t\2\2")
        buf.write("\u00fb\u00f8\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\u00fe\7)\2\2\u00feD\3\2\2\2\u00ff\u0101\7")
        buf.write("\17\2\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0103\7\f\2\2\u0103F\3\2\2\2\u0104")
        buf.write("\u0108\7%\2\2\u0105\u0107\n\n\2\2\u0106\u0105\3\2\2\2")
        buf.write("\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3")
        buf.write("\2\2\2\u0109\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c")
        buf.write("\b$\2\2\u010cH\3\2\2\2\u010d\u010e\t\13\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f\u0110\b%\2\2\u0110J\3\2\2\2\r\2\u00c8\u00ce")
        buf.write("\u00d6\u00de\u00e4\u00ed\u00f2\u00fb\u0100\u0108\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class AsmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Asect = 1
    Break = 2
    Continue = 3
    Do = 4
    Else = 5
    End = 6
    Ext = 7
    Fi = 8
    If = 9
    Is = 10
    Macro = 11
    Restore = 12
    Rsect = 13
    Save = 14
    Stays = 15
    Then = 16
    Tplate = 17
    Until = 18
    Wend = 19
    While = 20
    DOT = 21
    COMMA = 22
    MINUS = 23
    COLON = 24
    ASTERISK = 25
    ANGLE_BRACKET = 26
    REGISTER = 27
    WORD = 28
    DECIMAL_NUMBER = 29
    BINARY_NUMBER = 30
    HEX_NUMBER = 31
    STRING = 32
    CHAR = 33
    NEWLINE = 34
    COMMENT = 35
    WS = 36

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'asect'", "'break'", "'continue'", "'do'", "'else'", "'end'", 
            "'ext'", "'fi'", "'if'", "'is'", "'macro'", "'restore'", "'rsect'", 
            "'save'", "'stays'", "'then'", "'tplate'", "'until'", "'wend'", 
            "'while'", "'.'", "','", "'-'", "':'", "'*'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "Asect", "Break", "Continue", "Do", "Else", "End", "Ext", "Fi", 
            "If", "Is", "Macro", "Restore", "Rsect", "Save", "Stays", "Then", 
            "Tplate", "Until", "Wend", "While", "DOT", "COMMA", "MINUS", 
            "COLON", "ASTERISK", "ANGLE_BRACKET", "REGISTER", "WORD", "DECIMAL_NUMBER", 
            "BINARY_NUMBER", "HEX_NUMBER", "STRING", "CHAR", "NEWLINE", 
            "COMMENT", "WS" ]

    ruleNames = [ "Asect", "Break", "Continue", "Do", "Else", "End", "Ext", 
                  "Fi", "If", "Is", "Macro", "Restore", "Rsect", "Save", 
                  "Stays", "Then", "Tplate", "Until", "Wend", "While", "DOT", 
                  "COMMA", "MINUS", "COLON", "ASTERISK", "ANGLE_BRACKET", 
                  "REGISTER", "WORD", "DECIMAL_NUMBER", "BINARY_NUMBER", 
                  "HEX_NUMBER", "STRING", "CHAR", "NEWLINE", "COMMENT", 
                  "WS" ]

    grammarFileName = "AsmLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


