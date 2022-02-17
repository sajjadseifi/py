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
