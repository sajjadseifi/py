# Python Learingn...

# Tasks

<h2>Cacluator Interpreter</h2>

Lexical : 
```
        
    token :=    + |
                - |
                * |
                / |
                %
    iden := [A-Za-z_][A-Za-z_0-9]*

    num  := [0-9]+
    
    comment := #[^\n]*
```

Grammar :
```
    calc := |
        stmt calc

    stmt :=   expr  |
        print expr

    expr :=
        iden = expr |
        expr + expr |
        expr - expr |
        expr / expr |
        expr * expr |
        expr % expr |
        (expr)      |
        - expr      |
        + expr      |
        iden:expr   |
        iden        |
        num
```
