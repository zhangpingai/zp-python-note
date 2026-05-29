
print("你是谁？")
# input还会阻塞程序运行，直到得到输入信息为止
name = input()
print("你的名字是：%s" % name)

# name = input("请告诉我你是谁？")
# print(name)

# 无论输入什么，都是字符串
var = input("请输入信息")
print(f"你输入的是：{var}，类型是：{type(var)}")

# 输入年龄
age = int(input("请输入年龄："))
age += 10
print(age)
