class Matrix:
    """Simple Matrix class."""

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

m1 = Matrix('4 5\n8 6')
print(m1.__repr__())
