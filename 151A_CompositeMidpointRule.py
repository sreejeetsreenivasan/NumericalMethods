"""
The following program uses the numerical method of the composite midpoint rule to approximate the area under a curve"
"""

import math


def composite_midpoint(a, b, n):
    h = (b - a) / n
    iterative_sum = 0
    a_i = a - h
    for i in range(1, (n//2) + 1):
        a_i += 2 * h
        iterative_sum += (a_i * math.log(a_i))
    final_sum = 2 * h * iterative_sum
    return final_sum


print(composite_midpoint(1, 2, 20414))
