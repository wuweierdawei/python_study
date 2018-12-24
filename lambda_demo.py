# -*- coding: utf-8 -*-

def _lambda():
    _l = ['a', 'b', 'c']
    # lambda 结合 map、filter、reduce使用
    _l = map(lambda x: x + '!', _l)
    _r = ','.join(_l)
    return _r


print(_lambda())
