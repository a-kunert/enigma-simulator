from Letters import Letters
from Permutation import Permutation


class Rotor:

    def __init__(self, permutation=[], notches=None):
        self.permutation = Permutation(permutation)
        self._set_notches(notches)
        self.ring_offset = 0
        self.position_offset = 0
        self.next_rotor = None

    def set_ring_position(self, position):
        self.ring_offset = position - 1
        return self

    def set_position(self, position):
        self.position_offset = (position - 1) % Permutation.length
        return self

    def get_position(self):
        return self.position_offset + 1

    def rotate(self):
        if self.next_rotor and self._will_rotate_next():
            self.next_rotor.rotate()
        self.position_offset += 1
        self.position_offset %= Permutation.length
        return self

    def encrypt(self, letter):
        result = self.perform_single_forward_encryption(letter)
        result = self.next_rotor.encrypt(result)
        result = self.perform_single_backward_encryption(result)
        return result

    def perform_single_forward_encryption(self, letter):
        return self._current_permutation().permute(letter)

    def perform_single_backward_encryption(self, letter):
        return (-self._current_permutation()).permute(letter)

    def assemble(self, rotor):
        rotor.next_rotor = self
        return rotor

    def _current_permutation(self):
        return self.permutation.conjugate_shift(self.ring_offset - self.position_offset)

    def _will_rotate_next(self):
        return self.get_position() in self.notches

    def _set_notches(self, notches):
        if notches is None:
            notches = [k for k in range(1, Permutation.length + 1)]
        if type(notches) is str:
            notches = [Letters.code(letter) for letter in notches]
        self.notches = notches