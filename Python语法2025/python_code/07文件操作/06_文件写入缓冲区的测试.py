

# open
f = open("D:/word.txt", "w", encoding="utf-8")

f.write("哈哈哈哈哈哈")
f.flush()


# close  close之前会自动flush
f.close()
