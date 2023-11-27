def hamming_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError('Both vectors must be the same length.')

    return sum(bit1 != bit2 for bit1, bit2 in zip(vector1, vector2))

try:
    result1 = hamming_distance('01101010', '11011011')
    print(result1)
except ValueError as e:
    print(e)

try:
    result2 = hamming_distance('110', '10100')
    print(result2)
except ValueError as e:
    print(e)
