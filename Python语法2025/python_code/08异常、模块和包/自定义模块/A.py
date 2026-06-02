"""
import A
A.A1()
A.A2()
...

from A import A1
A1()


"""

"""
import B
B.say_hi()
B.wangwang()
print(B.add(1, 2))
print(B.name)
print(B.age)
print(B.height)
"""

# Python中的模块是单例，如果模块被多个文件导入，__name__是第一次导入这个模块的文件名称
from C import wangwang
import B

# from B import say_hi, wangwang
# say_hi()
# wangwang()

# 不推荐 可读性差，容易和其他模块冲突
# from B import *
# say_hi()
# wangwang()
# add(1, 2)
# print(name)   # 比如其他模块也有name则2者冲突
# print(age)
# print(height)

# 如果导入同名的功能，则后导入的生效
# from B import wangwang
# from C import wangwang
# wangwang()


# from C import *
# from C import miaomiao
# wangwang()
# hi()
# # info()
# miaomiao()
