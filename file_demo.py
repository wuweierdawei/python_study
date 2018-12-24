# -*- coding: utf-8 -*-


# 打开关闭文件
def low_file():
    f = open('说明.txt')
    # 比较low的实现
    try:
        data = f.read()
        f.write(data)
    finally:
        f.close()


def grace_file():
    # 使用 with 语句 系统会在执行完文件操作后自动关闭文件对象
    with open('data.txt') as f:
        data = f.read()
        f.write(data)
