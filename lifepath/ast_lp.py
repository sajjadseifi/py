class Node( object ):
    def __init__( self ):
        self.label = "AST"
        self.parent = None
        self.value = dict()
        self.children = []

    def first(self):
        return self.children[0]

class ASTLp( Node ):
    def __init__(self):
        self.label = "lp"
        super().__init__()

class ASTStmt ( Node ):
    def __init__(self):
        self.label = "stmt"
        super().__init__()

#lp
class ASTLp0( ASTLp ):
    def __init__(self):
        super().__init__()

class ASTLp1( ASTLp ):
    def __init__(self,stmt:ASTStmt,lp:ASTLp):
        self.stmt = stmt
        self.lp = lp
        self.children = [stmt,lp]
        super().__init__()

class ASTStmtPush( ASTStmt ):
    def __init__(self,num):
        self.num = num
        self.children  = [num]
        super().__init__()

class ASTStmtMov( ASTStmt ):
    def __init__(self,tar,src):
        self.tar = tar
        self.src = src
        self.children  = [tar,src]
        super().__init__()

class ASTStmtPlus( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtMin( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtMul( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtDiv( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtPer( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtPrint( ASTStmt ):
    def __init__(self):
        super().__init__()