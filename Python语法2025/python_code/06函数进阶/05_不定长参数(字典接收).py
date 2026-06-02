def func(name, **kwargs):
    """
    **kwargs 是<class 'dict'>，即全部的关键字传参被收集到字典内
    """
    print(f'kwargs类型是{type(kwargs)}') # kwargs类型是<class 'dict'>
    print(kwargs)


# 本质上我们传递的就是KV键值对，被收集到kwargs这个字典内
func("aa", id=1, age=11, gender="男", addr="深圳石岩")


def func2(name, age, *args, **kwargs):
    print(f"元组收集：{args}")
    print(f"字典收集：{kwargs}")


func2("张三丰", 11, 1, 2, 3, 4, 5, 6, id=1, addr=2, gender=3)
