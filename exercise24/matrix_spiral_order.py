from itertools import cycle

def spiral_matrix(size):
    if size < 1:
        raise ValueError('Matrix size must be greater than or equal to 1.')

    matrix = [[0] * size for _ in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_cycle = cycle(directions)
    
    row, col = 0, 0
    direction = next(direction_cycle)

    for num in range(1, size * size + 1):
        matrix[row][col] = num
        next_row, next_col = row + direction[0], col + direction[1]

        if (
            next_row < 0 or next_row >= size
            or next_col < 0 or next_col >= size
            or matrix[next_row][next_col] != 0
        ):
            direction = next(direction_cycle)

        row, col = row + direction[0], col + direction[1]

    return matrix

result1 = spiral_matrix(1)
print(result1)

result2 = spiral_matrix(2)
print(result2)

result3 = spiral_matrix(3)
print(result3)
