lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = []  # 空的列表

index = 0
while index < len(lst1):
    if lst1[index] % 2 == 0:
        lst2.append(lst1[index])
    index += 1
print(f"while：从列表{lst1}取出偶数，得到新列表：{lst2}")

# 清理lst2
lst2.clear()
for i in lst1:
    if i % 2 == 0:
        lst2.append(i)

print(f"for：从列表{lst1}取出偶数，得到新列表：{lst2}")
