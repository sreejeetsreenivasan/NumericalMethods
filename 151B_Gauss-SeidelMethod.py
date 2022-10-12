import copy
import math
import numpy
from matplotlib import pyplot as plt


set_of_points = []
A = [[4, -1, 0, -1, 0, 0], [-1, 4, -1, 0, -1, 0], [0, -1, 4, 0, 0, -1],
     [-1, 0, 0, 4, -1, 0], [0, -1, 0, -1, 4, -1], [0, 0, -1, 0, -1, 4]]
A_array = numpy.asarray(A)
b = [2, 1, 2, 2, 1, 2]
x_0 = [0, 0, 0, 0, 0, 0]
iteration = 0
tolerance = 0.01
list_of_r = []


def residual(x):
    r = numpy.subtract(b, numpy.matmul(A, x))
    total = 0
    for value in r:
        total += abs(value ** 2)
    total = math.sqrt(total)
    return total


def L_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = i
        while j < len(matrix[i]):
            matrix[i][j] = 0
            j += 1
        i += 1
    return numpy.asarray(matrix)


def U_matrix(matrix):
    i = len(matrix) - 1
    while i >= 0:
        j = i
        while j >= 0:
            matrix[i][j] = 0
            j -= 1
        i -= 1
    return numpy.asarray(matrix)


def D_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if i != j:
                matrix[i][j] = 0
            j += 1
        i += 1
    return numpy.asarray(matrix)


def Gauss_Seidel(r_0):
    global iteration
    r = residual(r_0)
    list_of_r.append(r)
    d_l_inverse = numpy.linalg.inv(numpy.add(D_matrix(copy.deepcopy(A_array)), L_matrix(copy.deepcopy(A_array))))
    t = -1 * numpy.matmul(d_l_inverse, U_matrix(copy.deepcopy(A_array)))
    while r > tolerance:
        if len(set_of_points) == 0:
            x_new = numpy.add(numpy.matmul(t, x_0), numpy.matmul(d_l_inverse, b))
            set_of_points.append(x_new)
            r = residual(x_new)
            list_of_r.append(r)
            iteration += 1
        else:
            x_new = numpy.add(numpy.matmul(t, (set_of_points[iteration - 1])).tolist(), numpy.matmul(d_l_inverse, b))
            set_of_points.append(x_new)
            r = residual(x_new)
            list_of_r.append(r)
            iteration += 1
    return set_of_points[-1]


print(Gauss_Seidel(x_0))

list_of_x = [i for i in range(1, len(list_of_r)+1)]
plt.plot(list_of_x, list_of_r, label='Residual Curve')
plt.xlabel('Iterations')
plt.ylabel("Residual at k-th iteration")
plt.title("Plot of Residual versus Iteration: Gauss-Seidel Method")
plt.legend()
plt.show()
