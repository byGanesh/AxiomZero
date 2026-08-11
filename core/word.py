# A Word is a sequence of generator symbols.
# Example: ['a', 'a', 'a2', 'a'] in Z3
#
# The GOAL of AxiomZero is to reduce a word to the empty list [] using valid algebraic rules, because [] means identity.
# The only rule we implement:
#     Cancel adjacent inverses: if symbol[i] and symbol[i+1] are
#     inverses of each other, remove both.
#     e.g. a · a^-1 -> (nothing)


class Word:
    def __init__(self, symbols, group):
        self.symbols = list(symbols)
        self.group = group

    def is_identity(self):
        return self.group.evaluate(self.symbols) == self.group.identity

    def is_empty(self):
        return len(self.symbols) == 0

    def get_valid_moves(self):
        valid = []
        for i in range(len(self.symbols) - 1):
            a = self.symbols[i]
            b = self.symbols[i + 1]
            if self.group.inverse_of(a) == b:
                valid.append(i)
        return valid

    def apply_move(self, position):
        new_symbols = (
            self.symbols[:position] +
            self.symbols[position + 2:]
        )
        return Word(new_symbols, self.group)

    def __repr__(self):
        if not self.symbols:
            return "[ e ]"
        return "[ " + " · ".join(self.symbols) + " ]"

    def __len__(self):
        return len(self.symbols)
