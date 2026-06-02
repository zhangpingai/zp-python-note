# open
fr = open("D:/bill.txt", "r", encoding="utf-8")
fw = open("D:/bill.txt.bak", "w", encoding="utf-8")

for line in fr.readlines():
    line = line.strip()  # 去除最后的\n和前后多余的空格
    if "测试" == line.split(",")[4]:
        continue

    fw.write(line)
    fw.write("\n")  # 注意写换行

# close
fr.close()
fw.close()
