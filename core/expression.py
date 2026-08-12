# An expression tree node.
# Every math expression is either:
# - A NUMBER
# - A VARIABLE
# - A BINOP (Binary operator) like +, -, *, /

class Expr:
    pass

class Num(Expr):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class BinOp(Expr):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"
