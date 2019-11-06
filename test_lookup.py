import unittest
from parameterized import parameterized
import alternativeMethod.lookup as lookup


class lookup_test(unittest.TestCase):
    @parameterized.expand([
        (5, "V"),
        (4, "IV"),
        (1990, "MCMXC"),
        (2008, "MMVIII")
    ])
    def test_canParseNumerals(self, expected: int, numerals: str):
        actual = lookup.parse_roman_numeral(numerals)
        self.assertEqual(actual, expected)
