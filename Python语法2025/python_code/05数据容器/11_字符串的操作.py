
"""
字符串也是容器，同时有下标索引
它和元组一样，是一个不可修改的容器
"""

name = "cxypa"
# print(name[0])
# print(name[-1])

# 不可修改
# name[0] = "a"
# name.append("a")

# index 搜索子字符串在字符串内的下标
print(name.index("hei"))
# print(name.index("xxx"))    # 找不到就报错

# repalce(old_str, new_str)
# 将字符串内的全部old_str替换为new_str
# 注意：字符串不可修改，它是给你返回一个新的字符串，老字符串没变化
name = name.replace("i", "I")
print(name)


# split(分隔符) 按给定分隔符分隔字符串
# 将字符串分隔为多个部分
# 组装到一个列表中，对外返回
# 即字符串本身无变化，提供新列表作为返回值
info = "周杰伦,王力鸿,李思思,田七,张学油"
name_list = info.split(",")
print(name_list)


# strip() 去除首尾的空格和回车
# 字符串不可改，strip()是返回一个修改好的新字符串需要变量接收
info = "   cxypa   "
new_info = info.strip()
print(new_info)

# strip(字符串) 去除首尾的指定字符串
info = "[[[cxypa]]]"
print(info.strip("[]"))

# count统计自定子字符串的数量
info = "abcabcabc"
print(info.count("a"))      # 3
print(info.count("ab"))     # 3
print(info.count("abcd"))   # 0

# 查看字符串长度 中文算1个
info = "你好heima"
print(len(info))


