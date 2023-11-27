# Exercise 18

Consider the problem below. We have an application in which at some point we get a matrix in the form of a string (an object of the str type). For example, the following string:

``````
1 |   string = """4 2 7
2 |   1 5 4
3 |   2 6 8"""
``````

represents a 3x3 matrix. Each row of the matrix is stored on a separate line. Each element of a row is separated from another element by a space.

It's hard to work with these matrices and perform some additional operations. We will transform such a matrix into nested lists:

``````
    [[4, 2, 7], [1, 5, 4], [2, 6, 8]]
``````

Part of a class named Matrix is implemented:

``````
1  | class Matrix:
2  |     """Simple Matrix class."""
3  |  
4  |     def __init__(self, string):
5  |         self.matrix = [
6  |             [int(i) for i in row.split()]
7  |             for row in string.splitlines()
8  |         ]
9  |  
10 |      def __repr__(self):
11 |         return '\n'.join(
12 |            [
13 |               (' '.join([str(i) for i in row]))
14 |                 for row in self.matrix
15 |              ]
16 |          )
``````

Add an implementation of the `row()` method to the Matrix class that takes the index as an argument and returns the corresponding row of the matrix.


# Example:

``````
    [IN]: m = Matrix('3 4\n5 6\n7 8')
    [IN]: m.row(0)
    [OUT]: [3, 4]
``````

# Example:

``````
    [IN]: m = Matrix('3 4\n5 6\n7 8')
    [IN]: m.row(2)
    [OUT]: [7, 8]
``````

You only need to implement the `row()` method. The tests run several test cases to validate the solution.