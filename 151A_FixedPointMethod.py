"""
The following program uses the Fixed Point Method to approximate the root of a given function to within a certain error
given an initial point with which to start the algorithm
The function (w/ respect to x) can be modified in the "func_approximation" function below
"""

import math


def func_approximation(x):
    """
    :param x: Input into function
    :return: The function value at x
    Change the expression for 'solution' based on the function needing to be approximated
    The function listed in solution is "g(x)", that is we find "x = g(x)" based on f(x)
    """
    solution = x - ((1 / 10) * (x**2 - 3))
    return solution


approx = []
error = math.pow(10, -3)


def fixed_point(initial_point):
    global approx
    approximation = func_approximation(initial_point)
    approx.append(approximation)
    if len(approx) < 2:
        fixed_point(approximation)
    else:
        if abs((approx[-1] - approx[-2])) < error:
            print(f'The approximation of the root to under a {error} error is {approx[-1]}')
            for i in range(len(approx)):
                print(f'P{i + 1}: {approx[i]}')
            return
        fixed_point(approximation)


fixed_point(0)
