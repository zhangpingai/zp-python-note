"""
1. 循环控制因子的创建
2. 基于控制因子的条件
3. 循环控制因子的更新
"""

# 无限次数猜数字
# 循环：无限循环（只要猜错循环不停，反之猜对循环停止）
import random
random_num = random.randint(1, 100)


flag = True     # 循环控制因子

while flag:     # 基于控制因子的条件判断
    num = int(input("猜数字："))

    # 判断
    if num == random_num:
        print("猜对了")
        flag = False
    else:
        if num > random_num:
            print("大了")
        else:
            print("小了")


