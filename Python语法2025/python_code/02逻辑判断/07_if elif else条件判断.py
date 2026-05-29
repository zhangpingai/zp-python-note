"""
if 条件：
    ...
elif 条件:
    ...
elif 条件:
    ...
elif 条件:
    ...
...
...
else:
    ...
"""

# height = int(input("请输入身高："))
# vip_level = int(input("请输入VIP级别："))
# day = int(input("今天几号："))
#
# # 如果身高小于120 免费、或者VIP级别大于3 免费、或者今天1号 免费、否则收费10元
# if height < 120:
#     print("免费(身高)")
# elif vip_level > 3:
#     print("免费(vip)")
# elif day == 1:
#     print("免费(1号)")
# else:
#     print("都不满足，收费10元")

# 如果身高小于120 免费、或者VIP级别大于3 免费、或者今天1号 免费、否则收费10元
if int(input("请输入身高：")) < 120:
    print("免费(身高)")
elif int(input("请输入VIP级别：")) > 3:
    print("免费(vip)")
elif int(input("今天几号：")) == 1:
    print("免费(1号)")
else:
    print("都不满足，收费10元")


