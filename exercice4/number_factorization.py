def calculate(n):
    def prime_factors(num):
        factors = []
        divisor = 2

        while num > 1:
            while num % divisor == 0:
                factors.append(divisor)
                num //= divisor
            divisor += 1

        return factors

    factors = prime_factors(n)

    if factors:
        return max(factors)
    else:
        return None

result = calculate(13195)
print(result)
