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
            if not num.isnumeric():
                print("syntax error : expected numeric token [%s]" % num)
            ast =  AST.ASTStmtPush(num)
        if key == "MOV":
            src = self.next()
            if not src.isnumeric():
                print("syntax error : expected numeric token [%s]" % num)
            ast = AST.ASTStmtMov(src)
        elif key == "SET":
            src = self.next()
            if not src.isnumeric():
                print("syntax error : expected numeric token [%s]" % num)     
            ast = AST.ASTStmtSet(src)
        elif key == "PRINT":
            ast = AST.ASTStmtPrint()
        elif key == "PLUS":
            ast = AST.ASTStmtPlus()
        elif key == "MIN":
            ast = AST.ASTStmtMin()
        elif key == "MUL":
            ast = AST.ASTStmtMul()
        elif key == "DIV":
            ast = AST.ASTStmtDiv()
        elif key == "PER":
            ast = AST.ASTStmtPer()

        if not ast:
            print("syntax error : expected keyword [%s]" % key)
            return None    

        return ast