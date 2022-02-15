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
from cacl.lexer import Lexer

unary = ["-","+"]
priority0 = ["-","+"]
priority1 = ["*","/","%"]

class Parser:
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

    def calc(self):
        if self.lexer.eof():
            return

        self.stmt()
        self.calc()        
    
    def stmt(self):
        expr = None
        if self.infollow("print"):
            self.nextd()
            expr = self.expr()
        else:
            expr = self.expr()
        return expr

    def expr(self):
        return self.ass()
   
    def ass(self):
        expr = self.exprunary()

        while self.infollow("="):
            # if not "iden".isidentifier():
            #     print("syntax error : expected identifier")
            self.nextd()
            expr2 = self.expr()

        return expr

    def unaryoprator(self):
        isun = False
        while self.infollow(unary):
            isun = True
            self.unaryoprator()
        
        return isun

    def exprunary(self):
        expr = None
        uns = self.unaryoprator()
        
        if uns:
            expr = self.expr()
        else:
            expr = self.exprpriority0()
        
        return expr

    def exprpriority0(self):
        expr1 = self.exprpriority1()

        if self.infollow(priority0):
            opr = self.nextd()
            expr2 = self.exprpriority1()

        return expr1

    def exprpriority1(self):
        expr1 = self.exprcabsol()

        if self.infollow(priority1):
            opr = self.nextd()
            expr2 = self.exprcabsol()

        return expr1

    def exprcabsol(self):
        expr = None
        if not self.infollow("("):
            expr = self.exprprim()
        else:
            self.nextd()
            expr = self.expr()

            if self.infollow(")"):
                self.nextd()
            else:
                print("syntax error : expected )")
        return expr

    def exprprim(self):
        if(self.nextg().isnumeric()):
            num = self.nextd()
            print("num",num)
            return num  
        elif(self.nextg().isidentifier()):
            iden = self.nextd()
            print("iden",iden)
            if self.infollow(":"):
                self.nextd()
                expr = self.expr()
                print("call",iden)
                return expr

            return iden
        else:
            return None
