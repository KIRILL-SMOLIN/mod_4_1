    # Функция деления двух чисел по правилам высшей математики
from math import inf

def divide(chislit, znamenat):
    if znamenat == 0:
        return inf
    else:
        return chislit / znamenat
