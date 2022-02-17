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

def stmt(ast : AST.Node):
    num = None
    if len(ast.children) > 0:
        num = ast.children[0]

    if isinstance(ast,AST.ASTStmtPush):
        pass
    if isinstance(ast,AST.ASTStmtPlus):
        pass
    if isinstance(ast,AST.ASTStmtMin):
        pass
    if isinstance(ast,AST.ASTStmtMul):
        pass
    if isinstance(ast,AST.ASTStmtDiv):
        pass
    if isinstance(ast,AST.ASTStmtPer):
        pass
    if isinstance(ast,AST.ASTStmtPrint):
        pass

