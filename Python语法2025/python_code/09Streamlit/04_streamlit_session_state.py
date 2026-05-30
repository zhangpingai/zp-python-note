"""
使用Streamlit的session_state功能，完成历史聊天的记录
"""

import streamlit as st


# 设置标题
st.title("程序员平安智能聊天机器人")

# 添加分割线
st.divider()
# 聊天信息框(UTF8是全球统一编码，内部还有各类表情图像 Windows键+V)
st.chat_message("assistant", avatar="😘").write("你好我是人工智能机器人，有什么可以帮到您!")

prompt = st.chat_input()


while True:
    if prompt == "exit":
        break

    if prompt:
        st.session_state[prompt] = {"content": prompt}

        for key in st.session_state:
            st.chat_message("user", avatar="🐮").write(st.session_state[key]["content"])

        prompt = None
