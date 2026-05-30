"""
数据类型的转换
"""

# 数字转字符串
t1 = str(123)
print(type(t1))
t2 = str(12.34)
print(type(t2))

# 整数和浮点数互转
print(float(123))  # 整数转浮点数，一切正常不会丢失精度
print(int(123.65))  # 浮点数转整数，会丢失小数精度

# 字符串转数字
t3 = int("123")
t4 = float("123.65")
print(type(t3))
print(type(t4))

# 错误示意
print(int("haha123"))
print(float("haha123"))
