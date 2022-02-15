from anytree import NodeMixin
import uuid

class ASTNode(NodeMixin):  
    def __init__(self, name, id, children=None):
        self.name = name
        self.id = id
        if children:
            self.children = children

class Node:
    parent = None
    label = "AST"
    children = []
    def accept(self, visitor, table = None):
        pass
        # return visitor.visit(self)

    def setparent(self, parent):
        self.parent = parent

class ASTCalc(Node):
    label = "calc"

class ASTStmt(Node):
    label = "stmt"

class ASTExpr(Node):
    label = "expr"

class ASTCalc0(ASTCalc):
    def _init__(self):
        pass

class ASTCalc1(ASTCalc):
    def _init__(self,stmt : ASTStmt,cacl : ASTCalc):
        self.children = [stmt,cacl]

class ASTStmtExpr(ASTStmt):
    def _init__(self,expr : ASTExpr):
        self.children = [expr]

class ASTStmtPrint(ASTStmt):
    def _init__(self,expr : ASTExpr):
        self.children = [expr]

class ASTIden(ASTExpr):
    def _init__(self,name):
        self.children = [name]

class ASTNum(ASTExpr):
    def _init__(self,num):
        self.children = [num]

class ASTExprAss(ASTExpr):
    def _init__(self,iden : ASTIden,expr : ASTExpr):
        self.children = [iden,expr]

class ASTExprUnary(ASTExpr):
    def _init__(self,oprator : str,expr : ASTExpr):
        self.children = [oprator,expr]

class ASTExprCacluate(ASTExpr):
    def _init__(self,left : ASTExpr,oprator : str,right : ASTExpr):
        self.children = [left,oprator,right]

class ASTExprCall(ASTExpr):
    def _init__(self,iden : ASTIden,expr : ASTExpr):
        self.children = [iden,expr]
