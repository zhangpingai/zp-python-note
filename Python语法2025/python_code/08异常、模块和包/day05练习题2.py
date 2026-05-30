# level1(10-18)  level2(18-26)  level3(36-35)
# 字典仅记录3个key 就是l1 l2 l3 默认的value是0
age_level_d = {
    "l1": 0,
    "l2": 0,
    "l3": 0,
}

height_level_d = {
    "l1": 0,        # l1 < 170
    "l2": 0         # l2 >= 170
}

bmi_level_d = {
    "l1": 0,        # l1 正常 （BMI<=28）
    "l2": 0         # l2 超重（BMI>28）
}




# open
f = open("D:/data.txt", "r", encoding="utf-8")
lines_list = f.readlines()
# close
f.close()

for line in lines_list:
    line = line.strip()  # 去除尾部的\n
    cols = line.split(",")

    id = cols[0]
    name = cols[1]
    age = int(cols[2])
    height = int(cols[3])
    weight = int(cols[4])
    gender = cols[5]
    city = cols[6]

    # 需求1
    if age >= 10 and age < 18:
        age_level_d["l1"] += 1
    elif age >= 18 and age < 26:
        age_level_d["l2"] += 1
    else:
        age_level_d["l3"] += 1

    # 需求2
    if height <= 170:
        height_level_d["l1"] += 1
    else:
        height_level_d["l2"] += 1

    # 需求3
    bmi = weight / ((height / 100) ** 2)
    if bmi <= 28:
        bmi_level_d["l1"] += 1
    else:
        bmi_level_d["l2"] += 1

# 结果输出
print(f"10~18岁人数：{age_level_d['l1']}、"
      f"18~26岁人数：{age_level_d['l2']}、"
      f"26~35岁人数：{age_level_d['l3']}")
print(f"身高小于等于1米7的人数：{height_level_d['l1']}、高于1米7的人数：{height_level_d['l2']}")
print(f"BMI小于等于28人数：{bmi_level_d['l1']}、大于28人数：{bmi_level_d['l2']}")
