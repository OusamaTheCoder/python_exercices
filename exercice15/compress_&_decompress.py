from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)
    
def decompress(compressed_string):
    decompressed_number = ''
    pairs = compressed_string.split('_')

    for pair in pairs:
        digit, count = pair[0], int(pair[1:])
        decompressed_number += digit * count

    return int(decompressed_number)

result1 = decompress('14_53_22_51_02')
result2 = decompress('11_03_51_03')

print(result1)
print(result2)
