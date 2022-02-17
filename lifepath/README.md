# LifePath Interpreter 

<h2>Description IR Code</h2>

```
    PUSH (n) : number push last of stack
    PLUS : replace 2 last element of stack with result of sum
    MIN : replace 2 last element of stack with result of mines
    MULT : replace 2 last element of stack with result of multipy
    DIV : replace 2 last element of stack with result of division
    PRINT : print of last element on stack
    ST (src) : pop last item and set data to source index 
    LD (src) : get data in source index and push to last element 
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
        LD num      |
        ST num      |
        PLUS        |
        MIN         |
        MUL         |
        DIV         |
        PER         |
        PRINT
```

<h2>Code Example</h2>

```
    PUSH 10 --[10]
    PUSH 5  --[10, 5]
    PUSH 8  --[10, 5, 8]
    PLUS    --[10, 13]
    LD 0    --[10, 13, 10]
    LD 0    --[10, 13, 10, 10]
    MUL     --[10, 13, 100]
    ST 1    --[10, 100]
    LD 2    --[10, 100, 100]
    LD 1    --[10, 100, 100, 100]
    PER     --[10, 100, 0]
    LD 0    --[10, 100, 0, 10]
    PLUS    --[10, 100, 10]
    PRINT   --10 (last element)
```