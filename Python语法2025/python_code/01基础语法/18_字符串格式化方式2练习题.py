"""
使用f_format方式格式化（字符串拼接）字符串
"""

name = "张三"
money = 100
salary = 18000.55

# f"{变量:精度}"
print(f"我是{name}, 钱包余额{money}元， 今天发工资{salary:10.1f}元， 钱包剩余：{money + salary}")
