from itertools import groupby

def compress(number):
    compressed_result = [f"{key}{'.' * len(list(group))}" for key, group in groupby(str(number))]
    result_string = ''.join(compressed_result)
    return result_string

result1 = compress(1000040000)
result2 = compress(20000000)
result3 = compress(123456)

print(result1)
print(result2)
print(result3)
