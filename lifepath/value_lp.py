import ast_lp as AST

def numget(ast : AST.Node):
    return ast.value.get("num")    
def numset(ast : AST.Node,val):
    ast.value["num"] = val
