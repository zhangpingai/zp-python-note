


# 数据和计算逻辑都是外部传入
def func(x, y, compute):
    result = compute(x, y)
    print(result)


func(10, 20, lambda x, y: x * y)


