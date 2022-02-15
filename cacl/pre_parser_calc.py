
import ast_calc as AST
from value_calc import valset

def pre_parse(ast :AST.Node):
    setnumval(ast)

def setnumval(ast : AST.Node):
    for ast in ast.children:
        if isinstance(ast,AST.ASTNum):
            valset(ast,ast.num)
        setnumval(ast)
