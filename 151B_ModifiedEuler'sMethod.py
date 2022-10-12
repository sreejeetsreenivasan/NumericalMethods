"""
The following code applies the Modified Euler's Method (2-stage Runge-Kutta Method) to solve the given IVP
"""

import math
from matplotlib import pyplot as plt

set_of_points = []
y_zero = 0.5
t_0 = 0
step_size = 0.01
iteration = 0
list_of_approx = []
list_of_errors = []


def equation(y):
    y_prime = 10 * (y - y * y)
    return y_prime


def modified_euler(h, left_endpoint, right_endpoint):
    global set_of_points
    global y_zero
    global iteration
    while iteration < right_endpoint / h:
        if len(set_of_points) == 0:
            slope_1 = equation(y_zero)
            slope_2 = equation(y_zero + h * slope_1)
            approx = y_zero + (h/2) * (slope_1 + slope_2)
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        else:
            slope_1 = equation(set_of_points[iteration - 1])
            slope_2 = equation(set_of_points[iteration - 1] + h * slope_1)
            approx = set_of_points[iteration - 1] + (h/2) * (slope_1 + slope_2)
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        modified_euler(h, left_endpoint, right_endpoint)
    # return f'The approximation of the IVP using step size {h} is {set_of_points[-1]}'
    return set_of_points[-1]


print(modified_euler(0.01, 0, 5))


def list_of_approximations(step_sizes):
    global set_of_points
    global iteration
    for value in step_sizes:
        if len(set_of_points) != 0:
            set_of_points.clear()
            iteration = 0
            result = modified_euler(value, left_endpoint=0, right_endpoint=1)
            list_of_approx.append(result)
        else:
            result = modified_euler(value, left_endpoint=0, right_endpoint=1)
            list_of_approx.append(result)
    return list_of_approx


# print(f'Approximations: ' f'{list_of_approximations([0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125])}')


def atkinson_estimation():
    estimates = []
    for i in range(len(list_of_approx) - 2):
        result = (list_of_approx[i] - list_of_approx[i + 1]) / (list_of_approx[i + 1] - list_of_approx[i + 2])
        estimates.append(math.log(result, 2))
    return estimates


def absolute_error(analytic_solution):
    for approximation in list_of_approx:
        result = abs(analytic_solution - approximation)
        list_of_errors.append(result)
    return list_of_errors


# print(f'Order of Accuracy: {atkinson_estimation()}')
# print(f'Abs Error: {absolute_error(0.741841337161)}')

list_of_x = []
i = 0
while i < len(set_of_points):
    if len(list_of_x) == 0:
        list_of_x.append(t_0)
        i += 1
    else:
        list_of_x.append(step_size + list_of_x[i - 1])
        i += 1

plt.plot(list_of_x, set_of_points)
plt.xlabel('t')
plt.ylabel('y')
plt.show()
