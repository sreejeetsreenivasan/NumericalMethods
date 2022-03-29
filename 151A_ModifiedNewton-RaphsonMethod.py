"""
The following program uses the Modified Newton's Method (a specific case of the Fixed Point Method) to approximate
the root of a function.
The Modified Newton's Method applies Newton's Method on a different function "mu", defined as the quotient of the
original function we want to find the root of and its first derivative. This increases the rate of convergence of
the algorithm.
The function "mu" can be modified in the "func_approximation" function below
"""

import math


def func_approximation(x):
    """
    :param x: Input into function
    :return: The quotient of the function evaluated at a particular fixed point with its derivative evaluated
    at the same fixed point.
    """
    mu = (1 - (x * math.exp(1 - x))) / ((x - 1) * math.exp(1 - x))
    derivative_mu = (((x - 2) * math.exp(x)) + math.e) / (math.e * ((x - 1) ** 2))
    try:
        solution = mu/derivative_mu
    except ZeroDivisionError:
        return None
    return solution


approx = []
iterations = 0


def modified_newton_method(p_naught):
    global approx
    global iterations
    try:
        guess = p_naught - (func_approximation(p_naught))
    except TypeError:
        print("Cannot Perform Calculation: Derivative Undefined")
        print(approx)
        return
    """
    if len(approx) >= 2:
        if abs((approx[-1] - approx[-2])) < error:
            print(f'Newton\'s Method requires {len(approx)} iterations to approximate the root within {error}')
            for i in range(len(approx)):
                print(f'P{i + 1}: {approx[i]}')
            return
    modified_newton_method(guess)
    """
    if iterations == 11:
        print(f'The approximation of the root after {iterations} iterations is {approx[-1]}')
        for i in range(len(approx)):
            print(f'P{i + 1}: {approx[i]}')
        return
    else:
        iterations += 1
        approx.append(guess)
        modified_newton_method(guess)


modified_newton_method(2)
