import alternativeMethod.lookup as lookup
import romanNumerals as rn
import time


if __name__ == "__main__":
    start = time.time()
    num = rn.parse_roman_numeral("MCMXC")
    end = time.time()
    print("parsing: " + str(num))
    print('%f' % (end - start))

    start = time.time()
    num = lookup.parse_roman_numeral("MCMXC")
    end = time.time()
    print("lookup: " + str(num))
    print('%f' % (end - start))
