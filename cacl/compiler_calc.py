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
    pass