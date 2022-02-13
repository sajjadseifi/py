# Grammar Calculator
'''
    calc := |
        body calc

    body :=     |
        ass     |
        print expr
            
    ass :=
        iden = expr

    expr :=
        rad expr    |
        sin expr    |
        cos expr    |
        tan expr    |
        cot expr    |
        expr + expr |
        expr - expr |
        expr / expr |
        expr * expr |
        expr % expr |
        (expr)      |
        iden        |
        num

    iden := [A-Za-z_][A-Za-z_0-9]*

    num  := [0-9]+
    
    comment := #[^\n]*
'''

code = input()
while code.upper() != 'E':
    print("code : %s" % code)
    code = input()
