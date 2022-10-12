"""
The following code applies the Modified Euler's Method (2-step Runge-Kutta Method) to a system of equations
to solve a multi-step ODE
"""


import math
import numpy
from matplotlib import pyplot as plt

set_of_points = []
y_zero = [1, 2, 0]
t_0 = 0
step_size = 0.1
iteration = 0


def equation(t, y):
    coefficient_matrix = [[0, 1, 0], [0, 0, 1], [2, 1, -2]]
    y_prime = numpy.add(numpy.matmul(coefficient_matrix, y), (0, 0, math.exp(t)))
    return y_prime


def modified_euler(h, left_endpoint, right_endpoint):
    global set_of_points
    global y_zero
    global iteration
    while iteration < right_endpoint / h:
        if len(set_of_points) == 0:
            slope_1 = equation(t_0, y_zero)
            slope_2 = numpy.add(y_zero, h * slope_1)
            approx = numpy.add(y_zero, (h/2) * (numpy.add(slope_1, equation(t_0 + h, slope_2))))
            set_of_points.append(approx.copy())
            left_endpoint += h
            iteration += 1
        else:
            slope_1 = equation(left_endpoint, set_of_points[iteration - 1])
            slope_2 = numpy.add(set_of_points[iteration - 1], h * slope_1)
            approx = numpy.add(set_of_points[iteration - 1], (h/2) * (numpy.add(slope_1, equation(left_endpoint + h, slope_2))))
            set_of_points.append(approx.copy())
            left_endpoint += h
            iteration += 1
        modified_euler(h, left_endpoint, right_endpoint)
    # return f'The approximation of the IVP using step size {h} is {set_of_points[-1]}'
    return set_of_points[-1][0]


print(modified_euler(0.1, 0, 3))


def function(x):
    return (43/36) * math.exp(x) + (1/4) * math.exp(-x) - (4/9) * math.exp(-2 * x) + (1/6) * x * math.exp(x)


list_of_x = []
list_of_y0 = []
for i in set_of_points:
    list_of_y0.append(i[0])
i = 0
while i < len(set_of_points):
    if len(list_of_x) == 0:
        list_of_x.append(t_0)
        i += 1
    else:
        list_of_x.append(step_size + list_of_x[i - 1])
        i += 1

list_of_f_values = []
for x in list_of_x:
    list_of_f_values.append(function(x))

plt.plot(list_of_x, list_of_y0, label='Approximate Solution')
plt.plot(list_of_x, list_of_f_values, label='Exact Solution', color='red')
plt.xlabel('t')
plt.ylabel('y')
plt.title("Heun's Method Approximation for Third Order ODE")
plt.legend()
plt.show()
