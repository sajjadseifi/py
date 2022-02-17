#Symbols Table[name,value]
class Symbols:
    tbl = dict()

    def get(self,name):
        return self.tbl.get(name) 
    def put(self,name,value):
        self.tbl[name] = value

    def rm(self,name):
        self.tbl.pop(name)
        pass

    def exist(self,name):
        return self.tbl[name] != None
