
"""
语法：
{元素, ..., ..., 元素}
"""
# 字面量
{1, 2, 3, "cxypa"}

# 空集合
s = set()       # 空集合只能这样写
s = {}          # 这不能创建空集合，反而是空字典
print(type(s))  # <class 'dict'>

# 变量
s = {1, 2, 3}
print(type(s))  # <class 'set'>

# 修改集合
# 下标
# s[0] = 10     # 集合没有下标
print(s)

# 去重
s = {1, 1, 2, 2, 3, 3, "cxypa", "cxypa", "程序员平安", "程序员平安"}
print(s)        # 去重了


# add添加新元素
s = {1, 2, 3}
s.add(4)
s.add(4)    # 多次添加4也只能加入1个因为去重
print(s)

# 移除元素
s = {1, 2, 3}
s.remove(2)
# s.remove(4) 如果不存在数据被移除，则报错
print(s)

# pop取出元素
s = {1, 2, 3}
element = s.pop()     # 没有参数可以传 随机取
print(f"取出元素{element}，集合内容：{s}")

# 清空集合
s = {1, 2, 3}
s.clear()
print(s)
s = {1, 2, 3}
s = set()       # 重新赋值为空集合也可以达到同样效果
print(s)


# 取出差集
s1 = {1, 3, 5}
s2 = {1, 3, 6}
# 保留s1有的 s2没的 放入s3  s1和s2不变
s3 = s1.difference(s2)
print(f"s1:{s1}, s2:{s2}, s3:{s3}")
# 保留s2有的 s1没的 放入s4  s1和s2不变
s4 = s2.difference(s1)
print(f"s1:{s1}, s2:{s2}, s4:{s4}")

# 消除差集
s1 = {1, 3, 5}
s2 = {1, 3, 6}
# 在s1内删除和s2相同的，即s1被修改，s2不变
s1.difference_update(s2)
print(f"s1:{s1}, s2:{s2}")

s1 = {1, 3, 5}
s2 = {1, 3, 6}
# 在s2内删除和s1相同的，即s2被修改，s1不变
s2.difference_update(s1)
print(f"s1:{s1}, s2:{s2}")

# 合并集合
s1 = {1, 3, 5}
s2 = {1, 3, 6}
# s1 s2不变，合并为s3（会去重）
s3 = s1.union(s2)
print(f"s1:{s1}, s2:{s2}, s3:{s3}")

# 查看集合元素个数
s = {1, 2, 3, 4, 5}
print(len(s))

s = {1, 2, 3, 4, 5, 5, 5, 5, 1, 3, 1}
# 集合支持遍历，但是顺序无法保证
for i in s:
    print(i)

# print("aaa" ,s[2]) 集合无法用下标

# 去重某list  list->set->list （顺序无法保证）
