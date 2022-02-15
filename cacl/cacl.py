# Grammar Calculator
'''
    :: Lexical Level ::

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

faddr = "./test/0"
addr = abspath(faddr)
lex = Lexer(addr)
pars = ParserTree(lex)
ast = pars.parse()
pre_parse(ast)
interpret(ast)