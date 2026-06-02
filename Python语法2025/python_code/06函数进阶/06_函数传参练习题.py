def func(name, age, *args, **kwargs):
    print(f"我是{name}, 年龄{age}岁, 我的爱好有：", end="")
    for i in args:  # args是元组
        print(i, end=" ")

    print()
    print("我的其它信息：", end=" ")

    for key in kwargs:  # kwargs是字典
        print(f"{key}: {kwargs[key]}", end="、")

    print()


func("张三丰", 11, "唱", "rap", "跳", "打篮球", addr="石岩", id=123, money=20000)
