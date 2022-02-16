#Grammar LifePath -> Calculator IR Interpreter
'''
    :: Lexer Level ::

    iden := [A-Za-z_][A-Za-z_0-9]*

    num  := [0-9]+
    
    comment := --[^\n]*

    :: Parser Level ::

    lp := |
        stmt lp
    
    stmt := |
        PSH expr
        PLS expr
        MIN expr
        MUL expr
        DIV expr
        PER expr
        PRINT expr

    expr := iden |
            num
'''