"""
The following code applies the Trapezoidal Method to solve the given IVP
"""

from matplotlib import pyplot as plt
import math

set_of_points = []
y_zero = 1
t_0 = 0
step_size = 0.009
iteration = 0


def equation(t, y):
    y_prime = -50 * y + 50 * math.sin(t) + math.cos(t)
    return y_prime


def trapezoidal(h, left_endpoint, right_endpoint):
    global set_of_points
    global y_zero
    global iteration
    while iteration < right_endpoint / h:
        if len(set_of_points) == 0:
            approx_1 = -50 * y_zero + 50 * (math.sin(t_0) + math.sin(t_0 + h)) + math.cos(t_0) + math.cos(t_0 + h)
            approx = (y_zero + (h / 2) * approx_1) / (1 + 25 * h)
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        else:
            approx_1 = -50 * set_of_points[iteration - 1] + 50 * (math.sin(left_endpoint) + math.sin(left_endpoint + h)) + math.cos(left_endpoint) + math.cos(left_endpoint + h)
            approx = (set_of_points[iteration - 1] + (h / 2) * approx_1) / (1 + 25 * h)
            set_of_points.append(approx)
            left_endpoint += h
            iteration += 1
        trapezoidal(h, left_endpoint, right_endpoint)
    return set_of_points[-1]


print(trapezoidal(0.009, 0, 2))

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
