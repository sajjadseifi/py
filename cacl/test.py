
def test_lexer():
    lex = test_lexer("../test/0")
    while True:
        t = lex.droptoken()
        if not t.text:
            break
        print("token : %s" % t.text)
