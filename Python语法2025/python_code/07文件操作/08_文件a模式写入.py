"""
a模式 append追加
- 文件不存在则新建
- 文件存在，则在原有内容之后继续写入（原有内容保留，反之w模式是原有内容清空）
"""

# open
f = open("D:/word2.txt", "a", encoding="utf-8")

f.write("啦啦啦\n")  # write不会自带换行
f.write("呱呱呱\n")

# close
f.close()
