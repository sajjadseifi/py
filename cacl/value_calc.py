import ast_calc as AST

def valget(ast : AST.Node):
    return ast.value["val"]    
def valset(ast : AST.Node,val):
    ast.value["val"] = val
