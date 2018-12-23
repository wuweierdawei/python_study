# -*- coding: utf-8 -*-

# func 为被装饰方法
def print_func(func):
    # *args,**kwargs都是可变参数
    # *args表示任何多个无名参数
    # 它是一个tuple；**kwargs表示关键字参数，它是一个 dict
    def wrapper(*args, **kwargs):
        # 装饰器功能扩展
        print 'print_fun:{}'.format(kwargs['c'])
        # 回调被装饰方法
        func(*args, **kwargs)

    return wrapper


# 基于class的装饰器
class PrintFunc:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print 'PrintFunc:{}'.format(kwargs['c'])
        return self.func(*args, **kwargs)


@print_func
@PrintFunc
def main_func(a, b, c):
    print 'main_func:{}:{}'.format(a + b, c)
    return True


main_func(1, 2, c={"c": "hello!"})
