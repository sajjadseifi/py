class IR:
    def __init__(self,path) -> None:
        self.idxstk = 0
        self.out = open(path,"w+")
        self.out.flush()

    def finished(self):
        self.out.close()

    def up(self):
        self.idxstk +=1
    def down(self):
        self.idxstk -=1

    def w(self,s:str):
        self.out.write("%s\n" % s)
    
    def push(self,num):
        self.w("PUSH %s" % num)
        self.up()
    
    def load(self,src):
        self.w("LD %s" % (src))
    
    def store(self,src):
        self.w("ST %s" % (src))
    
    def print(self):
        self.w("PRINT")
        self.down()
    
    def plus(self):
        self.w("PLUS")
        self.down()
    
    def min(self):
        self.w("MIN")
        self.down()
    
    def div(self):
        self.w("DIV")
        self.down()
    
    def mul(self):
        self.w("MUL")
        self.down()
    
    def per(self):
        self.w("PER")
        self.down()
