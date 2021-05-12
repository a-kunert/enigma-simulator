import unittest

from Letters import Letters


class MyTestCase(unittest.TestCase):

    def test_letters_returns_code(self):
        self.assertEqual(2, Letters.code('B'))
        self.assertEqual(2, Letters.code('b'))

    def test_letters_returns_letter(self):
        self.assertEqual('C', Letters.char(3))

    def test_nothing_happens_is_code_is_already_an_integer(self):
        self.assertEqual(3, Letters.code(3))


if __name__ == '__main__':
    unittest.main()
