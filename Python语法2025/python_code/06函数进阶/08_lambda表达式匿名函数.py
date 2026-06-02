def func(compute):
    # 被计算数据固定为1和2，要计算的逻辑取决于传入的compute函数
    result = compute(1, 2)
    print(result)


# 调用func4次，完成+-*/
# 这些函数仅用一次，不用于重复使用，所以用lambda快速实现
func(lambda x, y: x + y)
func(lambda x, y: x - y)
func(lambda x, y: x * y)
func(lambda x, y: x / y)

# 如果想要重复利用，可以将lambda匿名函数存入变量中即可。
# 这个变量就是一个带名字的函数
chengfa = lambda x, y: x * y
print(chengfa(1, 3))
