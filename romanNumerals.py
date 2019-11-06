from typing import List


def parse_roman_numeral(numerals: str) -> int:
    roman_decimals: List[int] = list(map(numeral_to_int, numerals))
    simple_decimals: List[int] = simplify_decimal_list(roman_decimals)
    return sum(simple_decimals)


def numeral_to_int(numeral: str) -> int:
    numeral = numeral.upper()
    numeralMap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    return numeralMap[numeral]


def simplify_decimal_list(roman_decimals: List[int]) -> List[int]:
    simple_decimals: List[int] = []
    while (len(roman_decimals) > 0):
        numeral_end_index = length_of_next_numeral(roman_decimals)

        simple_number = simplify_numeral_by_subtraction(
                            roman_decimals[0:numeral_end_index])
        simple_decimals.append(simple_number)

        roman_decimals = roman_decimals[numeral_end_index: len(roman_decimals)]
    return simple_decimals


def length_of_next_numeral(roman_decimals: List[int]) -> int:
    if (roman_decimals[0] >= max(roman_decimals)):
        return 1
    else:
        return roman_decimals.index(max(roman_decimals))+1


def simplify_numeral_by_subtraction(roman_decimals: List[int]) -> int:
    if(len(roman_decimals) == 1):
        return roman_decimals[0]

    calculated_value: int = max(roman_decimals)
    roman_decimals.remove(calculated_value)

    for number in roman_decimals:
        calculated_value -= number

    return calculated_value


if __name__ == "__main__":
    pass
