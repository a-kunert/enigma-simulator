import unittest

from Enigma import Enigma


class MyTestCase(unittest.TestCase):

    def test_is_builds_an_enigma_with_sensible_defaults(self):
        enigma = Enigma()
        self.assertEqual("F", enigma.encrypt("A"))
        self.assertEqual("T", enigma.encrypt("A"))
        self.assertEqual("Z", enigma.encrypt("A"))
        self.assertEqual("M", enigma.encrypt("A"))


if __name__ == '__main__':
    unittest.main()
