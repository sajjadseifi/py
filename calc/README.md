# Cacluator Interpreter

Lexical : 
```
        
    oprator :=    + |
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
    b = a * a
    c = rad:b
    print c % b + a
```
Interpreter Output :
```
    assign -> a = 10
    calculate -> 20 = 10 + 10
    assign -> b = 20
    calculate -> 100 = 10 * 10
    assign -> b = 100
    call -> rad(10.0)
    assign -> c = 10.0
    calculate -> 10 = 10 % 100
    calculate -> 20 = 10 + 10
    print -> 20
```

Compiler Output :
```
    PUSH 10
    PUSH 5
    PUSH 8
    PLUS
    LD 0
    LD 0
    MUL
    ST 1
    LD 2
    LD 1
    PER
    LD 0
    PLUS
    PRINT
```
