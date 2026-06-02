"""
写函数的时候：
- 形式参数，可以接收函数传入
- 实际参数，真的可以传入一个函数

这种写法称之为函数式编程，核心思想是：传入的是计算逻辑
"""


def func(compute):
    # 被计算数据固定为1和2，要计算的逻辑取决于传入的compute函数
    result = compute(1, 2)
    print(result)


def compute1(x, y):
    return x + y


def compute2(x, y):
    return x - y


def compute3(x, y):
    return x * y


def compute4(x, y):
    return x / y


# 传入的是compute函数，而非变量和数据
# 传的是函数也就是传的是计算的逻辑
func(compute1)
func(compute2)
func(compute3)
func(compute4)
