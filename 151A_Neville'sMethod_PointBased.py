"""
The following program applies Neville's Method to generate the solutions of a polynomial interpolating a given number
of points. The number of points "(x, y)" can be modified in the "initial_points" list below. The function "Neville" will
use these points to create an interpolating polynomial through all the given points, and output the y-value of the final
interpolated polynomial.
"""


initial_points = [(0, 1), (0.25, 1.64872), (0.5, 2.71828), (0.75, 4.48169)]
initial_matrix = []
for i in range(len(initial_points)):
    initial_matrix.append([0] * len(initial_points))
for index, point in enumerate(initial_points):
    initial_matrix[0][index] = point[1]


def Neville(x):
    iteration = 1
    while iteration < len(initial_points):
        for iter_index in range(len(initial_matrix[iteration]) - iteration):
            initial_matrix[iteration][iter_index] = (((x - initial_points[iter_index + iteration][0]) *
                                                     initial_matrix[iteration - 1][iter_index]) -
                                                     ((x - initial_points[iter_index][0]) *
                                                     initial_matrix[iteration - 1][iter_index + 1])) / \
                                                    (initial_points[iter_index][0] -
                                                     initial_points[iter_index + iteration][0])
        iteration += 1
    return f'Approximation Using Neville\'s Method with {len(initial_points)} points is {initial_matrix[-1][0]}'


print(Neville(0.43))
