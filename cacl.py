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

    expr := expr-unary

    unary-oprator := + |
                     - 

    expr-unary := expr-priority-0  |
        unary-oprator expr         |

    expr-priority-0 :=    expr-priority-1 |
        expr-priority-0 + expr-priority-1 |
        expr-priority-0 - expr-priority-1     

    expr-priority-1 :=  expr-priority-1 |
        expr-priority-1 / expr-capsol   |
        expr-priority-1 * expr-capsol   |
        expr-priority-1 % expr-capsol 

    expr-capsol := expr-prim |
        (expr)      

    expr-prim :=    |
        iden expr   |
        iden        |
        num
'''
unary = ["-","+"]
priority0 = ["-","+"]
priority1 = ["*","/","%"]
keywords = ["rad","sin","cos","cot","tan"]

class Parser:
    def __init__(self,lexer):
        self.lexer = Lexer("")
    def nextg(self):
        return self.lexer.gettoken().text    

    def nextd(self):
        return self.lexer.droptoken().text
    
    def infollow(self,toks):
        flw = self.nextg()
        
        if not isinstance(toks, list):
            return flw == toks

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
        
        if self.nextg() == "print":
            self.expr()
        else:
            self.ass()
        
    def ass(self):
        iden = self.nextd()

        if not iden.isidentifier():
            print("syntax error : expected identifier")
        
        if self.nextd() != "=":
            print("syntax error : expected =")

        expr = self.expr()

    def expr(self):
        self.exprunary()

    def unaryoprator(self):
        isun = False
        while self.infollow(unary):
            isun = True
            self.unaryoprator()
        
        return isun

    def exprunary(self):
        expr = None
        if self.unaryoprator():
            expr = self.expr()
        else:
            expr = self.exprpriority0()

    def exprpriority0(self):
        expr1 = self.exprpriority1()

        if self.infollow(priority0):
            opr = self.nextd()
            expr2 = self.exprpriority1()

    def exprpriority1(self):
        expr1 = self.exprcabsol()

        if self.infollow(priority1):
            opr = self.nextd()
            expr2 = self.exprcabsol()

    def exprcabsol(self):
        if not self.infollow("("):
            expr = self.exprprim()
        else:
            self.nextd()
            expr = self.expr()

            if self.infollow(")"):
                self.nextd()
            else:
                print("syntax error : expected )")

    def exprprim(self):
        if(self.nextg().isnumeric()):
            return self.nextd()
        elif(self.nextg().isidentifier()):
            iden = self.nextd()
            for k in keywords:
                if iden == k:
                    expr = self.expr()

            return iden
        else:
            return None
#compiler
lex = Lexer("./test/0")

while True:
    t = lex.droptoken()
    if not t.text:
        break
    print("token : %s" % t.text)
