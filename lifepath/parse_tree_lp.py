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
        ast = None
        key = self.next()
        num = self.next()

        if key == "PUSH":
            ast =  AST.ASTStmtPush(num)
        if key == "PLUS":
            ast = AST.ASTStmtPlus(num)
        if key == "MIN":
            ast = AST.ASTStmtMin(num)
        if key == "MUL":
            ast = AST.ASTStmtMul(num)
        if key == "DIV":
            ast = AST.ASTStmtDiv(num)
        if key == "PER":
            ast = AST.ASTStmtPer(num)
        if key == "PRINT":
            ast = AST.ASTStmtPrint(num)
        
        if not ast:
            print("syntax error : expected keyword [%s]" % key)
            return None    

        if not num.isnumeric():
            print("syntax error : expected numeric token [%s]" % num)

        return ast