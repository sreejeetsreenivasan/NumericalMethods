"""
The following program uses the Bisection Method (Binary Search) to find an approximate solution to the root of a
function after a set number of iterations.
The function (w/ respect to the variable 'x') can be modified within the function 'func_expression'.
"""

import math


def func_expression(x):
    """
    :param x: Input into function
    :return: The function value at x
    Change the expression for 'solution' based on the function needing to be approximated
    """
    solution = math.tan(x * math.pi) - 6
    return solution


approx = []
iterations = 0


def bisection(a, b):
    global iterations
    global approx
    mid = (a + b) / 2
    if iterations == 10:
        print(f'The approximation of the root after {iterations} iterations is {approx[-1]}')
        for i in range(len(approx)):
            print(f'P{i + 1}: {approx[i]}')
        return
    elif (func_expression(a) * func_expression(mid)) < 0:
        approx.append(mid)
        iterations += 1
        bisection(a, mid)
    else:
        approx.append(mid)
        iterations += 1
        bisection(mid, b)


bisection(0, 0.48)
