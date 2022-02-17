class IR:
    def __init__(self,path) -> None:
        self.idxstk = 0
        self.out = open(path,"w+")

    def up(self):
        self.idxstk +=1
    def down(self):
        self.idxstk -=1

    def w(self,s:str):
        self.out.write("%s\n" % s)
    
    def push(self,num):
        self.w("PUSH %s" % num)

    def mov(self,tar,src):
        self.w("MOV %s %s" % (tar,src))
    
    def print(self):
        self.w("PRINT")
    
    def plus(self):
        self.w("PLUS")
    
    def min(self):
        self.w("MIN")
    
    def div(self):
        self.w("DIV")
    
    def mul(self):
        self.w("MUL")
    
    def per(self):
        self.w("PER")
