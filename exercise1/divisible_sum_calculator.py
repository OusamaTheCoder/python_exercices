def calculate():
    limit = 100
    numbers = [num for num in range(limit) if num % 5 == 0 or num % 7 == 0]
    sum_of_numbers = sum(numbers)
    return sum_of_numbers

result = calculate()
print(result)
