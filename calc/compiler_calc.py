import ast_calc as AST
from ir_calc import IR
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
        compiler(ir,ast.children[1])
    
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
    expr(ir,ast.expr)
    
    idx = symtbl.get(name)

    if isinstance(idx,int) and idx > -1:
        ir.store(idx)
    else:
        last = ir.idxstk - 1
        print(name,last)
        symtbl.put(name,last)

def exprunary(ir:IR,ast : AST.ASTExprUnary):
    opr = ast.oprator
    expr(ir,ast.expr)

    ir.push(opr + 1)
    ir.mul()

def exprcalc(ir:IR,ast : AST.ASTExprCacluate):
    #sub expersion
    expr(ir,ast.left)
    expr(ir,ast.right)

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

def exprmath(ir:IR,ast : AST.ASTExprCall):
    call = ast.iden.name
    expr(ir,ast.expr)

def exprprim(ir:IR,ast : AST.Node):
    if isinstance(ast,AST.ASTNum):
        ir.push(ast.num)

    elif isinstance(ast,AST.ASTIden):
        name = ast.name
        idx  = symtbl.get(name)
        if isinstance(idx,int) and idx > -1:
            ir.load(idx)