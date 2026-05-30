import random

random_num = random.randint(1, 10)

# 第一次要求用户猜数字
num = int(input("第一次输入猜测数字："))
#
# if num == random_num:
#     print("你真棒一次就猜对了")
# else:
#     if num > random_num:
#         print("你猜大了")
#     else:
#         print("你猜小了")
#
#     num = int(input("第二次输入猜测数字："))
#
#     if num == random_num:
#         print("真棒，第二次猜对了")
#     else:
#         if num > random_num:
#             print("你猜大了")
#         else:
#             print("你猜小了")
#
#         num = int(input("第三次输入猜测数字："))
#
#         if num == random_num:
#             print("你最后猜对了")
#         else:
#             print("机会用完，全部猜错")
print(-6 % 2, 'a')
# 无法提示大了小了
if int(input("第一次输入猜测数字：")) == random_num:
    print("你真棒一次就猜对了")
elif int(input("第2次输入猜测数字：")) == random_num:
    print("你2就猜对了")
elif int(input("第3次输入猜测数字：")) == random_num:
    print("你3就猜对了")
else:
    print("全错")
