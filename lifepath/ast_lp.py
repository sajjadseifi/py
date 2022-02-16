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
        super().__init__()

class ASTStmt ( Node ):
    def __init__(self):
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


