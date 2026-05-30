"""
使用f_format方式格式化（字符串拼接）字符串
"""

name = "张三"
age = 11
height = 172.55
# 1.字符串之前写f标记，如f""
# 2.变量用{}包起来即可
message = f"我是{name}，今年{age}岁，身高{height}厘米，{height:4.1f}米"
print(message)  # 我是张三，今年11岁，身高172.55厘米，172.6米
