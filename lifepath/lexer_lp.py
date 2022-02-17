class Lexer:
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
        return tok == None

    def gettoken(self):
        saved = self.file.tell()
        token = self.droptoken()
        self.file.seek(saved,0)
        return token

    def droptoken(self):
        chunk = self.nextch()
        self.seekprev()

        if chunk == '':
            return None
        elif chunk.isspace():
            self.whitespace()
            return self.droptoken()

        elif chunk == "-":
            self.nextch()
            if(self.nextch() == "-"):
                self.comment()
                return self.droptoken()
            else:
                self.seekprev()

        if chunk.isalpha():
            return self.iden()

        elif chunk.isnumeric():
            return self.num()
        else:
            self.seeknext()
            print("lexical error : near token '%s'" % chunk)
            return chunk

    def whitespace(self):
        c = self.nextch()

        while(c.isspace()):
            c = self.nextch()

        if(c != ''):
            self.seekprev()
        
    def comment(self):
        while(self.nextch() != '\n'):
            pass

    def iden(self):
        c = self.nextch()
        tok = ''
        while(c.isalpha()):
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
