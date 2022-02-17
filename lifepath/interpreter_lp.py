import ast_lp as AST

stack = list()
def get2num():
    if len(stack) < 2:
        print("stack size not enouf size for calculate")
        exit(1)

    r = stack.pop()
    l = stack.pop()

    return (l,r) 

def setnum(num):
    stack.append(int(num))

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

    print(stack)

def stmtprint():
    num = stack.pop()
    print(num)

def stmtpush(ast : AST.ASTStmtPush):
    num = int(ast.num)
    stack.append(num)

def stmtplus():
    nums = get2num()
    setnum(nums[0] + nums[1])

def stmtmin():
    nums = get2num()
    setnum(nums[0] - nums[1])

def stmtmul():
    nums = get2num()
    setnum(nums[0] * nums[1])

def stmtdiv():
    nums = get2num()
    setnum(nums[0] / nums[1])

def stmtper():
    nums = get2num()
    setnum(nums[0] % nums[1])
