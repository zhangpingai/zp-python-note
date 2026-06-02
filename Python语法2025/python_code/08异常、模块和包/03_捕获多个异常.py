# 可以捕获多个异常，但是无法区分
try:
    open("asd", "r")
except (ZeroDivisionError, FileNotFoundError) as e:
    print("有异常了，异常是：", e)

# 同时捕获多个异常并进行区分
try:
    d = {}
    print(d['haha'])
except FileNotFoundError as e:
    print("文件没找到", e)
except ZeroDivisionError as e:
    print("除以0异常", e)
except KeyError as e:
    print("字典没这个Key")
