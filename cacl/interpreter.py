import ast_calc as AST

#semantic
def val(ast : AST.Node):
    return ast.value.get("val")    

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
        print(val(ast))
    else:
        print("ast error: this ast is not stmt");

def expr(ast : AST.Node):
    pass