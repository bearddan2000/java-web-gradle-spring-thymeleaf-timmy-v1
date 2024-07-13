import math

def math_ceil(x):
    return math.ceil(x*100)/100

def math_round(lst: list, fn_ptr):
    x = fn_ptr(lst)
    return math_ceil(x)