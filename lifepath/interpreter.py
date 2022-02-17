import ast_lp as AST
from lifepath.value_lp import numget

stack = list()

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
    if isinstance(ast,AST.ASTStmtPush):
        stmtpush(ast)
    if isinstance(ast,AST.ASTStmtPlus):
        stmtplus()
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

def stmtpush(ast : AST.ASTStmtPush):
    num = int(ast.num)
    stack.append(num)

def stmtplus():
    num1 = stack.pop()
    num2 = stack.pop()

    sum = num2 + num1

    stack.append(sum)
