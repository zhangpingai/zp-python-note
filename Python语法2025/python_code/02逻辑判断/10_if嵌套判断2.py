
age = int(input("请输入年龄"))
year = int(input("入职时间？"))
level = int(input("级别？"))

if age >= 18:
    if age < 30:
        if year >= 2:
            print("入职时间满2年，发礼物")
        elif level > 3:
            print("级别大于3，发礼物")
        else:
            print("级别和入职时间都不满足，无礼物")
    else:
        print("虽然成年但年龄超标，无礼物")
else:
    print("未成年不可以领取礼物")
