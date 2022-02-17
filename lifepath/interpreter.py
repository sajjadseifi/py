import ast_lp as AST

def interpreter(ast : AST.Node):
    if isinstance(ast,AST.ASTLp):
        lp(ast)
    else:
        print("ast error: please entered root ast LP");

def lp(ast : AST.Node):
    if len(ast.children):
        stmt(ast.first())
        interpreter(ast.children[1])

def stmt():
    pass