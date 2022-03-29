"""
The following program uses the Composite Simpson's Rule to approximate the area under a curve
We use the formula that the area under a function f(x) within the interval [a, b] is equal to
(h/3) * [f(x_0) + 2 * (∑ f(x_2j), 1 ≤ j ≤ (n/2) - 1) + 4 * (∑ f(x_2j-1), 1 ≤ j ≤ n/2) + f(x_n)], where
h is the length of each sub-interval (h = (a - b) / n) and there exists 'n' such intervals
"""

import math


def composite_simpsons(a, b, n):
    h = (b - a) / n
    initial_point = a * math.log(a)
    iterative_sum_1 = 0
    iterative_sum_2 = 0
    a_j = a
    a_k = a - h
    for j in range(1, (n//2)):
        a_j += 2 * h
        iterative_sum_1 += (a_j * math.log(a_j))
    for k in range(1, (n//2) + 1):
        a_k += 2 * h
        iterative_sum_2 += (a_k * math.log(a_k))
    iterative_sum_1 *= 2
    iterative_sum_2 *= 4
    total_sum = initial_point + iterative_sum_1 + iterative_sum_2 + (b * math.log(b))
    final_sum = h * (1/3) * total_sum
    return final_sum


print(composite_simpsons(1, 2, 68))
