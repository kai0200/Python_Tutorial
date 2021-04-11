# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
4.7.3 特殊参数
测试形参 /  * 的用法
/ 前必须按位置输入
* 后要使用key=value方式输入
"""


def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)


f(1, 2, 3, kwd1="a", kwd2="b")
f(1, 2, pos_or_kwd="or", kwd1="a", kwd2="b")
# error pos2 在/ 前不能使用key=value方式
f(1, pos2=2, pos_or_kwd="or", kwd1="a", kwd2="b")
