# python /Users/hirano.wataru/be_professional_python/function.py
# coding: utf_8

# 関数
# noinspection PyInterpreter
def f(x):
    # 関数定義のときにreturnを書かないとnoneが表示される。

    return x * 2


def d(x=2):
    return 2


result = f(10)
print(result)

d_result = d()
print(d_result)
