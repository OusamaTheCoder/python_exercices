def is_prime(n):

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True
    
def calculate():
    position = 100
    count_primes = 0
    number = 1

    while count_primes < position:
        number += 1
        if is_prime(number):
            count_primes += 1

    return number

result = calculate()
print(result)