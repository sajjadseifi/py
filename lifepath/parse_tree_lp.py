#Grammar Parser
'''
    lp := |
        stmt lp
    
    stmt :=
        PUSH num    |
        PLUS        |
        MIN         |
        MUL         |
        DIV         |
        PER         |
        PRINT
'''

from lexer_lp import Lexer
import ast_lp as AST


class ParseTree:
    def __init__(self,lex : Lexer):
        self.lex = lex

    def next(self): 
        return self.lex.droptoken()
    
    def parse(self):
       return self.lp()

    def lp(self):
        if self.lex.eof():
            return AST.ASTLp0()
            
        return AST.ASTLp1(self.stmt(),self.lp())
    
    def stmt(self):
        key = self.next()
        ast =  None        
        if key == "PUSH":
            num = self.next()
            ast =  AST.ASTStmtPush(num)
            if not num.isnumeric():
                print("syntax error : expected numeric token [%s]" % num)
        if key == "PRINT":
            ast = AST.ASTStmtPrint()
        if key == "PLUS":
            ast = AST.ASTStmtPlus()
        if key == "MIN":
            ast = AST.ASTStmtMin()
        if key == "MUL":
            ast = AST.ASTStmtMul()
        if key == "DIV":
            ast = AST.ASTStmtDiv()
        if key == "PER":
            ast = AST.ASTStmtPer()

        if not ast:
            print("syntax error : expected keyword [%s]" % key)
            return None    

        return ast