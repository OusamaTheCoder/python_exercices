class Matrix:
    """Simple Matrix class."""

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return '\n'.join([(' '.join([str(i) for i in row])) for row in self.matrix])

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        return [row[index] for row in self.matrix]

m1 = Matrix('3 4\n5 6')
print(m1.column(0))

m2 = Matrix('3 4\n5 6\n7 8')
print(m2.column(1))
