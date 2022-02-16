#Grammar LifePath -> Calculator IR Interpreter
'''
    :: Lexer Level ::

    num  := [0-9]+
    
    comment := --[^\n]*

    :: Parser Level ::

    lp := |
        stmt lp
    
    stmt := |
        keyw num

    keyw := 
        PUSH    |
        PLUS    |
        MIN     |
        MUL     |
        DIV     |
        PER     |
        PRINT
'''