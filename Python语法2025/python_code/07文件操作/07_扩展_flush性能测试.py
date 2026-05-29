
import time

s = time.time()
f = open("d:/test.txt", "w", encoding="utf-8")

for i in range(1000000):
    f.write(str(i) + "\n")
    f.flush()       # 带这句话性能极具下降，安全性极具上升

f.close()
end = time.time()
print(end - s)
