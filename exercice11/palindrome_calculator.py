def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]
    
def calculate():
    palindromic_numbers = []

    for num in range(100, 1000):
        if is_palindrome(num):
            palindromic_numbers.append(num)

    return palindromic_numbers

result = calculate()
print(result)