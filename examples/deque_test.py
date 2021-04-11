# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

"""
Test collections.deque
用列表实现队列
"""
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.appendleft("Tom")
queue.popleft()
queue.pop()
