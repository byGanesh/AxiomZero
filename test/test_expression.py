from core.expression import Num, Var, BinOp
from core.rules import RULES, RULE_NAMES


def try_all_rules(expr):
    """Try every rule on an expression. Print what applies."""
    print(f"\nExpression: {expr}")
    any_applied = False
    for i, rule in enumerate(RULES):
        result = rule(expr)
        if result is not None:
            print(f"  Rule {i} '{RULE_NAMES[i]}' → {result}")
            any_applied = True
    if not any_applied:
        print(f"  No rules apply.")


# --- Test each rule fires correctly ---

try_all_rules(BinOp('+', Var('x'), Num(0)))       # rule 0 should fire
try_all_rules(BinOp('+', Num(0), Var('x')))       # rule 1 should fire
try_all_rules(BinOp('*', Var('x'), Num(1)))       # rule 2 should fire
try_all_rules(BinOp('*', Num(1), Var('x')))       # rule 3 should fire
try_all_rules(BinOp('*', Var('x'), Num(0)))       # rule 4 should fire
try_all_rules(BinOp('*', Num(0), Var('x')))       # rule 5 should fire
try_all_rules(BinOp('-', Var('x'), Var('x')))     # rule 6 should fire
try_all_rules(BinOp('-', Var('x'), Num(0)))       # rule 7 should fire

# --- Test a nested expression ---
# ((x + 0) * (y - y))
# rules won't fire at the TOP level (it's a * not a + or -)
# but sub-expressions ARE simplifiable
nested = BinOp('*',
    BinOp('+', Var('x'), Num(0)),
    BinOp('-', Var('y'), Var('y'))
)
try_all_rules(nested)   # no top-level rule fires — notice this
