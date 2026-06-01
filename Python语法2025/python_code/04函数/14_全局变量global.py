"""
全局变量就是：不定义在函数内部的变量
"""
# 全局变量
num = 100  # 作用域在于整个代码


def func_a():
    print(f"a: {num}")


def func_b():
    global num  # 在此函数内部使用的num是全局变量
    num = 200  # 这个num就是访问全局变量，修改他的值
    print(f"b: {num}")  # 此时访问的num是全局变量num


func_a()
func_b()

print(f"外部：{num}")
