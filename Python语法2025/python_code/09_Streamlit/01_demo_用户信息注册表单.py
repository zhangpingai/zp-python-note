import streamlit as st

# 添加一个sidebar的左侧导航
with st.sidebar:
    st.header("程序员平安版权所有")


# 添加标题
st.title("程序员平安用户注册")

# 添加分割线
st.divider()

# 添加文本输入框并收集用户填入的信息
username = st.text_input("请输入用户名")
# 添加密码输入框
password = st.text_input("设置密码", type="password")
# 添加年龄输入框
age = st.number_input(
    "请输入年龄",
    min_value=18,   # 最小值范围
    max_value=100,  # 最大值范围
    value=18,       # 默认值
    step=1          # 步进值
)
# 添加性别输入框
st.radio("输入性别",
         ("男", "女", "其它"),  # 多选一选项的元组
         horizontal=False)     # 水平为真
# 添加日期输入框
birthday = st.date_input("输入生日")
# 拖拉条输入
st.slider(
    "请输入身高",
    min_value=10,  # 最小值范围
    max_value=250,  # 最大值范围
    value=170,  # 默认值
    step=1  # 步进值
)

# 添加按钮
button = st.button("确认提交")
if button:  # 即用户点按按钮
    # 在网页中显示文本信息
    st.write("成功")

