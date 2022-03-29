"""
The following program uses the Bisection Method (Binary Search) to find an approximate solution to the root of a function to within the prescribed error given an interval.
The function (w/ respect to the variable 'x') can be modified within the function 'func_expression'.
"""

import math


def func_expression(x):
    """
    :param x: Input into function
    :return: The function value at x
    Change the expression for 'solution' based on the function needing to be approximated
    """
    solution = x ** 2 - 3
    return solution


approx = []
error = math.pow(10, -3)


def bisection(a, b):
    global approx
    mid = (a + b) / 2
    if len(approx) >= 2:
        if abs((approx[-1] - approx[-2])) < error:
            print(f'The Bisection Method requires {len(approx)} iterations to approximate the root within {error}')
            for i in range(len(approx)):
                print(f'P{i + 1}: {approx[i]}')
            return
    if (func_expression(a) * func_expression(mid)) < 0:
        approx.append(mid)
        bisection(a, mid)
    else:
        approx.append(mid)
        bisection(mid, b)


bisection(0, 4)
