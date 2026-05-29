"""
需求：累计1到100的和
"""

# 控制因子
num = 1
# 变量记录累加的结果
sum = 0

# 循环控制条件
while num < 101:
    sum += num
    num += 1

print(sum)
