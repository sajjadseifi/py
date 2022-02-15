import ast_calc as AST


def interpret(ast : AST.Node):
    if isinstance(ast,AST.ASTCalc):
        calc(ast)
        print("finished");
    else:
        print("ast error: please entered root ast calc");

def calc(ast : AST.Node):
    if len(ast.children):
        interpret(ast.children[1])
