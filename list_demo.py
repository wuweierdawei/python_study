# -*- coding: utf-8 -*-

# list 加 index
def _enumerate():
    a = ["a", "b", "c"]
    for _i, _v in enumerate(a):
        # print:enumerate: {0: 'a'}
        print("enumerate:", {_i: _v})


_enumerate()


# map 返回list
def _map():
    _l = ['a', 'b', 'c']
    # lambda 结合 map、filter、reduce使用,返回list
    _l = map(lambda x: x + '!', _l)
    _r = ','.join(_l)
    return _r


# print:map: a!,b!,c!
print("map:", _map())


# 过滤返回符合条件的list
def _filter():
    _l = ['a', 'b', 'c']
    _l = filter(lambda x: x == 'a', _l)
    _r = ','.join(_l)
    return _r


# print:filter: a
print("filter:", _filter())


# reduce() 函数会对参数序列中元素进行累积
def _reduce():
    _l = [{"v": 1}, {"v": 2}, {"v": 3}]

    def _func(x, y):
        _v = x['v'] + y['v']
        # 把_func函数运算的结果作为下一次执行_func的x参数值
        return dict(v=_v)

    # python3 把reduce放到了functools中
    from functools import reduce
    return reduce(_func, _l)


# print:reduce: {'v': 6}
print("reduce:", _reduce())


# zip
def _zip():
    f_name = ["张", "李", "王"]
    s_name = ["三", "四", "五"]
    for _i in zip(f_name, s_name):
        # _i为元组tuple("张","三")
        # print:张三
        print("".join(_i))


_zip()
