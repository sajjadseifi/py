# Grammar Calculator
'''
    :: Lexical Level ::
    
    token :=    + |
                - |
                * |
                / |
                %

    iden := [A-Za-z_][A-Za-z_0-9]*

    num  := [0-9]+
    
    comment := #[^\n]*

    :: Parser Level ::
    
    calc := |
        stmt calc

    stmt :=   expr  |
        print expr
            
    expr :=
        iden = expr |
        expr + expr |
        expr - expr |
        expr / expr |
        expr * expr |
        expr % expr |
        (expr)      |
        - expr      |
        + expr      |
        iden:expr   |
        iden        |
        num
'''

#Interpreter
from os.path import abspath
from lexer_calc import Lexer
from parser_tree_calc import ParserTree
from pre_parser_calc import pre_parse
from interpreter import interpret
from compiler_calc import compiler
import sys

if len(sys.argv) > 2:
    conf = sys.argv[1]
    path = sys.argv[2]
    addr = abspath(path)
    lex = Lexer(addr)
    pars = ParserTree(lex)
    ast = pars.parse()
    pre_parse(ast)
    if conf == "-i":
        interpret(ast)
    if conf == "-c":
        compiler(ast)
else:
    print("please enter -config path")