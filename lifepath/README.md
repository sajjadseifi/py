# LifePath Interpreter 

IR Code Runner For Calculator

# Lexical Grammar
```

    iden := [A-Za-z_]+

    num  := [0-9]+
    
    comment := --[^\n]*

```

# Parser Grammar
```
    lp := |
        stmt lp
    
    stmt :=
        PUSH num   |
        PLUS num   |
        MIN  num   |
        MUL  num   |
        DIV  num   |
        PER  num   |
        PRINT
```

# Code Example 
```
    PUSH 1
    MIN 2
    --division code
    DIV 10
    PRINT
```