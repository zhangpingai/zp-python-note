
print("5 + 2 =", 5 + 2)     # 应用加法
print("5 - 2 =", 5 - 2)     # 应用减法
print("5 * 2 =", 5 * 2)     # 应用乘法
print("5 / 2 =", 5 / 2)     # 应用除法，非整除
print("5 // 2 =", 5 // 2)   # 应用整除
print("5 % 2 =", 5 % 2)     # 应用取余
print("5 ** 2 =", 5 ** 2)   # 应用指数计算

#
age = 10
# 赋值运算符（=），表示将右侧的结果提供 给左侧变量
# 即执行上： 先执行右侧得到结果，再赋值给左侧变量
age = age + 5


# 复合运算符  基础架构： ?=
# a ?= b  表示   a = a?b
# ?可以是任何的数学运算符，如：+ - * / % // **
print("-----------------------")
num = 10
num += 1        # 等于 num = num + 1      11
print(num)
num -=1         # num = num - 1          10
print(num)
num*=2          # num = num * 2          20
print(num)

num /= 2        # num = num / 2          10
print(num)

num //= 2       # num = num // 2         5
print(num)

num **= 2       # num = num ** 2         25
print(num)

num %= 4         # num = num % 4          1
print(num)
