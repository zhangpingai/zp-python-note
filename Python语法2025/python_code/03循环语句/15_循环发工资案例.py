import random

money = 10000  # 余额

for eid in range(1, 21):

    if money <= 0:
        print("没钱了，下次再来发工资结束")
        break

    score = random.randint(1, 10)

    if score < 5:
        print(f"编号{eid}，绩效分{score}分，太低，不发，下一个")
        continue

    money -= 1000
    print(f"编号{eid}绩效分{score}满足，领取1000元，余额剩余{money}元")
