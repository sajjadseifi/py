import ast_calc as AST

def valget(ast : AST.Node):
    return ast.value.get("val")    

def valset(ast : AST.Node,val):
    ast.value["val"] = val

def idxget(ast : AST.Node):
    return ast.value.get("idx")    

def idxset(ast : AST.Node,idx):
    ast.value["idx"] = idx
