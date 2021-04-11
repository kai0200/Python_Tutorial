# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
测试函数默认值, 默认值为[]{}等要注意在函数内判断
4.7.1. 默认值参数
"""


def f(a, L=[]):  # L 共享了默认值每调用一次都会增加
    L.append(a)
    return L


def f_2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


if __name__ == "__main__":
    print(f(1))
    print(f(2))
    print(f(3))

    print(f_2(1))
    print(f_2(3))
    print(f_2(5))
    print(f_2(7))
