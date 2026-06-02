#
my_list = ['程序员平安', '传智播客', '程序员平安', '传智播客', 'cxypa', 'cxypp', 'cxypa', 'cxypp', 'best']

s = set()

for i in my_list:
    s.add(i)

print(f"list: {my_list}")
print(f"set: {s}")

s = {7, 6, 5, 5, 5, 5, 5, 3, 2, 4, 4, 1}
print(s)  # 1,2,3,4,5,6,7   还是无序  输出是有序，是因为内部hash的顺序

s1 = "学IT来程序员平安就来程序员平安Python"
s2 = "学IT来程序员平安就来程序员平安python"
print(hash(s1))
print(hash(s2))
