num = 0
# 1. 打开文件
f = open("D:/word.txt", "r", encoding="utf-8")

for line in f.readlines():
    line = line.strip()
    for word in line.split(" "):
        if "cxypa" == word:
            num += 1

# 关闭文件
f.close()

print(f"文件内有{num}个cxypa")
