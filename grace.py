# -*- coding: utf-8 -*-

# 定义变量 变量交换值
def _variable():
    a, b = 1, 2
    print a, b
    a, b = b, a
    print a, b


_variable()


# list 加 index
def _enumerate():
    a = ["a", "b", "c"]
    for _i, _v in enumerate(a):
        print {_i: _v}


_enumerate()


# 字符串连接
def _str_join():
    l = ['a', 'b', 'c']
    print ",".join(l)


_str_join()
