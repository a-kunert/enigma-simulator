import unittest

from Plugboard import Plugboard


class MyTestCase(unittest.TestCase):

    def test_when_given_a_definition_it_flips_the_contained_letters(self):
        plugboard = Plugboard("AE XZ LS")
        self.assertEqual("X", plugboard.apply("Z"))

    def test_it_performs_an_involution(self):
        plugboard = Plugboard("AE XZ LS")
        self.assertEqual("Z", plugboard.apply("X"))

    def test_when_given_a_definition_it_leaves_the_other_letters_untouched(self):
        plugboard = Plugboard("AE XZ LS TV")
        self.assertEqual("U", plugboard.apply("U"))


if __name__ == '__main__':
    unittest.main()
