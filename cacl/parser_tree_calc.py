#Resolve Ambiguity
'''
    expr := expr-ass

    expr-ass := expr-unary |
            expr-unary = expr

    unary-oprator := + |
                     - 

    expr-unary := expr-priority-0  |
        unary-oprator expr         |

    expr-priority-0 :=    expr-priority-1 |
        expr-priority-0 + expr-priority-1 |
        expr-priority-0 - expr-priority-1     

    expr-priority-1 :=  expr-priority-1 |
        expr-priority-1 / expr-capsol   |
        expr-priority-1 * expr-capsol   |
        expr-priority-1 % expr-capsol 

    expr-capsol := expr-prim |
        (expr)      

    expr-prim :=    |
        iden:expr   |
        iden        |
        num
'''
from lexer_calc import Lexer
import ast_calc as Ast
from utils_calc import priority0,priority1,unary 

class ParserTree:
    def __init__(self,lexer: Lexer):
        self.lexer = lexer

    def nextg(self):
        return self.lexer.gettoken().text    

    def nextd(self):
        return self.lexer.droptoken().text
 
    def infollow(self,toks):
        flw = self.nextg()
        
        if not isinstance(toks, list):
            return flw == toks

        for tok in toks:
            if flw == tok:
                return True
        
        return False

    def parse(self):
        return self.calc()

    def calc(self):
        if self.lexer.eof():
            return Ast.ASTCalc0()

        return Ast.ASTCalc1(self.stmt(),self.calc())
    
    def stmt(self):
        if self.infollow("print"):
            self.nextd()
            return Ast.ASTStmtPrint(self.expr())
        else:
            return Ast.ASTStmtExpr(self.expr())

    def expr(self):
        return self.ass()

    def ass(self):
        expr = self.exprunary()

        if self.infollow("="):
            self.nextd()
            return Ast.ASTExprAss(expr,self.expr())

        return expr

    def unaryoprator(self):
        if self.infollow(unary):
            return Ast.ASTExprUnary(self.nextd())
        
        return None

    def exprunary(self):
        opast = self.unaryoprator()
        
        if opast:
            return Ast.ASTExprUnary(opast,self.expr())

        return self.exprpriority0()

    def exprpriority0(self):
        e1 = self.exprpriority1()

        if self.infollow(priority0):
            opr = self.nextd()
            e2 = self.exprpriority1()
            return Ast.ASTExprCacluate(e1,opr,e2)

        return e1

    def exprpriority1(self):
        e1 = self.exprcabsol()

        if self.infollow(priority1):
            opr = self.nextd()
            e2 = self.exprpriority1()
            return Ast.ASTExprCacluate(e1,opr,e2)

        return e1

    def exprcabsol(self):
        if not self.infollow("("):
            return self.exprprim()

        self.nextd()
        expr = self.expr()

        if self.infollow(")"):
            self.nextd()
        else:
            print("syntax error : expected )")

        return expr

    def exprprim(self):
        if(self.nextg().isnumeric()):
            return Ast.ASTNum(self.nextd())
        elif(self.nextg().isidentifier()):
            iden = self.nextd()

            if self.infollow(":"):
                self.nextd()
                expr = self.expr()
                return Ast.ASTExprCall(iden,expr)

            return Ast.ASTIden(iden)
        else:
            return None
