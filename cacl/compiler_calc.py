import ast_calc as AST
from cacl.ir_calc import IR
from value_calc import valget, valset
from symbols_calc import Symbols 
#semantic
symtbl = Symbols()


def compiler(ir:IR,ast : AST.Node):
    if isinstance(ast,AST.ASTCalc):
        calc(ir,ast)
    else:
        print("ast error: please entered root ast calc");

    ir.finished()

def calc(ir:IR,ast : AST.Node):
    if len(ast.children):
        stmt(ir,ast.first())
        compiler(ast.children[1])
    
def stmt(ir:IR,ast : AST.ASTStmt):
    if isinstance(ast,AST.ASTStmtExpr):
        expr(ir,ast.first())
    elif isinstance(ast,AST.ASTStmtPrint):
        cast = ast.first()
        expr(ir,cast)
        ir.print()
    else:
        print("ast error: this ast is not stmt");

def expr(ir:IR,ast : AST.Node):
    if isinstance(ast,AST.ASTExprAss):
        exprass(ir,ast)    
    elif isinstance(ast,AST.ASTExprUnary):
        exprunary(ir,ast)    
    elif isinstance(ast,AST.ASTExprCacluate):
        exprcalc(ir,ast)    
    elif isinstance(ast,AST.ASTExprCall):
        exprmath(ir,ast)    
    elif isinstance(ast,AST.ASTNum) or isinstance(ast,AST.ASTIden):
        exprprim(ir,ast)    

def exprass(ir:IR,ast : AST.ASTExprAss):
    name = ast.iden.name
    expr(ast.expr)
    
    idx = symtbl.get(name)

    if idx:
        ir.mov(idx,ir.idxstk)
    else:
        symtbl.put(name,ir.idxstk)

def exprunary(ir:IR,ast : AST.ASTExprUnary):
    opr = ast.oprator
    expr(ast.expr)

    ir.push(opr + 1)
    ir.mul()
    ir.down()

def exprcalc(ir:IR,ast : AST.ASTExprCacluate):
    #sub expersion
    expr(ast.left)
    expr(ast.right)

    #print
    op = ast.oprator 

    if op == "+":
        ir.plus()
    if op == "-":
        ir.min()
    if op == "*":
        ir.mul()
    if op == "/":
        ir.div()
    if op == "%":
        ir.per()

    ir.down()

def exprmath(ir:IR,ast : AST.ASTExprCall):
    pass

def exprprim(ir:IR,ast : AST.Node):
    if isinstance(ast,AST.ASTNum):
        ir.push(ast.num)

    elif isinstance(ast,AST.ASTIden):
        name = ast.name
        idx  = symtbl.get(name)
        if isinstance(idx,int) and idx > -1:
            ir.up()
            ir.mov(ir.idxstk,idx)