# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
4.7.4意实参列表
*args 理解为[]
"""


def write_multiple_items(file, separator, *args):
    print(file, separator.join(args))

    for i in args:
        print(i)


write_multiple_items("filename", "/", "aaaa", "bbbb")
