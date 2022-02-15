# Python Learingn...

# Tasks

<h2>Cacluator Interpreter</h2>

Lexical : 
```
    iden := [A-Za-z_][A-Za-z_0-9]*

    num  := [0-9]+
    
    comment := #[^\n]*
```

Grammar :
```
    calc := |
        stmt calc

    stmt :=     |
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
```
