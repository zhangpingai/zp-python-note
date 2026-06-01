"""
嵌套调用的基本原则是：```遇到函数就进入执行```，执行完成后再回到当初的位置继续向下
def func_b():
    print("22222")
    func_a()
    print("33333")
比如执行完222后，遇到函数了，则进入，将函数执行完成后再回来继续执行333
"""


def func_a():
    print("11111")


def func_b():
    print("22222")
    func_a()
    print("33333")


def func_c():
    print("44444")
    func_b()
    print("55555")


func_c()
