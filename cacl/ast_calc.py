from anytree import NodeMixin
# import uuid
# class ASTNode( NodeMixin ):  
#     def __init__( self, name, id, children=None ):
#         self.name = name
#         self.id = id
#         if children:
#             self.children = children

class Node( object ):
    parent = None
    label = "AST"
    children = []
    def __init__( self ):
        pass

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
    def __init__( self,stmt : ASTStmt,cacl : ASTCalc ):
        ASTCalc.__init__(self)
        self.children = [stmt,cacl]

class ASTStmtExpr( ASTStmt ):
    def __init__( self,expr : ASTExpr ):
        ASTStmt.__init__(self)
        self.children = [expr]

class ASTStmtPrint( ASTStmt ):
    def __init__( self,expr : ASTExpr ):
        ASTStmt.__init__(self)
        self.children = [expr]

class ASTIden( ):
    def __init__( self,name ):
        ASTExpr.__init__(self)
        self.children = [name]

class ASTNum( ASTExpr ):
    def __init__( self,num ):
        ASTExpr.__init__(self)
        self.children = [num]

class ASTExprAss( ASTExpr ):
    def __init__( self,iden : ASTIden,expr : ASTExpr ):
        ASTExpr.__init__(self)
        self.children = [iden,expr]

class ASTExprUnary( ASTExpr ):
    def __init__( self,oprator : str,expr : ASTExpr ):
        ASTExpr.__init__(self)
        self.children = [oprator,expr]

class ASTExprCacluate( ASTExpr ):
    def __init__( self,left : ASTExpr,oprator : str,right : ASTExpr ):
        ASTExpr.__init__(self)
        self.children = [left,oprator,right]

class ASTExprCall( ASTExpr ):
    def __init__( self,iden : ASTIden,expr : ASTExpr ):
        ASTExpr.__init__(self)
        self.children = [iden,expr]
