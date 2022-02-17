# LifePath Interpreter 

<h2>Description IR Code</h2>

```
    PUSH (n) : number push last of stack
    PLUS : replace 2 last element of stack with result of sum
    MIN : replace 2 last element of stack with result of mines
    MULT : replace 2 last element of stack with result of multipy
    DIV : replace 2 last element of stack with result of division
    PRINT : print of last element on stack
    MOV (tar) (src) : set value of source index to target index
```

<h2>Lexical Grammar</h2>

```
    iden := [A-Za-z_]+

    num  := [0-9]+
    
    comment := --[^\n]*
```

<h2>Parser Grammar</h2>

```
    lp := |
        stmt lp
    
    stmt :=
        PUSH num    |
        MOV num num |
        PLUS        |
        MIN         |
        MUL         |
        DIV         |
        PER         |
        PRINT
```

<h2>Code Example</h2>

```
    PUSH 1 --[1]
    PUSH 2 --[1,2]
    PUSH 5 --[1,2,5]
    MIN    --[1,-3]
    PUSH 4 --[1,-3,4]
    PUSH 2 --[1,-3,4,2]
    DIV    --[1,-3,2]
    PRINT  --2
```