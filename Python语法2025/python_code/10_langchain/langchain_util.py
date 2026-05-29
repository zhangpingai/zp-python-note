from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Tongyi

memory = ConversationBufferMemory(return_message=True)


def get_response(prompt, api_key):
    model = Tongyi(model="qwen-max", api_key=api_key)
    chain = ConversationChain(llm=model, memory=memory)

    # 发送请求
    response = chain.invoke({"input": prompt})

    return response["response"]


if __name__ == '__main__':

    print(get_response("请python 1-100的输出", "sk-fa5b080ac78b4323b13f733b50f1d5c0"))
