import streamlit as st

# 设置标题
st.title("程序员平安智能聊天机器人")

# 添加分割线
st.divider()

# 聊天信息框(UTF8是全球统一编码，内部还有各类表情图像 Windows键+V)
st.chat_message("assistant", avatar="😘").write("你好我是人工智能机器人，有什么可以帮到您!")

# 用户输入框
prompt = st.chat_input()

st.chat_message("user", avatar="🐮").write(prompt)
st.chat_message("assistant", avatar="😘").write("天气不错，不下雨别打伞")
