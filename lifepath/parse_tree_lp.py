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
import ast_lp as AST


class ParseTree:
    def __init__(self,lex : Lexer):
        self.lex = lex

    def next(self): 
        return self.lex.droptoken()
    
    def lp(self):
        if self.lex.eof():
            return AST.ASTLp0()
            
        return AST.ASTLp1(self.stmt(),self.lp())
    
    def stmt(self):
        pass