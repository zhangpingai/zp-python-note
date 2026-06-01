"""
列表本质上是一个类，内部提供了很多内置函数（称之为方法）
这些内置函数（方法）的使用，在语法上比较特殊需要写为：

列表变量.内置函数()

"""

# 查找元素是否在列表中
# 列表变量.index(被查找的数据)
# 找到了返回下标值， 找不到报错
lst = ['cxypp', 'cxypa', 'python', '666']
print(lst.index("666"))

# 快捷操作 确定某个元素是否在列表内（找不到下标）
# 元素 in 列表变量
# 在里面给True  不在里面给False
print("666" in lst)

# 修改指定下标的元素值
# 列表变量[下标] = 值
lst = [1, 2, 3]
lst[0] = 5
print(lst)
lst[-2] = 10
print(lst)

# 在列表指定下标位置，插入新元素
# 语法： 列表变量.insert(下标, 元素)
# 当下标值超出列表的索引范围，则相当于在尾部新增一个元素
lst = [1, 2, 3]
# lst.insert(1, 'cxypp')
# print(lst)
# lst.insert(4, 'cxypa')
# print(lst)
lst.insert(10, '666')
print(lst)

# 在列表尾部新增元素
# 语法：列表变量.append(元素)
lst = [1, 2, 3]
lst.append(4)
lst.append(5)
lst.append(6)
print(lst)

# 在列表尾部新增一批元素（将其它数据容器追加到当前列表尾部）
# 语法：列表变量.extend(数据容器)
lst = [1, 2, 3]
lst.extend([4, 5, 6])
print(lst)

# 删除列表元素
# 方式1 del 列表[下标]
lst = [1, 2, 3, 4, 5, 6]
del lst[0]
print(lst)
# 方式2 列表.pop(下标)
# 和方式1的区别是 pop有返回值，返回的是：被删除的元素
deleted_data = lst.pop(2)
print("被删除的是：", deleted_data)
print(lst)

# 删除某元素在列表中的```第一个```匹配项
# 语法： 列表.remove(元素)
lst = ["cxypp", "cxypa", "cxypa", "python", "666"]
lst.remove("cxypa")
print(lst)
# lst.remove("xxx")   # 如果元素不存在，则报错
# print(lst)

# 清空列表
# 语法：列表.clear()
lst = [1, 2, 3, 4, 5, 6]
lst.clear()
print(lst)
# 方式2
lst = [1, 2, 3, 4, 5, 6]
lst = []
print(lst)

# 统计列表内某个元素的个数
# 语法：列表.count(元素)
lst = ["cxypp", "cxypa", "cxypa", "python", "666"]
print("lst.count(\"cxypa\"): %d" % lst.count("cxypa"))
print(lst.count("xxx"))

# 统计列表总共有多少元素
# 语法： len(列表)
lst = ["cxypp", "cxypa", "cxypa", "python", "666"]
print(len(lst))
