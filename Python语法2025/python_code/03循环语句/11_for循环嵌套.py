"""
需求：每天都去表白 共100天
每次：表白送10个花 说1句我喜欢你
"""

# for i in range(1, 101):
#     print(f"今天是第{i}天表白祝我成功")
#
#     for j in range(1, 11):
#         print(f"\t第{i}天，送出第{j}朵玫瑰花")
#
#     print("我喜欢你")

# 外层for 内层while
for i in range(1, 101):
    print(f"今天是第{i}天表白祝我成功")

    j = 1
    while j < 11:
        print(f"\t第{i}天，送出第{j}朵玫瑰花")
        j += 1
    print("我哦喜欢你")
