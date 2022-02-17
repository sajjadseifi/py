# Cacluator Interpreter

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
Example Code :
```
    a = 10
    b = (10 + 10)
    c = rad:b
    print c % b + a
```
Interpreter Output :
```
    ass -> a = 10
    calc -> 20 = 10 + 10
    ass -> b = 20
    call -> rad(1)
    ass -> c = 1
    calc -> 1 = 1 % 20
    calc -> 11 = 1 + 10
    print -> 11
```

Compiler Output :
```
    PUSH 10
    PUSH 10
    PUSH 10
    PLUS
    MOV 3 0
    MOV 4 0
    MUL
    MOV 1 2
    MOV 4 2
    MOV 5 1
    PER
    MOV 5 0
    PLUS
    PRINT
```
