from lexer_lp import Lexer

def test_lexer(lexer:Lexer):
    while True:
        tok = lexer.droptoken()
        if not tok:
            break
        print("token : %s" % tok)