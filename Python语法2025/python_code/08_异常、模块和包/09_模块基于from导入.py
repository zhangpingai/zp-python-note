"""
from 模块名 import 功能 [as 别名]

用的时候：
功能名
就可以直接用了
不需要 模块.功能

-----------
假设模块叫做A，内部有3个功能分别是A1、A2、A3
如果 import A 导入
则用这三个功能需要： A.A1  A.A2  A.A3

如果是from写法则，用A1可以写成 from A import A1 直接用A1
限制在于如果要用A2需要在写
from A import A2
或者
from A import A1, A2

"""

# 需求还是用random模块的randint生成随机数
# import random as r
#
# r.randint()

# from random import randint
# randint(1, 10)      # 可以直接用randint函数名

# from random import randint as r     # 仅导入了random模块的randint函数，其它的没导入
# r(1, 10)      # 可以直接用别名代替原有的名称

# from random import randint, choices     # 导入了random模块的2个功能
# randint(1, 10)
# choices(['a', 'b'])

# 不推荐这种写法，因为可读性太差
from random import *            # 导入random内部的全部功能
from time import *
randint(1, 10)      # 因为如果导入多个模块，分不清这些函数是从哪个模块来的
choices(['a', 'b'])


