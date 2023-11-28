def get_slices(sequence, length):
    if length < 1:
        raise ValueError('The length cannot be less than 1.')
    if length > len(sequence):
        raise ValueError('The length cannot be greater than sequence.')

    return [sequence[i:i + length] for i in range(len(sequence) - length + 1)]

result1 = get_slices('esmartdata', 5)
print(result1)

result2 = get_slices('654646849173', 6)
print(result2)
