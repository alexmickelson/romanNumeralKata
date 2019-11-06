import unittest
from typing import List
from parameterized import parameterized
import romanNumerals as rn


class roman_test(unittest.TestCase):

    @parameterized.expand([
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        ("i", 1)
    ])
    def test_numeralToInts(self, numeral: str, expected: int):
        actual = rn.numeral_to_int(numeral)
        self.assertEqual(actual, expected)

    @parameterized.expand([
        (1, [10], "one number has a length of 1"),
        (1, [5, 1], "a large number followed by a smaller one is a numeral"),
        (2, [1, 5], "numbers followed by a larger one are not numerals"),
        (3, [1, 1, 5], "numbers followed by a larger one are not numerals"),
        (4, [1, 1, 1, 5], "numbers followed by a larger one are not numerals"),
        (1, [1000, 100, 1000, 10, 50], "numeral followed by smaller numeral"),
        (2, [100, 1000, 10, 50], "numerals followed by smaller numerals"),
        (1, [1, 1, 1], "numerals can be followed by equal numerals"),
        (1, [5, 1, 5], "numerals before smaller complex numerals have len 1")
    ])
    def test_length_of_next_numeral(self,
                                    length: int,
                                    roman_decimals: List[int],
                                    message: str):
        actual: int = rn.length_of_next_numeral(roman_decimals)
        self.assertEqual(actual, length, message)

    @parameterized.expand([
        (1, [1], "a single number evaluates to itself"),
        (4, [1, 5], "subtracting a single number works"),
        (3, [1, 1, 5], "subtracting multiple values works")
    ])
    def test_simplify_numeral_by_subtraction(
            self,
            expected: int,
            roman_decimals: List[int],
            message: str):
        actual: int = rn.simplify_numeral_by_subtraction(roman_decimals)
        self.assertEqual(actual, expected, message)

    @parameterized.expand([
        (5, "V"),
        (4, "IV"),
        (1990, "MCMXC"),
        (2008, "MMVIII")
    ])
    def test_canParseNumerals(self, expected: int, numerals: str):
        actual = rn.parse_roman_numeral(numerals)
        self.assertEqual(actual, expected)
