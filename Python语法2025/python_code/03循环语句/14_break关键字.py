"""
有10碗饭，挨个吃，每一碗饭吃之前问你饱没饱，吃饱了就不吃了
"""

for j in range(1, 11):
    print(f"今天是第{j}天干饭")

    for i in range(1, 11):
        flag = int(input(f"第{j}天的第{i}碗饭吃不吃，吃输入1不吃输入0："))
        if flag == 0:
            break  # break会直接结束循环（同样和if没关系，仅对for和while有效）

        print(f"吃完了第{i}碗饭，真香")

# i = 1
# while i <= 10:
#     flag = int(input(f"第{i}碗饭吃不吃，吃输入1不吃输入0："))
#     if flag == 0:
#         break  # break会直接结束循环（同样和if没关系，仅对for和while有效）
#
#     print(f"吃完了第{i}碗饭，真香")
#     i += 1
