"""
The following program applies Newton's Method to approximate the roots of a given function after a given number of
iterations. The function for which the roots are being approximated can be modified in the "func_approximation"
function below.
"""

import math


def func_approximation(x):
    """
    :param x: Input into function
    :return: The quotient of the function evaluated at a particular fixed point with its derivative evaluated
    at the same fixed point.
    """
    f = 1 - (x * math.exp(1 - x))
    derivative_f = (x - 1) * math.exp(1 - x)
    try:
        solution = f/derivative_f
    except ZeroDivisionError:
        return None
    return solution


approx = []
iterations = 0


def newton_method(p_0):
    global approx
    global iterations
    try:
        guess = p_0 - (func_approximation(p_0))
    except TypeError:
        return "Cannot Perform Calculation: Derivative Undefined"
    if iterations == 12:
        print(f'The approximation of the root after {iterations} iterations is {approx[-1]}')
        for i in range(len(approx)):
            print(f'P{i + 1}: {approx[i]}')
        return
    iterations += 1
    approx.append(guess)
    newton_method(guess)


newton_method(2)
