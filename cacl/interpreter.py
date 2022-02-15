import ast_calc as AST
from value_calc import valget, valset
from symbols_calc import Symbols 
#semantic
symtbl = Symbols()

def interpret(ast : AST.Node):
    if isinstance(ast,AST.ASTCalc):
        calc(ast)
        print("finished");
    else:
        print("ast error: please entered root ast calc");

def calc(ast : AST.Node):
    if len(ast.children):
        stmt(ast.children[0])
        interpret(ast.children[1])
    
def stmt(ast : AST.Node):
    if isinstance(ast,AST.ASTStmtExpr):
        expr(ast)
    elif isinstance(ast,AST.ASTStmtPrint):
        print(valget(ast))
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
    val = valget(ast.expr)
    symtbl.put(name,val)

def exprunary(ast : AST.ASTExprUnary):
    opr = ast.oprator
    expr(ast.expr)

    if opr == "-":
        valset(ast, -valget(ast))

def exprcalc(ast : AST.ASTExprCacluate):
    val = 0;
    opr = ast.oprator
    
    if opr == "-":
        val = valget(ast.left) - valget(ast.right)
    elif opr == "+":
        val = valget(ast.left) + valget(ast.right)
    elif opr == "*":
        val = valget(ast.left) * valget(ast.right)
    elif opr == "/":
        val = valget(ast.left) / valget(ast.right)
    elif opr == "%":
        val = valget(ast.left) % valget(ast.right)

    valset(ast,val)

def exprmath(ast : AST.ASTExprCall):
    #call math function
    math = ast.iden.name
    #radian value
    val = valget(ast.expr)

    upval = val

    if math == "rad":
        upval = 1
    elif math == "cot":
        upval = 2
    elif math == "tan":
        upval = 3
    elif math == "sin":
        upval = 4
    elif math == "cos":
        upval = 5

    valset(ast,upval) 
    pass

def exprprim(ast : AST.Node):
    if isinstance(ast,AST.ASTNum):
        valset(ast,ast.children[0])
    elif isinstance(ast,AST.ASTIden):
        name = ast.children[0]
        val  = symtbl.get(name)
        valset(ast,val)