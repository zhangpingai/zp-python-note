
"""
语法：
range(num1[, num2[,step]])
- []在描述语法中，表示：可选
写法1 range(num1)
写法2 range(num1, num2)
写法3 range(num1, num2, step)
"""

# range(5)结果：0, 1, 2, 3, 4
for i in range(5):
    print(i, end=" ")

print()
print("-"*20)
# 5, 6, 7, 8, 9
for i in range(5, 10):
    print(i, end=" ")

print()
print("-"*20)
# 步进为2： 5, 7, 9, 11, 13, 15, 17, 19
for i in range(5, 20, 2):
    print(i, end=" ")
