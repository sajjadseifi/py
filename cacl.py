# Grammar Calculator
'''
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
        - expr      |
        iden        |
        num

    iden := [A-Za-z_][A-Za-z_0-9]*

    num  := [0-9]+
    
    comment := #[^\n]*
'''
#Lexical
from math import fabs
import re
import this

#regex
idpat = re.compile('/^[A-Za-z_][A-Za-z_0-9]*$/')
numpat = re.compile('/^[0-9]+$/')

class Token:
    def __init__(self, text,line,offset):
        self.text = text
        self.line = line
        self.offset = offset
    
class Lexer:
    new_line = False
    line = 1
    offset = 0
    def __init__(self, file):
        self.file = open(file,'r')
    
    def seekprev(self):
        tel = self.file.tell()
        self.file.seek(tel-1,0)

    def seeknext(self):
        self.nextch()
    
    def nextch(self):
        c = self.file.read(1)
        return c 
    def eof(self):
        tok = self.gettoken()
        return tok.text == None

    def gettoken(self):
        saved = self.file.tell()
        token = self.droptoken()
        self.file.seek(saved,0)
        return token

    def droptoken(self):
        chunk = self.nextch()
        self.seekprev()
        self.offset = self.file.tell()  
        tok = ''
        if chunk.isspace():
            self.whitespace()
            return self.droptoken()
        elif chunk == "#":
            self.comment()
            return self.droptoken()
        if chunk.isalpha():
            tok = self.iden()
        elif chunk.isnumeric():
            tok = self.num()
        elif chunk == '':
            return Token(None,self.line,self.offset)
        else:
            self.seeknext()
            tok = chunk

        return Token(tok,self.line,self.offset)

    def whitespace(self):
        c = self.nextch()
        while(c .isspace()):
            c = self.nextch()

        self.seekprev()
    def comment(self):
        c = ''

        while(c != '\n'):
            c = self.nextch()

    def iden(self):
        c = self.nextch()   
        if not c.isalpha():
            self.seekprev()    
            return 

        tok = ''
        while(c.isalpha() or c.isnumeric()):
            tok += c
            c = self.nextch()
        
        if(c != ''):
            self.seekprev()
        return tok

    def num(self):
        tok = ''
        c = self.nextch()

        while(c.isnumeric()):
            tok += c
            c = self.nextch()

                
        if(c != ''):
            self.seekprev()

        return tok

#Parser
'''
    Resolve Ambiguity

    expr :=             |
        expr-math       |
        expr-priority-0 |
        expr-capsol     |
        expr-unary      |
        expr-prim

    expr-math :=
        rad expr    |
        sin expr    |
        cos expr    |
        tan expr    |
        cot expr    
    
    expr-priority-0 :=         |
        expr-priority-0 + expr |
        expr-priority-0 - expr     

    expr-priority-1 :=      |
        expr / expr         |
        expr * expr         |
        expr % expr 

    expr-capsol :=  |
        (expr)      

    expr-unary :=   |
        - expr-prim |
        + expr-prim 

    expr-prim :=    |
        iden        |
        num
'''

class Parser:
    def __init__(self,lexer):
        self.lexer = Lexer("")
    def next(self,ignored):
        if ignored:
            self.lexer.gettoken().text
        else: 
            self.lexer.droptoken().text
    
    def infollow(self,toks):
        flw = self.next(True)
        for tok in toks:
            if flw == tok:
                return True
        
        return False

    def calc(self):
        if self.lexer.eof():
            return

        self.stmt()
        self.calc()        
    
    def stmt(self):
        
        if self.next(True) == "print":
            self.expr()
        else:
            self.ass()
        
    def ass(self):
        iden = self.next()

        if not iden.isidentifier():
            print("syntax error : expected identifier")
        
        if self.next() != "=":
            print("syntax error : expected =")

        expr = self.expr()

    def expr(self):

        pass

    def exprmath(self):
        pass
    
    def exprpriority0(self):
        pass

    def exprpriority1(self):
        pass

    def exprcabsol(self):
        pass

    def exprunary(self):
        pass

    def exprprim(self):
        pass

#compiler
lex = Lexer("./test/0")

while True:
    t = lex.droptoken()
    if not t.text:
        break
    print("token : %s" % t.text)
