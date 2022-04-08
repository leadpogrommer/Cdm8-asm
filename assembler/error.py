from antlr4.error.Errors import CancellationException, ParseCancellationException
from antlr4.error.ErrorListener import ErrorListener


class LexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise CancellationException("Lexer cancelled")


class ParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseCancellationException("Parser cancelled")