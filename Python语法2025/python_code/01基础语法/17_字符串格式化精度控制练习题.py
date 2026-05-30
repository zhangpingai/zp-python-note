money = 52.569

# 1.空格空格空格52.3
print("%7.1f" % money)  # 52.6
# 2.52.27
print("%.2f" % money)  # 52.57
# 3.52
# 通过%.0f将其变成整数，同样会有四舍五入
print("%.0f" % money)  # 53
# 直接转int是丢弃小数部分，即没有四舍五入
print(int(money))  # 52
