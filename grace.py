# -*- coding: utf-8 -*-

# 定义变量 变量交换值
def _variable():
    a, b = 1, 2
    print(a, b)
    a, b = b, a
    print(a, b)


_variable()


# list 加 index
def _enumerate():
    a = ["a", "b", "c"]
    for _i, _v in enumerate(a):
        print({_i: _v})


_enumerate()


# 字符串连接
def _str_join():
    _l = ['a', 'b', 'c']
    print(",".join(_l))


_str_join()


# 打开关闭文件
def _low_file():
    f = open('说明.txt')
    # 比较low的实现
    try:
        data = f.read()
    finally:
        f.close()


def _grace_file():
    # 使用 with 语句 系统会在执行完文件操作后自动关闭文件对象
    with open('data.txt') as f:
        data = f.read()
