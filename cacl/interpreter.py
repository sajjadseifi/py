import ast_calc as AST


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
        pass
    elif isinstance(ast,AST.ASTStmtPrint):
        pass
    else:
        print("ast error: this ast is not stmt");
