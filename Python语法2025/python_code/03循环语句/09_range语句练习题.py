num = int(input("请输入一个数字："))
even = 0
for i in range(1, num):
    if i % 2 == 0:
        even += 1

print(f"1到{num}之间有{even}个偶数")
