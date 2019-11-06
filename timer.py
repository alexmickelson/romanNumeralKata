import romanNumerals as rn
import alternativeMethod.lookup as lookup
import alternativeMethod.lookupInMemory as mem_lookup
import time


if __name__ == "__main__":
    start = time.time()
    num = rn.parse_roman_numeral("MCMXC")
    end = time.time()
    print("parsing: " + str(num))
    print('second: %.10f' % (end - start))

    start = time.time()
    num = lookup.parse_roman_numeral("MCMXC")
    end = time.time()
    print("lookup: " + str(num))
    print('second: %.10f' % (end - start))

    start = time.time()
    num = mem_lookup.parse_roman_numeral("MCMXC")
    end = time.time()
    print("lookup from memory: " + str(num))
    print('second: %.10f' % (end - start))
