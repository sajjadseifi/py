from lexer_lp import Lexer

class ParserRD:
    def __init__(self,lex : Lexer):
        self.lex = lex

    def lp(self):
        if self.lex.eof():
            return

        self.stmt()
        self.lp()

    def stmt(self):
        pass