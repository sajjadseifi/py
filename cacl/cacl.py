# Grammar Calculator
'''
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

    iden := [A-Za-z_][A-Za-z_0-9]*

    num  := [0-9]+
    
    comment := #[^\n]*
'''

#Compiler
from cacl.lexer import Lexer
from cacl.parser import Parser


def __main__():
    lex = Lexer("../test/0")
    pars = Parser(lex)
    pars.calc()

