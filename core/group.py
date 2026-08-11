# Group definition
# A group is defined by:
# 1. A set of named generators
# 2. A multiplication table (Cayley table) that defines the group operation
# 3. The identity element
#
# Here we represent elements as strings for readability

class Group:
    def __init__(self, name, elements, cayley_table, identity):
        self.name = name
        self.elements = elements
        self.table = cayley_table
        self.identity = identity

    def __validate(self):
        e = self.identity
        for a in self.elements:
            assert self.op(e,a) == a, f"Identity failed: e.{a} != {a}"
            assert self.op(a,e) == a, f"Identity failed: {a}.e != {a}"

    def op(self, a, b):
        assert a in self.elements, f"'{a}' not in group {self.name}"
        assert b in self.elements, f"'{b}' not in group {self.name}"
        return self.table[a][b]

    def inverse_of(self, a):
        e = self.identity
        for b in self.elements:
            if self.op(a,b) == e:
                return b
        raise ValueError(f"No inverse found for '{a}' in {self.name}")

    def evaluate(self, word_list):
        res = self.identity
        for symbol in word_list:
            res = self.op(res, symbol)
        return res

    def __repr__(self):
        return f"Group({self.name}, {len(self.elements)} elements)"
