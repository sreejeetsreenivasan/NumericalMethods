"""
The following program applies the Secant Method (an extension of Newton's Method) to approximate the
roots of a given function. The function for which the roots are to be found can be modified below in
the "func_approximation" function.
"""

import math


def func_approximation(x):
    """
    :param x: Input into function
    :return:
    """
    f = x - math.cos(x)
    return f


approx = []
iterations = 0


def secant(p_0, p_1):
    global approx
    global iterations
    try:
        guess = p_1 - (((p_1 - p_0) / (func_approximation(p_1) - func_approximation(p_0))) *
                       func_approximation(p_1))
    except ZeroDivisionError:
        print(f'The approximation of the root after {iterations} iterations is {approx[-1]}')
        for i in range(len(approx)):
            print(f'P{i + 2}: {approx[i]}')
        return "Calculation stopped: Undefined"
    if iterations == 4:
        print(f'The approximation of the root after {iterations} iterations is {approx[-1]}')
        for i in range(len(approx)):
            print(f'P{i + 2}: {approx[i]}')
        return
    else:
        approx.append(guess)
        iterations += 1
        p_0 = p_1
        p_1 = guess
        secant(p_0, p_1)


secant(math.pi / 3, 0.75395)
