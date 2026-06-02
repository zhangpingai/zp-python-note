"""
with open() as f:
    ...
    ...

如果以这种语法写，文件会自动关闭，即自动调用close
"""

with open("D:/hi.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)

# 不需要写close
# 在python中任何 with xxx as xx: 的写法，都可以做到不用写close
