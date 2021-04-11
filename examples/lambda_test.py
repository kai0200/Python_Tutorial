# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
测试lambda
"""


def make_add(n):
    return lambda x: x + n


f = make_add(42)  # f(0) 这里的0 对应lambda 里的x
print(f(0))  # make_add(42)定义了n值为42, f(0) 调取的是x
print(f(1))

# .sort 函数key指定一个函数返回值作为排序的标准
# pair[1] 按字母排序
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
