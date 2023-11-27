from itertools import groupby

def compress(number):
    compressed_result = [f"{key}{len(list(group))}" for key, group in groupby(str(number))]
    result_string = '_'.join(compressed_result)
    return result_string

result1 = compress(100000)
result2 = compress(9993330)
result3 = compress(6540000)

print(result1)
print(result2)
print(result3)
