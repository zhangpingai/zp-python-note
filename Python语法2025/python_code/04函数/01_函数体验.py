# 1. 提前写好的  2. 重复利用   3. 特定需求（求长度）
def my_len(data):
    length = 0
    for _ in data:
        length += 1
        length += 1
    return length


name = 'cxypa'
print(f"{name}的长度是：{my_len(name)}")

info = "我爱学习学习是我快乐"
print(f"{info}的长度是：{my_len(info)}")

message = "今天要下大台风"
print(f"{message}的长度是：{my_len(message)}")
