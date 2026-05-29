"""
演示使用Python调用Ollama进行模型对话
先确保Ollama已经启动
"""

import ollama

# 建立和Ollama的连接（代码和Ollama程序）
client = ollama.Client(host="http://127.0.0.1:11434")

# 准备用户的提问
prompt = input("请输入你的问题：")

# 封装要提问的格式
# [{"role":"user", "content": "提问的内容"}]
message = [{"role": "user", "content": prompt}]


# 调用ollama进行回答
result = client.chat(
    model="deepseek-r1:7b",     # 模型名
    messages=message            # 封装好的列表（内含提问信息）
)

# 只输出回答信息
print(result['message']['content'])
