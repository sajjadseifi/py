
import ast_calc as AST
from value_calc import valset

def pre_parse(ast :AST.Node):
    setnumval(ast)

def setnumval(ast : AST.Node):
    for cast in ast.children:
        if isinstance(ast,AST.ASTNum):
            valset(ast,int(ast.num))

        if isinstance(cast,AST.Node):
            setnumval(cast)
