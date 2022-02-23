"""
Module uses Taylor series to calculate 1/(1+sinx) function.
"""

from math import pi, sin

def calculate(num, x_value):
    """
    (int, int/float) -> tuple
    This function is created to check the accuracy\
    of the results.
    It calculates a value the same way as the user_sinx.py\
    module, but returns a tuple, where the first element is\
    the result obtained using Taylor series, and the second\
    is the result of using built-in function math.sin().
    First argument: number of terms.
    Second argument: x value.
    >>> print(calculate(10, 14))
    (0.5023592408312615, 0.5023592408312615)
    >>> print(calculate(5, 3))
    (0.8731241473396999, 0.8763320184878719)
    >>> print(calculate(5, 10))
    (2.004244549756309, 2.193083986739963)
    """
    x_value = x_value%(2*pi)
    sinx = 0
    for n in range(num):
        n += 1
        factorial = 1
        range1 = 2*n - 1
        for i in range(1,range1+1):
            factorial *= i
        sinx += (((-1)**(n-1))*x_value**(2*n-1))/factorial 
    return 1/(1+sinx), 1/(1+sin(x_value))
