import ast_calc as AST
from value_calc import valget, valset
from symbols_calc import Symbols 
#semantic
symtbl = Symbols()

def interpret(ast : AST.Node):
    if isinstance(ast,AST.ASTCalc):
        calc(ast)
    else:
        print("ast error: please entered root ast calc");

def calc(ast : AST.Node):
    if len(ast.children):
        stmt(ast.first())
        interpret(ast.children[1])
    
def stmt(ast : AST.ASTStmt):
    if isinstance(ast,AST.ASTStmtExpr):
        expr(ast.first())
    elif isinstance(ast,AST.ASTStmtPrint):
        cast = ast.first()
        expr(cast)
        print("print -> %s" % valget(cast))
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
    val = valget(ast.expr)
    symtbl.put(name,val)
    valset(ast,val)

    print("assign -> %s = %s" % (name,val))

def exprunary(ast : AST.ASTExprUnary):
    opr = ast.oprator
    expr(ast.expr)

    if opr == "-":
        valset(ast, -valget(ast))

def exprcalc(ast : AST.ASTExprCacluate):
    val = 0;
    opr = ast.oprator
    
    expr(ast.left)
    expr(ast.right)

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

    print("calculate -> %s = %s %s %s" %
        (
            val,
            valget(ast.left),
            opr,
            valget(ast.right)
        )
    )

    valset(ast,val)

def exprmath(ast : AST.ASTExprCall):
    #call math function
    math = ast.iden.name
    #radian value
    expr(ast.expr)
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

    print("call -> %s(%s)" %(math,upval))
    
    valset(ast,upval) 

def exprprim(ast : AST.Node):
    if isinstance(ast,AST.ASTNum):
        valset(ast,int(ast.num))
    elif isinstance(ast,AST.ASTIden):
        name = ast.name
        val  = symtbl.get(name)
        valset(ast,int(val))