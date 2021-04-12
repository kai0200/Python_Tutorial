# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
class 相关功能测试
"""


class Point:
    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y


if __name__ == "__main__":
    P = Point(34, 97)
    print(f"Point x: {P.x} Point y: {P.y}")
