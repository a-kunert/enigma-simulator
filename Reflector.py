from Rotor import Rotor


class Reflector(Rotor):

    def rotate(self):
        pass

    def encrypt(self, letter):
        return self.permutation.permute(letter)
