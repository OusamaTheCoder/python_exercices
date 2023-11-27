from itertools import groupby

def compress(number):
    compressed_result = [(key, len(list(group))) for key, group in groupby(str(number))]
    return compressed_result

result1 = compress(111)
result2 = compress(1000000)
result3 = compress(10005000)

print(result1)
print(result2)
print(result3)
