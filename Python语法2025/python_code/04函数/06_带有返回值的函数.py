def add(x, y):
    print("函数执行开始")
    result = x + y
    return result
    print("函数执行结束")  # return 后的代码不会被执行


r = add(5, 2)  # return向调用方提供结果，add(5, 2)就等于7
print(r)

num = int("123")
