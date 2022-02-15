import ast_calc as AST


def interpret(ast : AST.Node):
    if isinstance(ast,AST.ASTCalc):
        print("finished");
    else:
        print("ast error: please entered root ast calc");
