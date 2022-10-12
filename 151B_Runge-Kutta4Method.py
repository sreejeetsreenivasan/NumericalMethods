"""
The following code applies the 4-stage Runge-Kutta Method to solve the given IVP
"""

from matplotlib import pyplot as plt
import math


set_of_points = []
y_zero = 1/3
t_0 = 0
step_size = 0.1
iteration = 0


def equation(t, y):
    y_prime = -5 * y + 5 * (t ** 2) + 2 * t
    return y_prime


def runge_kutta_4(h, left_endpoint, right_endpoint):
    global set_of_points
    global y_zero
    global iteration
    while iteration < right_endpoint / h:
        if len(set_of_points) == 0:
            slope_1 = equation(left_endpoint, y_zero)
            slope_2 = equation(left_endpoint + h / 2, y_zero + h / 2 * slope_1)
            slope_3 = equation(left_endpoint + h / 2, y_zero + h / 2 * slope_2)
            slope_4 = equation(left_endpoint + h / 2, y_zero + h / 2 * slope_3)
            approx = y_zero + h / 6 * (slope_1 + 2 * slope_2 + 2 * slope_3 + slope_4)
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        else:
            slope_1 = equation(left_endpoint, set_of_points[iteration - 1])
            slope_2 = equation(left_endpoint + h / 2, set_of_points[iteration - 1] + h / 2 * slope_1)
            slope_3 = equation(left_endpoint + h / 2, set_of_points[iteration - 1] + h / 2 * slope_2)
            slope_4 = equation(left_endpoint + h / 2, set_of_points[iteration - 1] + h / 2 * slope_3)
            approx = set_of_points[iteration - 1] + h / 6 * (slope_1 + 2 * slope_2 + 2 * slope_3 + slope_4)
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        runge_kutta_4(h, left_endpoint, right_endpoint)
    return set_of_points


print(runge_kutta_4(0.1, 0, 1))

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
