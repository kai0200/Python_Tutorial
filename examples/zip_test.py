# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
测试zip矩阵推导方法
"""
la = [1, 2, 3]
lb = ["a", "b", "c"]
lc = ["A", "B", "C"]
print(list(zip(la, lb, lc)))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(list(zip(*matrix)))
print([[row[i] for row in matrix] for i in range(4)])
