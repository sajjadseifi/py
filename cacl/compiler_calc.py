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
    val = valget(ast.expr)
    symtbl.put(name,val)
    valset(ast,val)

def exprunary(ast : AST.ASTExprUnary):
    opr = ast.oprator
    expr(ast.expr)

    print("PUSH %s%s" % (opr,valget(ast)))

def exprcalc(ast : AST.ASTExprCacluate):
    pass

def exprmath(ast : AST.ASTExprCall):
    pass

def exprprim(ast : AST.Node):
    pass