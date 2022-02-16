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
        PUSH num   |
        PLUS num   |
        MIN  num   |
        MUL  num   |
        DIV  num   |
        PER  num   |
        PRINT num
'''

from posixpath import abspath
from lexer_lp import Lexer
from test_lp import test_lexer

addr = abspath("./test/0")
lex = Lexer(addr)
test_lexer(lex)