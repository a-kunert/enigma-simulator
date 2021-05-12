import unittest

from Rotor import Rotor


class MyTestCase(unittest.TestCase):

    def test_it_encrypts_a_single_letter_in_base_position(self):
        rotor = Rotor("EKMFLGD")
        self.assertEqual("K", rotor.perform_single_forward_encryption("b"))

    def test_it_encrypts_a_single_letter_when_the_ring_is_shifted(self):
        rotor = Rotor("EKMFLGD").set_ring_position(5)
        self.assertEqual("O", rotor.perform_single_forward_encryption("f"))

    def test_it_encrypts_a_single_letter_when_the_rotor_rotated(self):
        rotor = Rotor("EKMFLG").set_position(4)
        self.assertEqual("C", rotor.perform_single_forward_encryption("A"))

    def test_it_can_rotate(self):
        rotor = Rotor().set_position(4)
        rotor.rotate()
        self.assertEqual(5, rotor.get_position())

    def test_it_allows_assembly_to_a_rotor_array(self):
        left_rotor = Rotor()
        middle_rotor = Rotor()
        right_rotor = Rotor()
        left_rotor.assemble(middle_rotor).assemble(right_rotor)
        self.assertEqual(middle_rotor, right_rotor.next_rotor)
        self.assertEqual(left_rotor, right_rotor.next_rotor.next_rotor)

    def test_if_the_rotor_hits_a_notch_it_rotates_the_next_rotor(self):
        left_rotor = Rotor(notches=[])
        right_rotor = Rotor(notches="B")
        rotors = left_rotor.assemble(right_rotor)
        self.assertEqual(1, left_rotor.get_position())
        rotors.rotate()
        self.assertEqual(1, left_rotor.get_position())
        rotors.rotate()
        self.assertEqual(2, left_rotor.get_position())


if __name__ == '__main__':
    unittest.main()
