

# 需求： 身高大于120需要判断VIP级别大于3 可以免费， 身高小于等于120 直接免费

if int(input("请输入身高：")) > 120:

    if int(input("请输入VIP级别：")) > 3:
        print("VIP级别免费")
    else:
        print("收费10元")
else:
    print("欢迎你免费")
