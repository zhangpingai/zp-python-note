"""
通过type语句查看字面量和变量的数据类型是什么
"""

# 语法： type(被查看的)   被查看的可以是：字面量、变量
# 执行顺序： 1. 先执行type(666)得到结果  2. 将结果通过print显示在屏幕上
print(type(666))
print(type(12.345))
print(type("cxypa666"))

# 将类型信息记录到变量中
print("------------------")
# 执行顺序：1. 先执行type(666)得到结果  2. 将结果赋值给左侧的变量int_type
int_type = type(666)
float_type = type(12.333)
str_type = type("cxypa666")
print(int_type)
print(float_type)
print(str_type)

# type查看变量的类型
print("------------------")
name = "张三丰"
age = 11
height = 172.55
print(type(name))
print(type(age))
print(type(height))

text1 = "我是字符串"
text2 = '我是字符串'

'''我是字符串1，我是注释'''
name = '''我是字符串2，我不是注释'''
print(name)
name = """我是字符串3，我不是注释"""
print(name)
print(type(name))
