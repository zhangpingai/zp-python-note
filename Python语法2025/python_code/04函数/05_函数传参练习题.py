

def check_temp(temp):
    print("欢迎来到程序员平安，检查体温中...")
    if temp > 37.5:
        print("高烧，隔离")
    else:
        print("正常，请进")


temp = float(input("你的体温是："))
check_temp(temp)        # 实际参数可以传递变量

check_temp(float(input("你的体温是：")))  # 表达式也可以作为实际参数
