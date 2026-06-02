"""
函数的形式参数可以有默认值：
- 当调用函数不传递这个形式参数，则使用默认值
- 如果传递，则以传递的值为主
"""


def user_info(name, age, gender="男"):
    print(f"我是{name}, 今年{age}岁, 性别{gender}")


"""
其它细节

# 默认值可以为多个参数设置（数量不限）
def user_info2(name, age=10, gender="男"):
    print(f"我是{name}, 今年{age}岁, 性别{gender}")


# 默认值可以为多个参数设置（数量不限）
# 默认值参数必须在无默认值参数的右侧
# 无默认值参数必须在默认值参数的左侧
def user_info3(name, age=10, gender):
    print(f"我是{name}, 今年{age}岁, 性别{gender}")
"""

# 这种调用在参数传递的时候等于是：
# name = "小王"  -> 我们传递的
# age = 21      -> 我们传递的
# gender = "男"  -> 函数自带的
user_info("小王", 21)

# 这种调用在参数传递的时候等于是：
# name = "小美"  -> 我们传递的
# age = 22      -> 我们传递的
# gender = "男"  -> 函数自带的
# gender = "女"  -> 我们传递的
user_info("小美", 22, "女")

# 回忆, end是有默认值的，默认值是：end="\n"
print("哈哈", end="\t")
print("拉拉")
