"""
Module uses Taylor series to calculate 1/(1+sinx) function\
and creates graphs for comparison of accuracy.
"""

from cProfile import label
from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np

def calculate(num, x_value):
    """
    (int, int/float) -> (float/int)
    Function uses Taylor's series to calculate value.
    The function returns an approximate function value.
    Function: 1/(1+sinx)
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
    return 1/(1+sinx)

def create_plot_1(seq_mem, num):
    """
    Function accepts two arguments:\
    seq_mem which will be passed to\
    calculate() function, and num which stands for\
    how many x values the function will calculate results\
    (with the step of 0.1).
    Function also calculates function values (for the same list\
    of x values) using built-in math.sin() function.
    Then two graphs are created.
    """
    x_args = list()
    i = 0.1
    for _ in range(num):
        x_args.append(i)
        i += 0.1
    y_talor = list()
    for x in x_args:
        y = calculate(seq_mem, x)
        y_talor.append(y)
    y_builtin = list()
    for x in x_args:
        y = 1/(1+sin(x))
        y_builtin.append(y)

    plt.plot(x_args, y_talor, label="Taylor series")
    plt.plot(x_args, y_builtin, label="built-in function")
    plt.title(f"comparison of two graphs\nnumber of terms: {seq_mem}")
    plt.legend()
    plt.show()

def create_plot_2(num):
    """
    Function creates two big graphs for\
    1/(1+sinx) function using built-in math.sin()\
    function and Taylor series.
    Argument num stands for the number of terms,\
    it will be passed to calculate() function.
    """
    x_args = np.linspace(-np.pi*10, np.pi*10, 1000)
    y_talor = list()
    for x in x_args:
        y = calculate(num, x)
        y_talor.append(y)
    y_builtin = list()
    for x in x_args:
        y = 1/(1+sin(x))
        y_builtin.append(y)

    fig = plt.figure()
    axes = fig.add_subplot(1, 1, 1)
    axes.spines['left'].set_position('center')
    axes.spines['bottom'].set_position('center')
    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.xaxis.set_ticks_position('bottom')
    axes.yaxis.set_ticks_position('left')

    axes.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot((0), (1), ls="", marker="^", ms=10, color="k",
            transform=axes.get_xaxis_transform(), clip_on=False)

    plt.axis([-30, 30, -10, 10])
    plt.plot(x_args, y_builtin, label="built-in function")
    plt.plot(x_args, y_talor, label="Taylor series")
    plt.legend()
    plt.show()
