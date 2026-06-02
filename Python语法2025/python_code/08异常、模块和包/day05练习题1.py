import random

names = [
    "赵伟", "钱芳", "孙强", "李敏", "周杰", "吴丽", "郑涛", "王芳", "冯伟", "陈静",
    "褚刚", "卫红", "蒋涛", "沈丽", "韩梅", "杨强", "朱敏", "秦芳", "尤伟", "许丽",
    "何涛", "吕强", "施芳", "张伟", "孔丽", "曹刚", "严芳", "华伟", "金涛", "魏丽",
    "陶芳", "姜涛", "戚红", "谢梅", "邹伟", "喻芳", "柏涛", "水丽", "窦刚", "章芳",
    "云涛", "苏梅", "潘丽", "葛涛", "奚芳", "范伟", "彭丽", "郎涛", "鲁芳", "韦刚",
    "昌丽", "马涛", "苗芳", "凤伟", "花梅", "方涛", "俞丽", "任芳", "袁伟", "柳涛",
    "酆芳", "鲍伟", "史丽", "唐涛", "费芳", "廉伟", "岑涛", "薛丽", "雷芳", "贺涛",
    "倪伟", "汤丽", "滕涛", "殷芳", "罗伟", "毕丽", "郝涛", "邬芳", "安伟", "常丽",
    "乐涛", "于芳", "时伟", "傅丽", "皮涛", "卞芳", "齐伟", "康丽", "伍涛", "余芳",
    "元伟", "卜丽", "顾涛", "孟芳", "平伟", "黄丽", "和涛", "穆芳", "萧伟", "尹丽"
]
genders = ['男', '女', '男', '男', '女']
cities = ["北京", "上海", "深圳", "深圳", "深圳", "广州", "杭州", "杭州", "珠海"]


def generate_line(id):
    """
    生成一条随机数据
    :return: 数据字符串
    """
    random_name_index = random.randint(0, len(names) - 1)
    # 随机抽取的姓名
    name = names[random_name_index]
    age = random.randint(10, 35)
    height = random.randint(160, 190)
    weight = random.randint(70, 120)
    gender = genders[random.randint(0, len(genders) - 1)]
    city = cities[random.randint(0, len(cities) - 1)]

    line = f"{id},{name},{age},{height},{weight},{gender},{city}"
    return line


# open
f = open("D:/data.txt", "w", encoding="utf-8")

for id in range(1, 10001):
    line = generate_line(id)
    f.write(line)
    f.write("\n")  # 记得写换行

# close
f.close()

"""
写出的文件 可以称之为：csv（固定分隔符文件）
1,张三,11
2,王五,22
...
...
"""
