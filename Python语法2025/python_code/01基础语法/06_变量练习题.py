# 变量名称 = 变量值
money = 50

print("当前钱包余额：", money, "元")
print("购买冰淇淋，花费10元")
print("购买可乐，花费5元")
# 写法1
# print("最终，钱包剩余：", money-10-5, "元")
# 写法2，先计算右侧结果，再赋予左侧变量
money = money - 10 - 5
# money = 35
print("最终，钱包剩余：", money, "元")
