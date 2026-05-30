import ollama

client = ollama.Client(host="http://127.0.0.1:11434")


def get_response(prompt):
    # 按格式组装信息
    # [{"role": "user", "content": 提问信息}]
    message = [{"role": "user", "content": prompt}]

    # 通过client变量内的.chat函数调用，进行模型访问，获得模型的回答
    result = client.chat(
        model="deepseek-r1:7b",     # 选择访问ollama的哪个模型
        messages=message            # 传入组装好的格式，进行提问
    )

    return result["message"]["content"]


if __name__ == '__main__':
    r = get_response("你好呀")
    print(r)
