def calculate():
    count = 0

    for num in range(100, 1000):
        str_num = str(num)
        if str_num == str_num[::-1]:
            count += 1

    return count

result = calculate()
print(result)
