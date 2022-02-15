# Grammar Calculator
'''
    calc := |
        body calc

    body :=     |
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

    iden := [A-Za-z_][A-Za-z_0-9]*

    num  := [0-9]+
    
    comment := #[^\n]*
'''
#Lexical
import re

#regex
idpat = re.compile('/^[A-Za-z_][A-Za-z_0-9]*$/')
numpat = re.compile('/^[0-9]+$/')

class Lexer:
    def __init__(self, file):
        self.file = open(file,'r')
    
    def seekprev(self):
        tel = self.file.tell()
        self.file.seek(tel-1,0)

    def seeknext(self):
        self.nextch()
    
    def nextch(self):
        return self.file.read(1)

    def gettoken(self):
        saved = self.file.tell()
        token = self.droptoken()
        self.file.seek(saved,0)
        return token

    def droptoken(self):
        chunk = self.nextch()
        self.seekprev()

        if(chunk.isspace()):
            self.whitespace()
            return self.droptoken()
        elif(chunk.isalpha()):
            return self.iden()
        elif(chunk.isnumeric()):
            return self.num()
        elif(chunk == "#"):
            self.comment()
            return self.droptoken()
        elif(chunk == ''):
            self.seeknext()
            return chunk
        else:
            self.seeknext()
            return chunk

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


#compiler
lex = Lexer("./test/0")

while True:
    t = lex.droptoken()
    if not t:
        break
    print("token : %s" % t)