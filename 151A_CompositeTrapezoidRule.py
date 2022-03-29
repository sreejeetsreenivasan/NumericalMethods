"""
The following program uses the Composite Trapezoid Rule to approximate the area under a curve
We use the formula that the area under a function f(x) within the interval [a, b] is equal to
(h/2) * [f(x_0) + 2 * (∑ f(x_j), 1 ≤ j ≤ n-1)) + f(x_n)], where h is the length of each sub-interval
(h = (a - b) / n) and there exists 'n' such intervals
"""

import math


def composite_trapezoid(a, b, n):
    h = (b - a) / n
    initial_point = a * math.log(a)
    iterative_sum = 0
    while a < (b - h):
        a = a + h
        iterative_sum = iterative_sum + (a * math.log(a))
    iterative_sum = iterative_sum * 2
    iterative_sum = iterative_sum + initial_point + (b * math.log(b))
    final_sum = h * (1/2) * iterative_sum
    return final_sum


print(composite_trapezoid(1, 2, 14434))
