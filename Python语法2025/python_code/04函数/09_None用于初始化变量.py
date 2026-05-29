
# 当使用变量的时候，初始化的值没有任何要求，可以用None代替
age = None

for i in range(5):
    age = int(input("你的年龄是："))
    print(f"age: {age}")

print(f"最后一个同学的年龄是：{age}")
