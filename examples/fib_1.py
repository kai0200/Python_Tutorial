# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
斐波那契数列运算
"""


def fib(n):
    """ Print a Fibonacci series up to n. """
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


if __name__ == "__main__":
    fib(10)
