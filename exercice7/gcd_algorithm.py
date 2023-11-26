def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

result = greatest_common_divisor(32, 48)
print(result)
