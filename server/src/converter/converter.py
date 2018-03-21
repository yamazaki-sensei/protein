import random
from pykakasi import kakasi


__pdb_chars = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
__minimum_length = 50

__kakasi = kakasi()
__kakasi.setMode('H', 'a')
__kakasi.setMode('K', 'a')
__kakasi.setMode('J', 'a')
__converter = __kakasi.getConverter()


def convert(src):
    converted = __converter.do(src).upper()
    result = ''
    while len(result) < __minimum_length:
        for i in range(0, len(converted)):
            char = converted[i]
            if char in __pdb_chars:
                result += char
                continue

            result += random.choice(__pdb_chars)

    return result
