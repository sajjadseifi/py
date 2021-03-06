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
    PUSH 7  --[7]
    PUSH 3  --[7, 3]
    PUSH 8  --[7, 3, 8]
    PLUS    --[7, 11]
    LD   0  --[7, 11, 7]
    LD   0  --[7, 11, 7, 7]
    MUL     --[7, 11, 49]
    ST   1  --[7, 49]
    LD   1  --[7, 49, 49]
    LD   2  --[7, 49, 49, 49]
    LD   1  --[7, 49, 49, 49, 49]
    PER     --[7, 49, 49, 0]
    LD   0  --[7, 49, 49, 0, 7]
    PLUS    --[7, 49, 49, 7]
    PRINT   --7 (last of element)
```