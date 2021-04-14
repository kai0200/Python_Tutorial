# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
class 相关功能测试
"""


class Point:
    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y


class MyClass:
    # 类变量所有实例共享
    i = 12345

    def __init__(self, name):
        # 实例变量实例独有
        self.name = name

    def put(self):
        return self.name

    def get(self, name):
        self.name = name

    def f():
        """ 类函数 """
        return 'hello world!'

    def m(self):
        """ 实例函数 """
        return 'm self'


class Dog:
    """正确的类的设计应该使用实例变量"""

    name = 'zaria'
    age = 8

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.trick.append(trick)


if __name__ == "__main__":
    P = Point(34, 97)
    print(f"Point x: {P.x} Point y: {P.y}")

    t = MyClass.f()
    u = MyClass('Jhon')
    print(MyClass.i, t, u.m())
