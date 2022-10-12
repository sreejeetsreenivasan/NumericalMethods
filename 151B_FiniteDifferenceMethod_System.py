"""
The following code applies the Finite Difference Method approximation to solve a 2nd-order BVP of the form
y'' + qy' + py = f(x). It also calculates the l_1, l_2, and l_infinity norms of the resulting error vector,
provided an exact solution
"""

import math
import numpy
from matplotlib import pyplot as plt


set_of_points = []
y_a = 0
y_b = -4
t_0 = 0
T = 2
step_size = 0.05
p = -2
q = 1
N = int((T - t_0)/step_size)


def equation(x):
    result = x * math.exp(x) - x
    return result


def function(x):
    result = (1/6) * x ** 3 * math.exp(x) - (5/3) * x * math.exp(x) + 2 * math.exp(x) - x - 2
    return result


A = []
B = []
for i in range(N-1):
    A.append([])
for j in range(N-1):
    B.append([])

for index, nested_list in enumerate(A):
    if index == 0:
        nested_list.extend([-2/(step_size ** 2) + q, 1/(step_size ** 2) + p/(2 * step_size)])
        nested_list.extend([0] * (N-3))
    elif index == N-2:
        nested_list.extend([0] * (N-3))
        nested_list.extend([1/(step_size ** 2) - p/(2 * step_size), -2/(step_size ** 2) + q])
    else:
        nested_list.extend([0] * (index - 1))
        nested_list.extend([1/(step_size ** 2) - p/(2 * step_size), -2/(step_size ** 2) + q, 1/(step_size ** 2) + p/(2 * step_size)])
        nested_list.extend([0] * (N-3-index))


for index, nested_list in enumerate(B):
    if index == 0:
        nested_list.append(equation(t_0) - y_a/(step_size ** 2) + p * y_a/(2 * step_size))
    elif index == N-2:
        nested_list.append(equation(T-step_size) - y_b/(step_size ** 2) - p * y_b/(2 * step_size))
    else:
        nested_list.append(equation(t_0 + step_size))
        t_0 += step_size

resultant_vector = numpy.matmul(numpy.linalg.inv(A), B)

list_of_x = []
list_of_y = []
list_of_f_values = []
i = step_size
append_x_iteration = 0
while append_x_iteration < len(resultant_vector):
    list_of_x.append(round(i, 1))
    i += step_size
    append_x_iteration += 1

for i in resultant_vector:
    list_of_y.append(i[0])

for element in list_of_x:
    list_of_f_values.append(function(element))

plt.plot(list_of_x, list_of_y, label='Approximate Solution')
plt.plot(list_of_x, list_of_f_values, label='Exact Solution', color='red')
plt.xlabel('t')
plt.ylabel('y')
plt.title("Finite Difference Method Approximation: h = 0.05")
plt.legend()
plt.show()

error_vector = [exact - approx for exact, approx in zip(list_of_f_values, list_of_y)]


def l_1_norm(list_of_errors):
    total = 0
    for value in list_of_errors:
        total += abs(value)
    return f'The l_1 norm of the error vector is {total}'


def l_2_norm(list_of_errors):
    total = 0
    for value in list_of_errors:
        total += abs(value ** 2)
    return f'The l_2 norm of the error vector is {math.sqrt(total)}'


def l_infinity_norm(list_of_errors):
    abs_list = map(abs, list_of_errors)
    return f'The l_infinity norm of the error vector is {max(abs_list)}'


print(l_1_norm(error_vector))
print(l_2_norm(error_vector))
print(l_infinity_norm(error_vector))
