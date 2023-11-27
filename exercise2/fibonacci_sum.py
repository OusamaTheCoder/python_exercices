def calculate():
    limit = 1000000
    fibonacci_sequence = [0, 1]
    
    while True:
        next_element = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_element >= limit:
            break
        fibonacci_sequence.append(next_element)
    
    even_elements = [num for num in fibonacci_sequence if num % 2 == 0]
    sum_of_even_elements = sum(even_elements)
    
    return sum_of_even_elements

result = calculate()
print(result)
