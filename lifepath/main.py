#Grammar LifePath -> Calculator IR Interpreter
'''
    :: Lexer Level ::

    iden := [A-Za-z_]+

    num  := [0-9]+
    
    comment := --[^\n]*

    :: Parser Level ::

    lp := |
        stmt lp
    
    stmt :=
        PUSH num    |
        PLUS        |
        MIN         |
        MUL         |
        DIV         |
        PER         |
        PRINT
'''

from posixpath import abspath
from lexer_lp import Lexer
from interpreter_lp import interpreter
from parse_tree_lp import ParseTree
import sys

if len(sys.argv):
    path = sys.argv[1]
    addr = abspath(path)
    lex = Lexer(addr)
    p3 = ParseTree(lex)
    ast = p3.parse()
    interpreter(ast)
