import ast_calc as AST
from symbols_calc import Symbols 
#semantic

symtbl = Symbols()

def valget(ast : AST.Node):
    return ast.value["val"]    
def valset(ast : AST.Node,val):
    ast.value["val"] = val

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
    elif isinstance(ast,AST.ASTNum):
        exprprim(ast)    

def exprass(ast : AST.ASTExprAss):
    pass

def exprunary(ast : AST.ASTExprUnary):
    pass

def exprcalc(ast : AST.Node):
    pass

def exprmath(ast : AST.Node):
    pass

def exprprim(ast : AST.Node):
    pass