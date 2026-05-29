

def func():
    # 就是返回了  (1, 2)的元组
    return 1, 2


# 自动解包，将元素的2个元素赋值给x和y
x, y = func()
print(x, y)

# 接收到完整的元组
x = func()
print(x, type(x))
