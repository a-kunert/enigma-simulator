from Letters import Letters
from Permutation import Permutation


class Plugboard:

    def __init__(self, definition=""):
        self.permutation = Permutation()
        transpositions  = definition.split(" ")
        for transposition in transpositions:
            self.permutation += Permutation(tuple(Letters.code(letter) for letter in transposition))

    def apply(self, letter):
        return self.permutation.permute(letter)
