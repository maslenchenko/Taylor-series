"""
Module uses Taylor series to calculate 1/(1+sinx) function.
"""

from math import pi

def calculate():
    """
    Function for users.
    First things first you should  enter a number of\
    terms (int). Then enter a value of x (float or integer).
    It uses Taylor's series to calculate value.
    The function returns an approximate function value.
    Function: 1/(1+sinx)
    To quit type "q".
    """
    try:
        num = input(">>> please enter a number of sequence members:\n")
        num = int(num)
    except:
        if num == "q":
            quit()
        else:
            print("incorrect value")
            print(calculate())
            quit()
    try:
        x_value = input(">>> please enter for which x value you would like to calculate 1/(1+sinx) function:\n")
        x_value = float(x_value)
    except:
        if x_value == "q":
            quit()
        else:
            print("incorrect value")
            print(calculate())
            quit()
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

print(calculate())
