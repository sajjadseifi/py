#Grammar Parser
'''
    lp := |
        stmt lp
    
    stmt :=
        PUSH num   |
        PLUS num   |
        MIN  num   |
        MUL  num   |
        DIV  num   |
        PER  num   |
        PRINT num
'''

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