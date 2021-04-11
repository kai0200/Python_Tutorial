# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
关键字参数测试
"""


def print_st(uid: int, age: int = 18, school: str = "QingHua"):
    print(uid)
    print(age)
    print(school)
    print()


if __name__ == "__main__":
    print_st(11)
    print_st(uid=13, age=21, school="BeiDa")
