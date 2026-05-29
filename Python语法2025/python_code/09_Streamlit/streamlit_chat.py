"""
通过Streamlit完成聊天机器人页面开发
"""
import streamlit as st
import ollama_utils as utils

# 添加标题
st.title("程序员平安聊天机器人")

# 添加分割线
st.divider()

# 输出第一条消息 机器人欢迎语
if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content": "你好我是人工智能机器人，有什么可以帮到您!"}]
    # st.session_state["message"].append({"role": "assistant", "content": "你好我是人工智能机器人，有什么可以帮到您!"})

# list.append({"role": "user", "content": "内容"})
# state["message"]  =   [ {"role": "user", "content": "内容"} , {"role": "user", "content": "内容"}]
# 每一个消息的对话分为2部分： 角色，内容
# 机器人  角色：assistant   内容：说的话
# 人     角色：user         内容：说的话
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 用户输入 在页面下方添加用户输入栏
prompt = st.chat_input()

if prompt:          # 如果prompt有内容 表示用户提问

    # 首先将用户的提问在页面输出
    st.chat_message("user").write(prompt)

    # 把用户提问这个对话保存到session_state内
    st.session_state["message"].append({"role": "user", "content": prompt})

    # 调用AI回答
    with st.spinner("正在思考中..."):        # 转圈圈的加载框
        res = utils.get_response(prompt)

    # 将AI回答信息写到屏幕上
    st.chat_message("assistant").write(res)

    # 将AI回答的消息记录到session_state内
    st.session_state["message"].append({"role": "assistant", "content": res})
