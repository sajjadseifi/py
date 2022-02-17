#Interpreter
from os.path import abspath
from lexer_calc import Lexer
from parser_tree_calc import ParserTree
from pre_parser_calc import pre_parse
from interpreter import interpret
from compiler_calc import compiler
from ir_calc import IR
import sys

if len(sys.argv) > 2:
    conf = sys.argv[1]
    path = sys.argv[2]
    lex = Lexer(abspath(path))
    pars = ParserTree(lex)
    ast = pars.parse()
    pre_parse(ast)

    if conf == "-i":
        interpret(ast)
    if conf == "-c":
        path = "a.out"
        if len(sys.argv) > 3:
            path = sys.argv[3]

        ir = IR(abspath(path))
        compiler(ir,ast)

else:
    print("please enter -config path")