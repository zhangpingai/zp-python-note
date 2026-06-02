t1 = (1, 2, 3)
# 报错：TypeError: 'tuple' object does not support item assignment
# t1[0] = 5
# 报错：AttributeError: 'tuple' object has no attribute 'append'
# t1.append(4)

# 可以修改元组内部list的内部值
t1 = (1, 2, [6, 7, 8])
t1[2][2] = 80  # 这是对元组内的list的某个元素进行重新赋值
t1[2].append(100)

# 这是对元组元素的重新赋值为新list，不支持
# t1[2] = [5, 6, 7]

for item in t1:
    print(item)

print("=" * 60)

t1 = (1, 2, 3)
for i in t1:
    print(i)
