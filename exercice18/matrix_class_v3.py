class Matrix:
    """Simple Matrix class."""

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return '\n'.join([(' '.join([str(i) for i in row])) for row in self.matrix])

    def row(self, index):
        return self.matrix[index]

m = Matrix('3 4\n5 6\n7 8')
print(m.row(0))  # Output: [3, 4]
print(m.row(2))  # Output: [7, 8]
