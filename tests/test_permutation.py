import unittest

from Permutation import Permutation


class MyTestCase(unittest.TestCase):

    def test_when_created_from_a_tuple_its_a_cycle(self):
        permutation = Permutation((1, 3, 6))
        self.assertEqual([3, 2, 6, 4, 5, 1], permutation.permutation[:6])

    def test_when_created_from_a_list_it_fills_the_voids(self):
        part = [1, 25, 3, 5]
        permutation = Permutation(part)
        self.assertEqual(part + [2, 4, 6, 7, 8, 9, 10], permutation.permutation[:11])

    def test_it_can_be_initialized_by_a_string(self):
        permutation = Permutation("CbDA")
        self.assertEqual([3, 2, 4, 1, 5], permutation.permutation[0:5])

    def test_it_allows_composition(self):
        left = Permutation([2, 4, 3, 1])
        right = Permutation([4, 1, 2, 3])
        result = left + right
        self.assertEqual([1, 2, 4, 3], result.permutation[:4])

    def test_it_computes_the_inverse(self):
        permutation = Permutation([2, 4, 3, 1])
        result = (-permutation)
        self.assertEqual([4, 1, 3, 2], result.permutation[:4])

    def test_its_possible_to_multiply_it_with_an_integer(self):
        permutation = Permutation([1, 4, 2, 3])
        self.assertEqual([1, 3, 4, 2], (2 * permutation).permutation[:4])
        self.assertEqual([1, 2, 3, 4], (0 * permutation).permutation[:4])
        self.assertEqual([1, 4, 2, 3], (-2 * permutation).permutation[:4])

    def test_its_possible_to_subtract(self):
        first = Permutation([1, 4, 2, 3])
        second = Permutation([2, 3, 1, 4])
        self.assertEqual([2, 1, 4, 3], (first - second).permutation[0:4])

    def test_it_can_be_shifted(self):
        permutation = Permutation([3, 2, 4, 1])
        self.assertEqual([2, 4, 1, 5, 6], permutation.shift().permutation[:5])
        self.assertEqual([26, 3, 2, 4, 1], permutation.shift(-1).permutation[:5])

    def test_it_can_conjugate(self):
        permutation = Permutation([3, 2, 4, 1, 6, 5])
        conjugate = Permutation([1, 6, 2, 4, 3, 5])
        self.assertEqual([2, 4, 5, 1, 3, 6], permutation.conjugate(conjugate).permutation[0:6])

    def test_it_can_shift_conjugate(self):
        permutation = Permutation([5, 3, 1, 8, 7, 2, 4, 6])
        self.assertEqual([1, 2, 3, 8, 6, 4, 11, 10], permutation.conjugate_shift(3).permutation[0:8])


if __name__ == '__main__':
    unittest.main()
