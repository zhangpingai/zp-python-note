"""
全局变量就是：不定义在函数内部的变量
"""
# 全局变量
num = 100  # 作用域在于整个代码


def func_a():
    print(f"a: {num}")


def func_b():
    num = 200  # 这个num是一个和全局num同名的局部变量
    print(f"b: {num}")  # 此时访问的num是局部变量num


func_a()
func_b()

print(f"外部：{num}")
