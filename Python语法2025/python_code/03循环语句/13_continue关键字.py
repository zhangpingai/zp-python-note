"""
有10碗饭，内容不一样，每吃一碗前都会问你，这个吃不吃 吃就吃掉 不吃就跳过
"""

for i in range(1, 11):
    flag = int(input(f"第{i}碗饭，你吃不吃？吃输入1，不吃输入0"))
    if flag == 0:
        continue  # continue尽管在if内，但是和if没有任何关联，continue仅对for或while有效

    print(f"正在吃第{i}碗饭，吃完了")
