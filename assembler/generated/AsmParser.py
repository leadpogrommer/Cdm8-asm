# Generated from /home/ilya/work/cdm8e/ORiGinalASM/assembler/AsmParser.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("\u015e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\3\2\3\2\7\2O\n\2\f\2\16\2R\13\2\3\2\7\2U\n\2\f\2\16")
        buf.write("\2X\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3e\n\3\3\4\3\4\3\4\6\4j\n\4\r\4\16\4k\3\5\3\5\3\5\6\5")
        buf.write("q\n\5\r\5\16\5r\3\6\3\6\3\6\6\6x\n\6\r\6\16\6y\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u0086\n\b\f\b\16")
        buf.write("\b\u0089\13\b\3\t\3\t\3\t\3\t\6\t\u008f\n\t\r\t\16\t\u0090")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\6\f\u0099\n\f\r\f\16\f\u009a")
        buf.write("\3\r\3\r\6\r\u009f\n\r\r\r\16\r\u00a0\3\16\3\16\5\16\u00a5")
        buf.write("\n\16\3\16\6\16\u00a8\n\16\r\16\16\16\u00a9\3\16\5\16")
        buf.write("\u00ad\n\16\3\16\3\16\5\16\u00b1\n\16\3\16\6\16\u00b4")
        buf.write("\n\16\r\16\16\16\u00b5\5\16\u00b8\n\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\7\20\u00c0\n\20\f\20\16\20\u00c3\13\20")
        buf.write("\3\21\3\21\6\21\u00c7\n\21\r\21\16\21\u00c8\3\21\3\21")
        buf.write("\3\21\5\21\u00ce\n\21\3\21\3\21\6\21\u00d2\n\21\r\21\16")
        buf.write("\21\u00d3\3\22\7\22\u00d7\n\22\f\22\16\22\u00da\13\22")
        buf.write("\3\22\3\22\6\22\u00de\n\22\r\22\16\22\u00df\3\22\3\22")
        buf.write("\6\22\u00e4\n\22\r\22\16\22\u00e5\5\22\u00e8\n\22\3\23")
        buf.write("\3\23\3\23\3\23\6\23\u00ee\n\23\r\23\16\23\u00ef\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\6\25\u00f8\n\25\r\25\16\25\u00f9")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\6\30\u0104\n")
        buf.write("\30\r\30\16\30\u0105\3\30\3\30\3\30\3\30\6\30\u010c\n")
        buf.write("\30\r\30\16\30\u010d\3\30\3\30\3\30\6\30\u0113\n\30\r")
        buf.write("\30\16\30\u0114\3\31\3\31\3\32\3\32\6\32\u011b\n\32\r")
        buf.write("\32\16\32\u011c\3\32\3\32\3\32\3\32\6\32\u0123\n\32\r")
        buf.write("\32\16\32\u0124\3\33\3\33\3\33\3\33\3\34\3\34\3\34\6\34")
        buf.write("\u012e\n\34\r\34\16\34\u012f\3\35\3\35\5\35\u0134\n\35")
        buf.write("\3\35\6\35\u0137\n\35\r\35\16\35\u0138\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0141\n\36\3\37\5\37\u0144\n\37\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%")
        buf.write("\5%\u0155\n%\3%\3%\3%\5%\u015a\n%\3&\3&\3&\2\2\'\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJ\2\4\4\2\32\32\34\34\4\2\3\26\37\37\2\u016b")
        buf.write("\2L\3\2\2\2\4d\3\2\2\2\6f\3\2\2\2\bm\3\2\2\2\nt\3\2\2")
        buf.write("\2\f{\3\2\2\2\16\u0087\3\2\2\2\20\u008a\3\2\2\2\22\u0092")
        buf.write("\3\2\2\2\24\u0094\3\2\2\2\26\u0096\3\2\2\2\30\u009c\3")
        buf.write("\2\2\2\32\u00b7\3\2\2\2\34\u00b9\3\2\2\2\36\u00bc\3\2")
        buf.write("\2\2 \u00c4\3\2\2\2\"\u00d8\3\2\2\2$\u00e9\3\2\2\2&\u00f1")
        buf.write("\3\2\2\2(\u00f5\3\2\2\2*\u00fd\3\2\2\2,\u00ff\3\2\2\2")
        buf.write(".\u0101\3\2\2\2\60\u0116\3\2\2\2\62\u0118\3\2\2\2\64\u0126")
        buf.write("\3\2\2\2\66\u012a\3\2\2\28\u0131\3\2\2\2:\u0140\3\2\2")
        buf.write("\2<\u0143\3\2\2\2>\u0149\3\2\2\2@\u014b\3\2\2\2B\u014d")
        buf.write("\3\2\2\2D\u014f\3\2\2\2F\u0151\3\2\2\2H\u0159\3\2\2\2")
        buf.write("J\u015b\3\2\2\2LP\5\20\t\2MO\7%\2\2NM\3\2\2\2OR\3\2\2")
        buf.write("\2PN\3\2\2\2PQ\3\2\2\2QV\3\2\2\2RP\3\2\2\2SU\5\4\3\2T")
        buf.write("S\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2WY\3\2\2\2XV\3")
        buf.write("\2\2\2YZ\7\b\2\2Z\3\3\2\2\2[\\\5\6\4\2\\]\5\f\7\2]e\3")
        buf.write("\2\2\2^_\5\b\5\2_`\5\f\7\2`e\3\2\2\2ab\5\n\6\2bc\5\f\7")
        buf.write("\2ce\3\2\2\2d[\3\2\2\2d^\3\2\2\2da\3\2\2\2e\5\3\2\2\2")
        buf.write("fg\7\3\2\2gi\5H%\2hj\7%\2\2ih\3\2\2\2jk\3\2\2\2ki\3\2")
        buf.write("\2\2kl\3\2\2\2l\7\3\2\2\2mn\7\17\2\2np\5J&\2oq\7%\2\2")
        buf.write("po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\t\3\2\2\2tu")
        buf.write("\7\23\2\2uw\5J&\2vx\7%\2\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2")
        buf.write("\2yz\3\2\2\2z\13\3\2\2\2{|\5\16\b\2|\r\3\2\2\2}\u0086")
        buf.write("\5\26\f\2~\u0086\5\30\r\2\177\u0086\5\32\16\2\u0080\u0086")
        buf.write("\5 \21\2\u0081\u0086\5.\30\2\u0082\u0086\5\62\32\2\u0083")
        buf.write("\u0086\5\64\33\2\u0084\u0086\5\20\t\2\u0085}\3\2\2\2\u0085")
        buf.write("~\3\2\2\2\u0085\177\3\2\2\2\u0085\u0080\3\2\2\2\u0085")
        buf.write("\u0081\3\2\2\2\u0085\u0082\3\2\2\2\u0085\u0083\3\2\2\2")
        buf.write("\u0085\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3")
        buf.write("\2\2\2\u0087\u0088\3\2\2\2\u0088\17\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u008a\u008b\7\35\2\2\u008b\u008c\5\22\n\2\u008c")
        buf.write("\u008e\5\24\13\2\u008d\u008f\7%\2\2\u008e\u008d\3\2\2")
        buf.write("\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\21\3\2\2\2\u0092\u0093\7 \2\2\u0093\23")
        buf.write("\3\2\2\2\u0094\u0095\7(\2\2\u0095\25\3\2\2\2\u0096\u0098")
        buf.write("\7\4\2\2\u0097\u0099\7%\2\2\u0098\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\27\3\2\2\2\u009c\u009e\7\5\2\2\u009d\u009f\7%\2")
        buf.write("\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\31\3\2\2\2\u00a2\u00a4")
        buf.write("\5\34\17\2\u00a3\u00a5\7\t\2\2\u00a4\u00a3\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a8\7%\2\2")
        buf.write("\u00a7\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00b8\3\2\2\2\u00ab\u00ad")
        buf.write("\5\34\17\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\u00b0\5@!\2\u00af\u00b1\5\36\20\2")
        buf.write("\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3")
        buf.write("\2\2\2\u00b2\u00b4\7%\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b8\3\2\2\2\u00b7\u00a2\3\2\2\2\u00b7\u00ac\3\2\2\2")
        buf.write("\u00b8\33\3\2\2\2\u00b9\u00ba\5> \2\u00ba\u00bb\t\2\2")
        buf.write("\2\u00bb\35\3\2\2\2\u00bc\u00c1\5:\36\2\u00bd\u00be\7")
        buf.write("\30\2\2\u00be\u00c0\5:\36\2\u00bf\u00bd\3\2\2\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\37\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c6\7\13")
        buf.write("\2\2\u00c5\u00c7\7%\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00cb\5\"\22\2\u00cb\u00cd\5\16\b")
        buf.write("\2\u00cc\u00ce\5(\25\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\7\n\2\2\u00d0")
        buf.write("\u00d2\7%\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4!\3\2\2")
        buf.write("\2\u00d5\u00d7\5$\23\2\u00d6\u00d5\3\2\2\2\u00d7\u00da")
        buf.write("\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00db\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dd\5&\24\2")
        buf.write("\u00dc\u00de\7%\2\2\u00dd\u00dc\3\2\2\2\u00de\u00df\3")
        buf.write("\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e7")
        buf.write("\3\2\2\2\u00e1\u00e3\7\22\2\2\u00e2\u00e4\7%\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e1\3")
        buf.write("\2\2\2\u00e7\u00e8\3\2\2\2\u00e8#\3\2\2\2\u00e9\u00ea")
        buf.write("\5&\24\2\u00ea\u00eb\7\30\2\2\u00eb\u00ed\5,\27\2\u00ec")
        buf.write("\u00ee\7%\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0%\3\2\2")
        buf.write("\2\u00f1\u00f2\5\16\b\2\u00f2\u00f3\7\f\2\2\u00f3\u00f4")
        buf.write("\5*\26\2\u00f4\'\3\2\2\2\u00f5\u00f7\7\7\2\2\u00f6\u00f8")
        buf.write("\7%\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00fc\5\16\b\2\u00fc)\3\2\2\2\u00fd\u00fe\7\37")
        buf.write("\2\2\u00fe+\3\2\2\2\u00ff\u0100\7\37\2\2\u0100-\3\2\2")
        buf.write("\2\u0101\u0103\7\26\2\2\u0102\u0104\7%\2\2\u0103\u0102")
        buf.write("\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2\2\2\u0105")
        buf.write("\u0106\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\5\60\31")
        buf.write("\2\u0108\u0109\7\21\2\2\u0109\u010b\5*\26\2\u010a\u010c")
        buf.write("\7%\2\2\u010b\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0110\5\16\b\2\u0110\u0112\7\25\2\2\u0111\u0113")
        buf.write("\7%\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115/\3\2\2\2\u0116")
        buf.write("\u0117\5\16\b\2\u0117\61\3\2\2\2\u0118\u011a\7\6\2\2\u0119")
        buf.write("\u011b\7%\2\2\u011a\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\3")
        buf.write("\2\2\2\u011e\u011f\5\16\b\2\u011f\u0120\7\24\2\2\u0120")
        buf.write("\u0122\5*\26\2\u0121\u0123\7%\2\2\u0122\u0121\3\2\2\2")
        buf.write("\u0123\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3")
        buf.write("\2\2\2\u0125\63\3\2\2\2\u0126\u0127\5\66\34\2\u0127\u0128")
        buf.write("\5\16\b\2\u0128\u0129\58\35\2\u0129\65\3\2\2\2\u012a\u012b")
        buf.write("\7\20\2\2\u012b\u012d\5D#\2\u012c\u012e\7%\2\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\67\3\2\2\2\u0131\u0133\7\16\2\2\u0132")
        buf.write("\u0134\5D#\2\u0133\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("\u0136\3\2\2\2\u0135\u0137\7%\2\2\u0136\u0135\3\2\2\2")
        buf.write("\u0137\u0138\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3")
        buf.write("\2\2\2\u01399\3\2\2\2\u013a\u0141\5H%\2\u013b\u0141\5")
        buf.write("F$\2\u013c\u0141\5B\"\2\u013d\u0141\5D#\2\u013e\u0141")
        buf.write("\5> \2\u013f\u0141\5<\37\2\u0140\u013a\3\2\2\2\u0140\u013b")
        buf.write("\3\2\2\2\u0140\u013c\3\2\2\2\u0140\u013d\3\2\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141;\3\2\2\2\u0142")
        buf.write("\u0144\7\31\2\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2\2")
        buf.write("\2\u0144\u0145\3\2\2\2\u0145\u0146\5J&\2\u0146\u0147\7")
        buf.write("\27\2\2\u0147\u0148\5J&\2\u0148=\3\2\2\2\u0149\u014a\5")
        buf.write("J&\2\u014a?\3\2\2\2\u014b\u014c\7\37\2\2\u014cA\3\2\2")
        buf.write("\2\u014d\u014e\7#\2\2\u014eC\3\2\2\2\u014f\u0150\7\36")
        buf.write("\2\2\u0150E\3\2\2\2\u0151\u0152\7$\2\2\u0152G\3\2\2\2")
        buf.write("\u0153\u0155\7\31\2\2\u0154\u0153\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u015a\7 \2\2\u0157")
        buf.write("\u015a\7\"\2\2\u0158\u015a\7!\2\2\u0159\u0154\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015aI\3\2\2")
        buf.write("\2\u015b\u015c\t\3\2\2\u015cK\3\2\2\2)PVdkry\u0085\u0087")
        buf.write("\u0090\u009a\u00a0\u00a4\u00a9\u00ac\u00b0\u00b5\u00b7")
        buf.write("\u00c1\u00c8\u00cd\u00d3\u00d8\u00df\u00e5\u00e7\u00ef")
        buf.write("\u00f9\u0105\u010d\u0114\u011c\u0124\u012f\u0133\u0138")
        buf.write("\u0140\u0143\u0154\u0159")
        return buf.getvalue()


class AsmParser ( Parser ):

    grammarFileName = "AsmParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'asect'", "'break'", "'continue'", "'do'", 
                     "'else'", "'end'", "'ext'", "'fi'", "'if'", "'is'", 
                     "'macro'", "'restore'", "'rsect'", "'save'", "'stays'", 
                     "'then'", "'tplate'", "'until'", "'wend'", "'while'", 
                     "'.'", "','", "'-'", "':'", "'*'", "'>'", "'-|'" ]

    symbolicNames = [ "<INVALID>", "Asect", "Break", "Continue", "Do", "Else", 
                      "End", "Ext", "Fi", "If", "Is", "Macro", "Restore", 
                      "Rsect", "Save", "Stays", "Then", "Tplate", "Until", 
                      "Wend", "While", "DOT", "COMMA", "MINUS", "COLON", 
                      "ASTERISK", "ANGLE_BRACKET", "LINE_MARK_MARKER", "REGISTER", 
                      "WORD", "DECIMAL_NUMBER", "BINARY_NUMBER", "HEX_NUMBER", 
                      "STRING", "CHAR", "NEWLINE", "COMMENT", "WS", "BASE64" ]

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
    RULE_argument = 28
    RULE_template_field = 29
    RULE_label = 30
    RULE_instruction = 31
    RULE_string = 32
    RULE_register = 33
    RULE_character = 34
    RULE_number = 35
    RULE_name = 36

    ruleNames =  [ "program", "section", "asect_header", "rsect_header", 
                   "tplate_header", "section_body", "code_block", "line_mark", 
                   "line_number", "filepath", "break_statement", "continue_statement", 
                   "line", "label_declaration", "arguments", "conditional", 
                   "conditions", "connective_condition", "condition", "else_clause", 
                   "branch_mnemonic", "conjunction", "while_loop", "while_condition", 
                   "until_loop", "save_restore_statement", "save_statement", 
                   "restore_statement", "argument", "template_field", "label", 
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
    If=9
    Is=10
    Macro=11
    Restore=12
    Rsect=13
    Save=14
    Stays=15
    Then=16
    Tplate=17
    Until=18
    Wend=19
    While=20
    DOT=21
    COMMA=22
    MINUS=23
    COLON=24
    ASTERISK=25
    ANGLE_BRACKET=26
    LINE_MARK_MARKER=27
    REGISTER=28
    WORD=29
    DECIMAL_NUMBER=30
    BINARY_NUMBER=31
    HEX_NUMBER=32
    STRING=33
    CHAR=34
    NEWLINE=35
    COMMENT=36
    WS=37
    BASE64=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
            self.state = 74
            self.line_mark()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.NEWLINE:
                self.state = 75
                self.match(AsmParser.NEWLINE)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Rsect) | (1 << AsmParser.Tplate))) != 0):
                self.state = 81
                self.section()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
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
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmParser.Asect]:
                localctx = AsmParser.AbsoluteSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.asect_header()
                self.state = 90
                self.section_body()
                pass
            elif token in [AsmParser.Rsect]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.rsect_header()
                self.state = 93
                self.section_body()
                pass
            elif token in [AsmParser.Tplate]:
                localctx = AsmParser.TemplateSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.tplate_header()
                self.state = 96
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
            self.state = 100
            self.match(AsmParser.Asect)
            self.state = 101
            self.number()
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.match(AsmParser.NEWLINE)
                self.state = 105 
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
            self.state = 107
            self.match(AsmParser.Rsect)
            self.state = 108
            self.name()
            self.state = 110 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 109
                self.match(AsmParser.NEWLINE)
                self.state = 112 
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
            self.state = 114
            self.match(AsmParser.Tplate)
            self.state = 115
            self.name()
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.match(AsmParser.NEWLINE)
                self.state = 119 
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
            self.state = 121
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
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 123
                        self.break_statement()
                        pass

                    elif la_ == 2:
                        self.state = 124
                        self.continue_statement()
                        pass

                    elif la_ == 3:
                        self.state = 125
                        self.line()
                        pass

                    elif la_ == 4:
                        self.state = 126
                        self.conditional()
                        pass

                    elif la_ == 5:
                        self.state = 127
                        self.while_loop()
                        pass

                    elif la_ == 6:
                        self.state = 128
                        self.until_loop()
                        pass

                    elif la_ == 7:
                        self.state = 129
                        self.save_restore_statement()
                        pass

                    elif la_ == 8:
                        self.state = 130
                        self.line_mark()
                        pass

             
                self.state = 135
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

        def LINE_MARK_MARKER(self):
            return self.getToken(AsmParser.LINE_MARK_MARKER, 0)

        def line_number(self):
            return self.getTypedRuleContext(AsmParser.Line_numberContext,0)


        def filepath(self):
            return self.getTypedRuleContext(AsmParser.FilepathContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 137
            self.line_number()
            self.state = 138
            self.filepath()
            self.state = 140 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 139
                    self.match(AsmParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 142 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 144
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
            self.state = 146
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
            self.state = 148
            self.match(AsmParser.Break)
            self.state = 150 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 149
                self.match(AsmParser.NEWLINE)
                self.state = 152 
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
            self.state = 154
            self.match(AsmParser.Continue)
            self.state = 156 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 155
                self.match(AsmParser.NEWLINE)
                self.state = 158 
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
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = AsmParser.StandaloneLabelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.label_declaration()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==AsmParser.Ext:
                    self.state = 161
                    self.match(AsmParser.Ext)


                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 164
                    self.match(AsmParser.NEWLINE)
                    self.state = 167 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==AsmParser.NEWLINE):
                        break

                pass

            elif la_ == 2:
                localctx = AsmParser.InstructionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 169
                    self.label_declaration()


                self.state = 172
                self.instruction()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Break) | (1 << AsmParser.Continue) | (1 << AsmParser.Do) | (1 << AsmParser.Else) | (1 << AsmParser.End) | (1 << AsmParser.Ext) | (1 << AsmParser.Fi) | (1 << AsmParser.If) | (1 << AsmParser.Is) | (1 << AsmParser.Macro) | (1 << AsmParser.Restore) | (1 << AsmParser.Rsect) | (1 << AsmParser.Save) | (1 << AsmParser.Stays) | (1 << AsmParser.Then) | (1 << AsmParser.Tplate) | (1 << AsmParser.Until) | (1 << AsmParser.Wend) | (1 << AsmParser.While) | (1 << AsmParser.MINUS) | (1 << AsmParser.REGISTER) | (1 << AsmParser.WORD) | (1 << AsmParser.DECIMAL_NUMBER) | (1 << AsmParser.BINARY_NUMBER) | (1 << AsmParser.HEX_NUMBER) | (1 << AsmParser.STRING) | (1 << AsmParser.CHAR))) != 0):
                    self.state = 173
                    self.arguments()


                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 176
                    self.match(AsmParser.NEWLINE)
                    self.state = 179 
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
            self.state = 183
            self.label()
            self.state = 184
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
            self.state = 186
            self.argument()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AsmParser.COMMA:
                self.state = 187
                self.match(AsmParser.COMMA)
                self.state = 188
                self.argument()
                self.state = 193
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
            self.state = 194
            self.match(AsmParser.If)
            self.state = 196 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 195
                self.match(AsmParser.NEWLINE)
                self.state = 198 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 200
            self.conditions()
            self.state = 201
            self.code_block()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.Else:
                self.state = 202
                self.else_clause()


            self.state = 205
            self.match(AsmParser.Fi)
            self.state = 207 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 206
                self.match(AsmParser.NEWLINE)
                self.state = 209 
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
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 211
                    self.connective_condition() 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 217
            self.condition()
            self.state = 219 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 218
                self.match(AsmParser.NEWLINE)
                self.state = 221 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 223
                self.match(AsmParser.Then)
                self.state = 225 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 224
                    self.match(AsmParser.NEWLINE)
                    self.state = 227 
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
            self.state = 231
            self.condition()
            self.state = 232
            self.match(AsmParser.COMMA)
            self.state = 233
            self.conjunction()
            self.state = 235 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 234
                self.match(AsmParser.NEWLINE)
                self.state = 237 
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
            self.state = 239
            self.code_block()
            self.state = 240
            self.match(AsmParser.Is)
            self.state = 241
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
            self.state = 243
            self.match(AsmParser.Else)
            self.state = 245 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 244
                self.match(AsmParser.NEWLINE)
                self.state = 247 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 249
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
            self.state = 251
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
            self.state = 253
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
            self.state = 255
            self.match(AsmParser.While)
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

            self.state = 261
            self.while_condition()
            self.state = 262
            self.match(AsmParser.Stays)
            self.state = 263
            self.branch_mnemonic()
            self.state = 265 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 264
                self.match(AsmParser.NEWLINE)
                self.state = 267 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 269
            self.code_block()
            self.state = 270
            self.match(AsmParser.Wend)
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
            self.state = 276
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
            self.state = 278
            self.match(AsmParser.Do)
            self.state = 280 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 279
                self.match(AsmParser.NEWLINE)
                self.state = 282 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AsmParser.NEWLINE):
                    break

            self.state = 284
            self.code_block()
            self.state = 285
            self.match(AsmParser.Until)
            self.state = 286
            self.branch_mnemonic()
            self.state = 288 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 287
                self.match(AsmParser.NEWLINE)
                self.state = 290 
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
            self.state = 292
            self.save_statement()
            self.state = 293
            self.code_block()
            self.state = 294
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
            self.state = 296
            self.match(AsmParser.Save)
            self.state = 297
            self.register()
            self.state = 299 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 298
                self.match(AsmParser.NEWLINE)
                self.state = 301 
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
            self.state = 303
            self.match(AsmParser.Restore)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.REGISTER:
                self.state = 304
                self.register()


            self.state = 308 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 307
                self.match(AsmParser.NEWLINE)
                self.state = 310 
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


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(AsmParser.NumberContext,0)


        def character(self):
            return self.getTypedRuleContext(AsmParser.CharacterContext,0)


        def string(self):
            return self.getTypedRuleContext(AsmParser.StringContext,0)


        def register(self):
            return self.getTypedRuleContext(AsmParser.RegisterContext,0)


        def label(self):
            return self.getTypedRuleContext(AsmParser.LabelContext,0)


        def template_field(self):
            return self.getTypedRuleContext(AsmParser.Template_fieldContext,0)


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
        self.enterRule(localctx, 56, self.RULE_argument)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.character()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.string()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.register()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.label()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 317
                self.template_field()
                pass


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

        def MINUS(self):
            return self.getToken(AsmParser.MINUS, 0)

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
        self.enterRule(localctx, 58, self.RULE_template_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AsmParser.MINUS:
                self.state = 320
                self.match(AsmParser.MINUS)


            self.state = 323
            self.name()
            self.state = 324
            self.match(AsmParser.DOT)
            self.state = 325
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
        self.enterRule(localctx, 60, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
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
        self.enterRule(localctx, 62, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
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
        self.enterRule(localctx, 64, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
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
        self.enterRule(localctx, 66, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
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
        self.enterRule(localctx, 68, self.RULE_character)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
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

        def MINUS(self):
            return self.getToken(AsmParser.MINUS, 0)

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
        self.enterRule(localctx, 70, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmParser.MINUS, AsmParser.DECIMAL_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==AsmParser.MINUS:
                    self.state = 337
                    self.match(AsmParser.MINUS)


                self.state = 340
                self.match(AsmParser.DECIMAL_NUMBER)
                pass
            elif token in [AsmParser.HEX_NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(AsmParser.HEX_NUMBER)
                pass
            elif token in [AsmParser.BINARY_NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
                self.match(AsmParser.BINARY_NUMBER)
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

        def If(self):
            return self.getToken(AsmParser.If, 0)

        def Is(self):
            return self.getToken(AsmParser.Is, 0)

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
        self.enterRule(localctx, 72, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AsmParser.Asect) | (1 << AsmParser.Break) | (1 << AsmParser.Continue) | (1 << AsmParser.Do) | (1 << AsmParser.Else) | (1 << AsmParser.End) | (1 << AsmParser.Ext) | (1 << AsmParser.Fi) | (1 << AsmParser.If) | (1 << AsmParser.Is) | (1 << AsmParser.Macro) | (1 << AsmParser.Restore) | (1 << AsmParser.Rsect) | (1 << AsmParser.Save) | (1 << AsmParser.Stays) | (1 << AsmParser.Then) | (1 << AsmParser.Tplate) | (1 << AsmParser.Until) | (1 << AsmParser.Wend) | (1 << AsmParser.While) | (1 << AsmParser.WORD))) != 0)):
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





