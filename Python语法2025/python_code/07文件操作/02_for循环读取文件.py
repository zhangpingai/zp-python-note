

# 1. 打开 2 读取 3关闭
# 方式1
f = open("D:/hi.txt", "r", encoding="utf-8")

for line in f:
    print(line.strip())     # 还是需要自行处理\n

#这个写法等同于下面的写法
# for line in f.readlines():
#     print(line.strip())
f.close()


# 方式2
for line in open("D:/hi.txt", "r", encoding="utf-8"):
    print(line.strip())
# 这个方式3个步骤都集成了
# open是打开文件，  for循环读取行   for循环结束后会自动close


# d = {}
# for key in d:
#     pass
#
# for key in d.keys():
#     pass
