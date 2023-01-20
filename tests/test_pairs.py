import unittest
import pairs


class TestFindPairs(unittest.TestCase):
    def test_example_input(self):
        numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
        target = 12
        expected_output = set(
            [frozenset([5, 7]), frozenset([12, 0]), frozenset([16, -4])])
        output = pairs.find_pairs(numbers, target)
        self.assertEqual(output, expected_output)

    def test_no_pairs(self):
        numbers = [1, 2, 3, 4]
        target = 10
        expected_output = set()
        output = pairs.find_pairs(numbers, target)
        self.assertEqual(output, expected_output)

    def test_negative_numbers(self):
        numbers = [-5, -3, -2, 0, 5, 7]
        target = 2
        expected_output = set(
            [frozenset([-5, 7]), frozenset([-3, 5])])
        output = pairs.find_pairs(numbers, target)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
