import ast_lp as AST
from lifepath.value_lp import numget

stack = list()
def get2num():
    n1 = stack.pop()
    n2 = stack.pop()

    return (n1,n2) 

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
        stmtmin()
    if isinstance(ast,AST.ASTStmtMul):
        stmtmul()
    if isinstance(ast,AST.ASTStmtDiv):
        stmtdiv()
    if isinstance(ast,AST.ASTStmtPer):
        stmtper()
    if isinstance(ast,AST.ASTStmtPrint):
        num = stack.pop()
        print(num)

def stmtpush(ast : AST.ASTStmtPush):
    num = int(ast.num)
    stack.append(num)

def stmtplus():
    nums = get2num()

    stack.append(nums[0] + nums[1])

def stmtmin():
    nums = get2num()

    stack.append(nums[0] - nums[1])

def stmtmul():
    nums = get2num()

    stack.append(nums[0] * nums[1])

def stmtdiv():
    nums = get2num()

    stack.append(nums[0] / nums[1])


def stmtper():
    nums = get2num()

    stack.append(nums[0] % nums[1])
