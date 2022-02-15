from anytree import NodeMixin
# import uuid
# class ASTNode( NodeMixin ):  
#     def __init__( self, name, id, children=None ):
#         self.name = name
#         self.id = id
#         if children:
#             self.children = children

class Node( object ):
    def __init__( self ):
        self.label = "AST"
        self.parent = None
        self.value = dict()
        self.children = []

    def accept( self, visitor, table = None ):
        pass
        # return visitor.visit( self )

    def setparent( self, parent ):
        self.parent = parent

class ASTCalc( Node ):
    label = "calc"
    def __init__( self ):
        Node.__init__(self)

class ASTStmt( Node ):
    label = "stmt"
    def __init__( self ):
        Node.__init__(self)

class ASTExpr( Node ):
    label = "expr"
    def __init__( self ):
        Node.__init__(self)

class ASTCalc0( ASTCalc ):
    def __init__( self ):
        ASTCalc.__init__(self)

class ASTCalc1( ASTCalc ):
    def __init__( self,stmt : ASTStmt,calc : ASTCalc ):
        ASTCalc.__init__(self)
        self.stmt = stmt
        self.calc = calc
        self.children = [stmt,calc]

class ASTStmtExpr( ASTStmt ):
    def __init__( self,expr : ASTExpr ):
        ASTStmt.__init__(self)
        self.expr = expr
        self.children = [expr]

class ASTStmtPrint( ASTStmt ):
    def __init__( self,expr : ASTExpr ):
        ASTStmt.__init__(self)
        self.expr = expr
        self.children = [expr]

class ASTIden( ):
    def __init__( self,name ):
        ASTExpr.__init__(self)
        self.name = name
        self.children = [name]

class ASTNum( ASTExpr ):
    def __init__( self,num ):
        ASTExpr.__init__(self)
        self.num = num
        self.children = [num]

class ASTExprAss( ASTExpr ):
    def __init__( self,iden : ASTIden,expr : ASTExpr ):
        ASTExpr.__init__(self)
        self.iden = iden
        self.expr = expr
        self.children = [iden,expr]

class ASTExprUnary( ASTExpr ):
    def __init__( self,oprator : str,expr : ASTExpr ):
        ASTExpr.__init__(self)
        self.oprator = oprator
        self.expr = expr
        self.children = [oprator,expr]

class ASTExprCacluate( ASTExpr ):
    def __init__( self,left : ASTExpr,oprator : str,right : ASTExpr ):
        ASTExpr.__init__(self)
        self.left = left
        self.oprator = oprator
        self.right = right
        self.children = [left,oprator,right]

class ASTExprCall( ASTExpr ):
    def __init__( self,iden : ASTIden,expr : ASTExpr ):
        ASTExpr.__init__(self)
        self.iden = iden
        self.expr = expr
        self.children = [iden,expr]
