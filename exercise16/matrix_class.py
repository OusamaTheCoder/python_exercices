class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        self.matrix = [list(map(int, row.split())) for row in rows]

m1 = Matrix('3 4\n5 6')
print(m1.matrix)

m2 = Matrix('3 4\n5 6\n7 8')
print(m2.matrix)