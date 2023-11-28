def score(word):
    letter_values = {
        ' ': 0,
        'EAIONRTLSU': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10
    }

    total_score = sum(
        value for chars,
        value in letter_values.items()
        for char in word.upper()
        if char in chars)

    return total_score

result1 = score('python')
print(result1)

result2 = score('programming')
print(result2)