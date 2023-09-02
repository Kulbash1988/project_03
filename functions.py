# Модуль для функций

def get_topmgrs(empl):
    return [n for n, s in empl.items() if s >= 100000]

def divide(dividend, divisor):
    """ Функция divide принимает делимое и делитель в качестве параметров. Возвращает целое частное"""
    quotient = 0

    while dividend > 0:
        dividend -= divisor
        quotient += 1
    return quotient

def trapezoid_s(a, b, h):
   return h * (a+b) / 2 

def sum_all(*args):
    total = 0
    for i in args:
        total += i

    return total