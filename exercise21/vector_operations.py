def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1
    return distance
    
def hamming_weight(vector):
    zero_vector = '0' * len(vector)
    return hamming_distance(vector, zero_vector)

result1 = hamming_weight('110001010')
print(result1)

result2 = hamming_weight('110111')
print(result2)