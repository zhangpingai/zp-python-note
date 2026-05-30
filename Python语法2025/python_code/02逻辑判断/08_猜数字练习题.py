"""
num = 10

if input(请输入数字)==10?
    ...
elif input(请输入数字)== 10?
    ...
elif input(请输入数字)== 10?
    ...
else:
    ...
"""

num = 10
# 假设给3次猜测的机会
if int(input("请猜测第一个数字")) == num:
    print("猜中了你真棒")
elif int(input("请猜测第二次")) == num:
    print("第二次猜中")
elif int(input("请猜测第三次")) == num:
    print("第三次猜中")
else:
    print("憨货")
