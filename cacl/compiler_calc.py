import ast_calc as AST
from value_calc import valget, valset
from symbols_calc import Symbols 
#semantic
symtbl = Symbols()
oprcode = {
    "+" :"PLUS",
    "-" :"MIN",
    "*" :"MUL",
    "/" :"DIV",
    "%" :"PER",
}

class STK:
    def __init__(self,c:int) -> None:
        self.c = c
    def up(self):
        self.c +=1
    def down(self):
        self.c +=1

stk = STK(-1)

def pushstk(num):
    print("PUSH",num)
    stk.up()

def popstk():
    stk.down()

def compiler(ast : AST.Node):
    if isinstance(ast,AST.ASTCalc):
        calc(ast)
    else:
        print("ast error: please entered root ast calc");

def calc(ast : AST.Node):
    if len(ast.children):
        stmt(ast.first())
        compiler(ast.children[1])
    
def stmt(ast : AST.ASTStmt):
    if isinstance(ast,AST.ASTStmtExpr):
        expr(ast.first())
    elif isinstance(ast,AST.ASTStmtPrint):
        cast = ast.first()
        expr(cast)
        print("PRINT")
    else:
        print("ast error: this ast is not stmt");

def expr(ast : AST.Node):
    if isinstance(ast,AST.ASTExprAss):
        exprass(ast)    
    elif isinstance(ast,AST.ASTExprUnary):
        exprunary(ast)    
    elif isinstance(ast,AST.ASTExprCacluate):
        exprcalc(ast)    
    elif isinstance(ast,AST.ASTExprCall):
        exprmath(ast)    
    elif isinstance(ast,AST.ASTNum) or isinstance(ast,AST.ASTIden):
        exprprim(ast)    

def exprass(ast : AST.ASTExprAss):
    name = ast.iden.name
    expr(ast.expr)
    
    idx = symtbl.get(name)
    if idx:
        print("MOV",idx,stk.c)
    else:
        symtbl.put(name,stk.c)

def exprunary(ast : AST.ASTExprUnary):
    opr = ast.oprator
    expr(ast.expr)

    pushstk(opr + 1)
    print("MUL")
    popstk()

def exprcalc(ast : AST.ASTExprCacluate):
    #sub expersion
    expr(ast.left)
    expr(ast.right)
    #print
    print(oprcode.get(ast.oprator))
    popstk()

def exprmath(ast : AST.ASTExprCall):
    pass

def exprprim(ast : AST.Node):
    if isinstance(ast,AST.ASTNum):
        pushstk(ast.num)
    elif isinstance(ast,AST.ASTIden):
        name = ast.name
        idx  = symtbl.get(name)
        if isinstance(idx,int) and idx > -1:
            stk.up()
            print("MOV",stk.c,idx)
