"""
文件操作3大步：
1. 打开
2. 读或写
3. 关闭
"""
import time

# 相对路径写法 在文件所在的文件夹内寻找
# f = open("hi.txt", "r", encoding="utf-8")
# 绝对路径写法 在指定的路径中寻找
f = open("D:/hi.txt", "r", encoding="utf-8")

# read([num])
# content = f.read()        # 读取全部
# print(content)

# content = f.read(3)         # 仅读取3个长度
# print(content)

# readlines
# lst = f.readlines()
# for line in f.readlines():
#     # readlines每一行的换行\n不会清除
#     line = line.strip()     # 去除首尾的空格和回车
#     print(line)

# readline  一次读取一行  \n不会被去掉
print(f.readline().strip())
print(f.readline().strip())

# close
f.close()
