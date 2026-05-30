f = None
try:
    # 我感觉这里可能出现问题
    f = open("D:/lala.txt", "r", encoding="utf-8")
except:
    # 如果真出现问题，应该怎么做
    f = open("D:/lala.txt", "w", encoding="utf-8")

print(f.read())
f.close()
