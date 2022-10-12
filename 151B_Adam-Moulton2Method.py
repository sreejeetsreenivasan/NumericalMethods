"""
The following code applies the 2-step Adam-Moulton Method to solve the given IVP
"""

from matplotlib import pyplot as plt
import math


set_of_points = []
y_0 = 1/3
y_1 = 0.20470052083333334
t_0 = 0
t_1 = 0.1
step_size = 0.1
iteration = 1


def equation(t, y):
    y_prime = -5 * y + 5 * (t ** 2) + 2 * t
    return y_prime


def adam_moulton_2(h, left_endpoint, right_endpoint):
    global set_of_points
    global iteration
    while iteration < right_endpoint / h:
        if len(set_of_points) == 0:
            approx = (y_1 + h * (5/12 * (5 * (t_1 + h) ** 2 + 2 * (t_1 + h)) + 2/3 *
                                 (-5 * y_1 + 5 * (t_1 ** 2) + 2 * t_1) - 1/12 *
                                 (-5 * y_0 + 5 * (t_0 ** 2) + 2 * t_0))) / (1 + 25/12 * h)
            set_of_points.append(approx)
            left_endpoint += 2 * h
            iteration += 1
        if len(set_of_points) == 1:
            approx = (set_of_points[iteration - 2] + h * (5/12 * (5 * (left_endpoint + h) ** 2 + 2 * (left_endpoint + h)) + 2/3 *
                                 (-5 * set_of_points[iteration - 2] + 5 * (left_endpoint ** 2) + 2 * left_endpoint) - 1/12 *
                                 (-5 * y_1 + 5 * (t_1 ** 2) + 2 * t_1))) / (1 + 25/12 * h)
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        else:
            approx = (set_of_points[iteration - 2] + h * (5/12 * (5 * (left_endpoint + h) ** 2 + 2 * (left_endpoint + h)) + 2/3 *
                                 (-5 * set_of_points[iteration - 2] + 5 * (left_endpoint ** 2) + 2 * left_endpoint) - 1/12 *
                                 (-5 * set_of_points[iteration - 3] + 5 * ((left_endpoint - h) ** 2) + 2 * (left_endpoint - h)))) / (1 + 25/12 * h)
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        adam_moulton_2(h, left_endpoint, right_endpoint)
    return set_of_points[-1]


print(adam_moulton_2(0.1, 0, 1))


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
