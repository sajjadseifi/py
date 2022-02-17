import ast_lp as AST
from stack_lp import Stack

stklp = Stack(1024)

def interpreter(ast : AST.Node):
    if isinstance(ast,AST.ASTLp):
        lp(ast)
    else:
        print("ast error: please entered root ast LP");

def lp(ast : AST.ASTLp):
    if isinstance(ast,AST.ASTLp1):
        stmt(ast.stmt)
        interpreter(ast.lp)

def stmt(ast : AST.Node):
    if isinstance(ast,AST.ASTStmtPrint):
        stmtprint()
    if isinstance(ast,AST.ASTStmtPush):
        stmtpush(ast)
    if isinstance(ast,AST.ASTStmtMov):
        stmtmov(ast)
    if isinstance(ast,AST.ASTStmtMovld):
        stmtmovld(ast)
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

    stklp.print()

def stmtprint():
    num = stklp.pop()
    print(num)

def stmtpush(ast : AST.ASTStmtPush):
    num = int(ast.num)
    stklp.push(num)

def stmtmov(ast : AST.ASTStmtMov):
    tar = int(ast.tar)
    src = int(ast.src)
    
    if tar < 0 or tar >= stklp.size:
        print("out of bounds target",tar)
    if src < 0 or src >= stklp.size:
        print("out of bounds source",tar)
    if src >= tar :
        print("source position must less than target position",tar)
    
    ldnum = stklp.get(src)
    stklp.set(tar,ldnum);


def stmtmovld(ast : AST.ASTStmtMov):
    src = int(ast.src)
    stklp.push(src)

def stmtplus():
    nums = stklp.popn(2)
    stklp.push(nums[0] + nums[1])

def stmtmin():
    nums = stklp.popn(2)
    stklp.push(nums[0] - nums[1])

def stmtmul():
    nums = stklp.popn(2)
    stklp.push(nums[0] * nums[1])

def stmtdiv():
    nums = stklp.popn(2)
    stklp.push(nums[0] / nums[1])

def stmtper():
    nums = stklp.popn(2)
    stklp.push(nums[0] % nums[1])
