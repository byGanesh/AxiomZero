"""
We define a finite group via its Cayley table.
Check all 4 group axioms before accepting the definition.
"""


class Group:
    def __init__(self, name, elements, cayley_table, identity):
        self.name = name
        self.elements = elements
        self.table = cayley_table
        self.identity = identity

        self._check_axioms()

    def op(self, a, b):
        return self.table[a][b]

    def _check_closure(self):
        for a in self.elements:
            for b in self.elements:
                result = self.op(a, b)
                if result not in self.elements:
                    raise ValueError(
                        f"Closure failed: {a} · {b} = {result}, "
                        f"which is not in {self.name}"
                    )

    def _check_associativity(self):
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    left  = self.op(self.op(a, b), c)
                    right = self.op(a, self.op(b, c))
                    if left != right:
                        raise ValueError(
                            f"Associativity failed: "
                            f"({a}·{b})·{c} = {left}, "
                            f"but {a}·({b}·{c}) = {right}"
                        )

    def _check_identity(self):
        e = self.identity
        if e not in self.elements:
            raise ValueError(f"Identity '{e}' not in elements list.")
        for a in self.elements:
            if self.op(e, a) != a:
                raise ValueError(
                    f"Identity failed (left): e·{a} = {self.op(e,a)}, expected {a}"
                )
            if self.op(a, e) != a:
                raise ValueError(
                    f"Identity failed (right): {a}·e = {self.op(a,e)}, expected {a}"
                )

    def _check_inverses(self):
        e = self.identity
        for a in self.elements:
            found = False
            for b in self.elements:
                if self.op(a, b) == e and self.op(b, a) == e:
                    found = True
                    break
            if not found:
                raise ValueError(
                    f"Inverse missing: no inverse found for '{a}' in {self.name}"
                )

    def _check_axioms(self):
        print(f"Checking axioms for {self.name}...")
        self._check_closure()
        self._check_associativity()
        self._check_identity()
        self._check_inverses()
        print(f"{self.name} is a valid group.\n")


    def inverse_of(self, a):
        e = self.identity
        for b in self.elements:
            if self.op(a, b) == e:
                return b

    def evaluate(self, symbol_list):
        result = self.identity
        for symbol in symbol_list:
            result = self.op(result, symbol)
        return result

    def print_cayley_table(self):
        width = max(len(str(e)) for e in self.elements) + 2
        header = " " * width + " | " + "  ".join(
            str(e).ljust(width) for e in self.elements
        )
        print(header)
        print("-" * len(header))
        for a in self.elements:
            row = str(a).ljust(width) + " | " + "  ".join(
                str(self.op(a, b)).ljust(width) for b in self.elements
            )
            print(row)
