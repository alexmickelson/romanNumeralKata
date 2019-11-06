import re


def parse_roman_numeral(numerals: str) -> int:
    number_pattern = r"^[0-9]+"
    with open("lookup.txt") as lookup:
        for line in lookup:
            if line.endswith('={0}\n'.format(numerals)):
                numbers = re.findall(number_pattern, line)
                return int(numbers[0])
