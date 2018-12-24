# -*- coding: utf-8 -*-

# 根据key去dict中的value
def get_value(key_):
    _dict = {
        "a": "A",
        "b": "B",
        "c": "C"
    }
    # '{key_name}' .format(**dict) , **_dict中的**声明参数为dict
    _v = str('{%s}' % key_).format(**_dict)
    return _v


print(get_value("b"))
