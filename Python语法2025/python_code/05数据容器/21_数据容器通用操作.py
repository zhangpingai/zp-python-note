
# 通用操作：遍历：略
# 通用操作：求元素个数：len(数据容器) 略


lst = [1, 3, 5, 7, 9]
t = (1, 3, 5, 7, 9)
s_str = "cxypa"
s_set = {1, 3, 5, 7, 9}
d = {"1": 11, "2": 22, "3": 33}
# 找出最大值
print(f"{lst}, max: {max(lst)}")
print(f"{t}, max: {max(t)}")
print(f"{s_str}, max: {max(s_str)}")
print(f"{s_set}, max: {max(s_set)}")
print(f"{d}, max: {max(d)}")        # 字典找最大key
# 找出最小值
print(f"{lst}, min: {min(lst)}")
print(f"{t}, min: {min(t)}")
print(f"{s_str}, min: {min(s_str)}")
print(f"{s_set}, min: {min(s_set)}")
print(f"{d}, min: {min(d)}")        # 字典找最小key

# 转列表
print("*"*50)
print(f"{t} 转list： {list(t)}")
print(f"{s_str} 转list： {list(s_str)}")
print(f"{s_set} 转list： {list(s_set)}")
print(f"{d} 转list： {list(d)}")      # 仅key转list

# 转元组
print("*"*50)
print(f"{lst} 转tuple： {tuple(lst)}")
print(f"{s_str} 转tuple： {tuple(s_str)}")
print(f"{s_set} 转tuple： {tuple(s_set)}")
print(f"{d} 转tuple： {tuple(d)}")      # 仅key转tuple


# 转字符串
print("*"*50)
print(f"{lst} 转str： {str(lst)}")
print(f"{t} 转str： {str(t)}")
print(f"{s_set} 转str： {str(s_set)}")
print(f"{d} 转str： {str(d)}")      # 字典整体转字符串

# 转集合
print("*"*50)
print(f"{lst} 转set： {set(lst)}")
print(f"{t} 转set： {set(t)}")
print(f"{s_str} 转set： {set(s_str)}")    # 去重会丢失 一个 i
print(f"{d} 转set： {set(d)}")      # 字典仅key转集合

# 排序
lst = [5, 3, 1, 7, 2]
t = (5, 3, 1, 7, 2)
s_str = "cxypa"
s_set = {5, 3, 1, 7, 2}
d = {"33": 11, "cc": 22, "bb": 33}

# 升序排序
print("*"*50)
print(f"{lst}, 排序后: {sorted(lst)}")      # 转为list
print(f"{t}, 排序后: {sorted(t)}")          # 转为list
print(f"{s_str}, 排序后: {sorted(s_str)}")  # 转为list
print(f"{s_set}, 排序后: {sorted(s_set)}")  # 转为list
print(f"{d}, 排序后: {sorted(d)}")     # 按key排序并且仅剩余key转为list
# 降序排序 reverse=True ，reverse可以不写，不写默认是False
print("*"*50)
print(f"{lst}, 排序后（reverse=True）: {sorted(lst, reverse=True)}")      # 转为list
print(f"{t}, 排序后（reverse=True）: {sorted(t, reverse=True)}")          # 转为list
print(f"{s_str}, 排序后（reverse=True）: {sorted(s_str, reverse=True)}")  # 转为list
print(f"{s_set}, 排序后（reverse=True）: {sorted(s_set, reverse=True)}")  # 转为list
print(f"{d}, 排序后（reverse=True）: {sorted(d, reverse=True)}")     # 按key排序并且仅剩余key转为list
