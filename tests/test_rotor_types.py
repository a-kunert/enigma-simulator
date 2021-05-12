import unittest

from RotorTypes import RotorTypes


class MyTestCase(unittest.TestCase):

    def test_it_returns_a_rotor_type_by_name(self):
        result = RotorTypes.get("I")
        self.assertEqual("EKMFL",result["permutation"][0:5])


if __name__ == '__main__':
    unittest.main()
