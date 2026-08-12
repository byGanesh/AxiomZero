# Simplification rules. Each rule is a function:
# rule(expr) -> Expr or None
#
# If the rule applies, it returns the simplified expression.
# If not, it returns None.
#
# These are the ACTIONS available to the RL agent.
#

from core.expression import Expr, Num, Var, BinOp

def rule_add_zero_right(expr):
    # x + 0 -> x
    if(isinstance(expr, BinOp) and expr.op == "+"
        and isinstance(expr.right, Num)
        and expr.right.value == 0):
        return expr.left
    return None

def rule_add_zero_left(expr):
    # 0 + x -> x
    if(isinstance(expr, BinOp)
            and expr.op == "+"
            and isinstance(expr.left, Num)
            and expr.left.value == 0):
        return expr.right
    return None

def rule_mul_one_right(expr):
    # x * 1 -> x
    if(isinstance(expr, BinOp)
        and expr.op == "*"
        and isinstance(expr.right, Num)
        and expr.right.value == 1
    ):
        return expr.left
    return None

def rule_mul_one_left(expr):
    # 1 * x -> x
    if(isinstance(expr, BinOp)
            and expr.op == "*"
            and isinstance(expr.left, Num)
            and expr.left.value == 1
    ):
        return expr.right
    return None

def rule_mul_zero_right(expr):
    # x * 0 -> 0
    if (isinstance(expr, BinOp)
            and expr.op == "*"
            and isinstance(expr.right, Num)
            and expr.right.value == 0
    ):
        return Num(0)
    return None

def rule_mul_zero_left(expr):
    # 0 * x -> 0
    if(isinstance(expr, BinOp)
            and expr.op == "*"
            and isinstance(expr.right, Num)
            and expr.left.value == 0
    ):
        return Num(0)
    return None

def rule_sub_self(expr):
    # x - x -> 0
    if(isinstance(expr, BinOp)
        and expr.op == "-"
        and expr.left == expr.right
    ):
        return Num(0)
    return None

def rule_sub_zero(expr):
    # x - 0 -> x
    if(isinstance(expr, BinOp)
            and expr.op == "-"
            and isinstance(expr.right, Num)
            and expr.right.value == 0
    ):
        return expr.left
    return None

# Rule registry (action 0 - 7)
RULES = [
    rule_add_zero_right,
    rule_add_zero_left,
    rule_mul_one_right,
    rule_mul_one_left,
    rule_mul_zero_right,
    rule_mul_zero_left,
    rule_sub_self,
    rule_sub_zero,
]

RULE_NAMES = [
    "x + 0 -> x",
    "0 + x -> x",
    "x * 1 -> x",
    "1 * x -> x",
    "x * 0 -> 0",
    "0 * x -> 0",
    "x - x -> 0",
    "x - 0 -> x",
]
