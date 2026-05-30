# __all__内置python变量，默认是*
# 如果你给与一个列表，列表内写上函数名称
# 可以控制这个文件（模块）被from ... import * 的时候，哪些函数可以被导入
__all__ = ['wangwang', 'hi']

def wangwang():
    print("C汪汪")


def hi():
    print("Hello")


def info():
    print("我是渣渣辉")


def miaomiao():
    print("喵喵喵")


