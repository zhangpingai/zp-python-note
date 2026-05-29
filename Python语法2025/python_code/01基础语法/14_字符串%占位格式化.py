"""
演示使用%占位的方式对字符串进行格式化（拼接）
"""

name = "张三丰"
age = 11
height = 172.55

# 传统拼接
message = "我是" + name + "，今年" + str(age) + "岁，身高（cm）：" + str(height)
print(message) # 我是张三丰，今年11岁，身高（cm）：172.55

# %占位符
message2 = "我是%s" % name    # 将name的值 填入 %s所在的位置
print(message2) # 我是张三丰

# %s占位，但是提供数字类型，则会自动转为字符串
message3 = "我是%s，今年%s岁，身高（cm）：%s" % (name, age, height)
print(message3) # 我是张三丰，今年11岁，身高（cm）：172.55

# %s 占位是字符串
# %d 占位是数字
# %f 占位是浮点数

message4 = "我是%s，今年%d岁，身高（cm）：%f" % (name, age, height)
print(message4) # 我是张三丰，今年11岁，身高（cm）：172.550000
