"""
The following program applies Newton's Method to approximate the roots of a given function within a certain error bound.
The function for which the roots are being approximated can be modified in the "func_approximation" function below.
"""

import math


def func_approximation(x):
    """
    :param x: Input into function
    :return: The quotient of the function evaluated at a particular fixed point with its derivative evaluated
    at the same fixed point.
    """
    f = 1 - 4 * x * math.cos(x) + 2 * (x**2) + math.cos(2 * x)
    derivative_f = -2 * math.sin(2 * x) + 4 * x * math.sin(x) - 4 * math.cos(x) + 4 * x
    try:
        solution = f/derivative_f
    except ZeroDivisionError:
        return None
    return solution


approx = []
error = math.pow(10, -5)


def newton_method(p_naught):
    global approx
    try:
        guess = p_naught - (func_approximation(p_naught))
    except TypeError:
        return "Cannot Perform Calculation: Derivative Undefined"
    approx.append(guess)
    if len(approx) >= 2:
        if abs((approx[-1] - approx[-2])) < error:
            print(f'Newton\'s Method requires {len(approx)} iterations to approximate the root within {error}')
            for i in range(len(approx)):
                print(f'P{i + 1}: {approx[i]}')
            return
    newton_method(guess)


newton_method(1)
