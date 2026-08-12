from core.expression import Num, Var, BinOp

e1 = BinOp('+', Var('x'), Num(0))
print(e1)

e2 = BinOp('*', Var('x'), Num(1))
print(e2)

e3 = BinOp(
    "*",
    BinOp('+', Var('x'),Num(0)),
    BinOp('-', Var('y'), Num(4)),
)
print(e3)
