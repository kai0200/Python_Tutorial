# Python 教程

[toc]

## 1. 甜点

Monty Python 飞行马戏团

## 2. 解释器

sys.argv[0] 处理-c -m
之后的选项，而是直接留在 sys.argv 中由命令或模块来处理

```sh
python -c "import os; print('hello world')"
python2 -m SimpleHTTPServer 8888
```

文件开头

```sh
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```

## 3. 速览

- 计算器
/ 除法
// 整除
% 余数

- 字符串
'...' "..." 意义相同
'\' 用于转义
word[0:11] 0不写默认为0
word[2:]   末尾不写默认为最后
word[1:999] 999越界不报错
word[::-1] 反向排序

- 列表

```py
>>> squares[:]  全部列表
>>> letters[2:5] = ['C', 'D', 'E']  替换列表
>>> # now remove them
>>> letters[2:5] = []  删除列表内容
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []  清空列表
len(l)
print('The value of i is', i)  “，”号后接变量
print(a, end=',')   end指定结尾符号
```

## 4. 流程控制工具

- while

```py
while a < 1000:
    a, b = b, a+b
    print(a, end=',')

```

- if

```python
if x < 0:
    x = 0
elif x == 0:
    print('x == 0')
elif x == 1:
    print('x == 1')
else:
    print('more')
```

- for

```sh
打印words里的顺序号+words[i]
words = ['cat', 'window', 'defenestrate']
for i in range(len(words)):
    print(i, words[i])
```

- sum
sum(range(4))  # 0 + 1 + 2 + 3

- list

>>> list(range(4))
[0, 1, 2, 3]

- break、continue 语句及 else 子句
- 函数默认值 4.7.1
- 关键字参数 4.7.2
- 特殊参数 4.7.3 formal_parameters.py
- 任意参数列表 4.7.4 random_parameter.py
- 解包实参列表 4.7.5

```py
list(range(3,6))
args = [3, 6]
list(range(*args))
def parrot(voltage, state='a stiff', action='voom'):
    print(voltage, state, action)

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d) # 这里通过字典定义了每个变量的值，**解包了这个字典
```

- Lambda 表达式  4.7.6 lambda_test.py

```py
def make_incrementor(n):
    return lambda x: x + n  # lambda 表达式返回函数返回值为x+n

f = make_incrementor(42)  # lambda x: "这里的lambda x为f(x)调用
f(1)
```

- 文档字符串

```py
def my_function():
'''说明文字，便于以后分析'''
print(my_function.__doc__)
```

- 函数注释

```py
def f(ham: str, eggs: str='eggs') -> str:
    print("Annotations:", f.__annotations__)  # annotations 注释
    return ham + 'and' + eggs
```

## 5. 数据结构

方法签名中 i 两边的方括号表示该参数是可选的

- 列表详解
l.append(x), l.extend(iterable)==a[len(a):] = iterable, l.insert(n,x),
l.remove(x), l.pop([i]), l.clear()==del a[:],
l.index(x[,start[,end]]), l.count(x), l.sort(*, key=None, reverse=False),
l.reverse(), l.copy()

q = deque(["Eric", "John", "Michael"])
q.appendleft("Tom")
q.append
q.pop
q.poplef
列表推导： [重要]
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[abs(x) for x in vec]
[(x, x**2) for x in range(6)]
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
[[row[i] for row in matrix] for i in range(4)] 矩阵推导
list(zip(*matrix)) 矩阵推导建议使用zip

- del语句

- 元组和序列
t = 12345, 54321, 'hello!'  元组定义方式1
t = (1, 2, 3)
x, y, c = t

- 集合set() 或 {}  # 集合没有重复的值
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
b = set('alacazam')
列表推导：
a = {x for x in 'abracadabra' if x not in 'abc'}

- 字典
- 循环技巧
- 深入条件控制
- 序列和其他类型比较

## 6. 模块

## 7. 输入输出

## 8. 错误和异常

## 9. 类

## 10. 标准库简介1

## 11. 标准库简介2

## 12. 虚拟环境和包

## 13. 接下来

## 14. 交互式编辑和编辑历史

## 15. 浮点算术：争议和限制

## 16. 附录

