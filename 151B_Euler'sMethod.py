"""
The following program uses Euler's Method to compute an approximation for a function y(t) at some desired point,
and plots the general graph using the matplotlib library
"""
from matplotlib import pyplot as plt
import math


set_of_points = []
left_endpoint = 0
right_endpoint = 2
t_0 = 0
y_zero = 1
iteration = 0
step_size = 0.05
list_of_approximate_values = []
list_of_errors = []


def equation(t, y):
    y_prime = -50 * y + 50 * math.sin(t) + math.cos(t)
    return y_prime


def Euler(h):
    global left_endpoint
    global right_endpoint
    global set_of_points
    global y_zero
    global iteration
    while iteration < right_endpoint / h:
        if len(set_of_points) == 0:
            approx = equation(left_endpoint, y_zero) * h + y_zero
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        else:
            approx = equation(left_endpoint, set_of_points[iteration - 1]) * h + set_of_points[iteration - 1]
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        Euler(h)
    # return f'The approximation of the IVP using step size {h} is {set_of_points[-1]}'
    return set_of_points[-1]


print(Euler(0.05))


def list_of_approximations(step_sizes):
    global set_of_points
    global iteration
    for value in step_sizes:
        if len(set_of_points) != 0:
            set_of_points.clear()
            iteration = 0
            result = Euler(value)
            list_of_approximate_values.append(result)
        else:
            result = Euler(value)
            list_of_approximate_values.append(result)
    return list_of_approximate_values


def absolute_error(analytic_solution):
    for approximation in list_of_approximate_values:
        result = abs(analytic_solution - approximation)
        list_of_errors.append(result)
    return list_of_errors


# print(f'Approximations: {list_of_approximations([0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125])}')
# print(f'Absolute Error: {absolute_error(0.741841337161)}')

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
