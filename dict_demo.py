# -*- coding: utf-8 -*-

# 根据key去dict中的value
def get_value(key_):
    _dict = {
        "a": "A",
        "b": "B",
        "c": "C"
    }
    _v = str('{%s}' % key_).format(**_dict)
    return _v


print(get_value("b"))
