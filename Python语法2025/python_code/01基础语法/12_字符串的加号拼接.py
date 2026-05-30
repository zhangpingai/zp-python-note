print("程序员平安", "666")

# 在Python +号用于数字是数学计算，用于字符串就是2个字符串拼接在一起
print("程序员平安" + "666")

name = "张三丰"
skill = "太极拳"
say = "我是" + name + "，我的技能是" + skill
print(say)

name = "张三丰"
age = 11
height = 172.55
# 组装信息到info变量中，信息格式是：我是xxx，今年xxx岁，身高xxx厘米
# info = "我是" + name + "，今年" + age + "岁，身高" + height + "厘米"
info = "我是" + name + "，今年" + str(age) + "岁，身高" + str(height) + "厘米"
print(info)

# 字符串乘以数字，可以做到将字符串复制多少份前后拼接到一起
print("-" * 50)
