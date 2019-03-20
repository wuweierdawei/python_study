# -*- coding: utf-8 -*-

def dynamic_run(py_script, param):
    try:
        g_context, l_context = {}, {}
        g_context.update(param)
        # g_context 传入执行的参数
        # l_context 收集执行后参数
        exec(py_script, g_context, l_context)
    except Exception as e:
        print(e)
    return l_context


with open("py_script/add.txt") as f:
    s = f.read()
    _param = {"x": 3, "y": 4}
    _l = dynamic_run(s, _param)
    print(_l)
# print
# {'x': 4, 'y': 8}
