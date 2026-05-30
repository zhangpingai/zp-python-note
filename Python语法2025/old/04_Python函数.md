# 函数介绍

函数：是组织好的，可重复使用的，用来实现特定功能的代码段。

![image.png](assets/04_Python函数/file-20260530130618269.png)

**为什么随时都可以使用len()统计长度？**

**因为，len()是Python内置的函数：**

•**是提前写好的**

•**可以重复使用**

•**实现统计长度这一特定功能的代码段**

**我们使用过的：input()、print()、str()、int()等都是Python的内置函数**

# 函数体验

接下来，让我们实际的体验一下函数的使用。

让我们在PyCharm中完成一个案例需求：

不使用内置函数len()，完成字符串长度的计算。

**\> 体验代码，会出现未学习到的语法，同学们只需要关心效果即可，语法后面会详细讲解。**

```python
# 1. 提前写好的  2. 重复利用   3. 特定需求（求长度）
def my_len(data):
    length = 0
    for _ in data:
        length += 1
        length += 1
    return length

name = 'cxypa'
print(f"{name}的长度是：{my_len(name)}")

info = "我爱学习学习是我快乐"
print(f"{info}的长度是：{my_len(info)}")

message = "今天要下大台风"
print(f"{message}的长度是：{my_len(message)}")
```
```python
cxypa的长度是：10
我爱学习学习是我快乐的长度是：20
今天要下大台风的长度是：14
```

**为什么要学习、使用函数呢？**

**为了得到一个针对特定需求、可供重复利用的代码段**

**提高程序的复用性，减少重复性代码，提高开发效率**

# 函数的基础语法

## 函数的定义

![image.png](assets/04_Python函数/file-20260530130618305.png)

## 函数的调用：

函数名(参数)

​  

## 注意事项

① 参数如不需要，可以省略（后续章节讲解）

② 返回值如不需要，可以省略（后续章节讲解）

③ 函数必须先定义后使用

```python
"""
语法：
def 函数名称([传入参数]):
    ...
    [return ...]
[] 表示可选

使用函数语法：
函数名([传入参数])

-- 函数的特征：```提前写好的```、可重复使用、针对特定功能
先把函数写出来，然后你才能用
"""

# 函数：1. 先写出来
# 功能： 调用此函数输出你好
def hello():            # 这是准备一个函数
    print("你好，我是周杰轮，晚上一起打球")

# 2. 在去用
hello()
hello()
hello()
```

  

# 函数基础语法练习题

```python
"""
def 函数名(参数):
    ...
    return
"""

def say_hi():
    print("你好")
    print("我是渣渣辉")

say_hi()
say_hi()
say_hi()
```

# 带有传入参数的函数

传入参数的功能是：在函数进行计算的时候，接受外部（调用时）提供的数据

有如下代码，完成了2个数字相加的功能：

![image.png](assets/04_Python函数/file-20260530130618321.png)

函数的功能非常局限，只能计算1 + 2。

有没有可能实现：每一次使用函数，去计算用户指定的2个数字，而非每次都是1 + 2呢？

可以的，使用函数的传入参数功能，即可实现。

​  

## 函数的传入参数 - 传参定义

基于函数的定义语法：

![image.png](assets/04_Python函数/file-20260530130618331.png)

可以有如下函数定义：

![image.png](assets/04_Python函数/file-20260530130618325.png)

实现了，每次计算的是x + y，而非固定的1 + 2

x + y的值，可以在调用函数的时候指定。

## 函数的传入参数 - 语法解析

语法解析：

![image.png](assets/04_Python函数/file-20260530130618328.png)

•函数定义中，提供的x和y，称之为：形式参数（形参），表示函数声明将要使用2个参数

•**参数之间使用逗号进行分隔**

•函数调用中，提供的5和6，称之为：实际参数（实参），表示函数执行时真正使用的参数值

•**传入的时候，按照顺序传入数据，使用逗号分隔**

## 函数的传入参数

传入参数的数量是不受限制的。

•可以不使用参数

•也可以仅使用任意N个参数

```python
"""
语法：
def 函数名称([传入参数]):
    ...
    [return ...]
[] 表示可选
"""

# 函数需求：实现一个2个数字相加的函数
def add(x, y, z, q, w, e):      # 声明形式参数x和y，表明如果要用函数，请传入2个数据，函数将传入的数据赋值到x和y变量上
    # 相当于：x = 100   y = 200
    result = x + y
    print(f"{x} + {y} = {result}")

add(100, 200, 1, 1, 1, 1)

add("cxypa", "666", 1, 1, 1, 1)
# 参数名字说法：
"""
# 形式参数，即：def add(x, y):   这个x和y 称之为形式参数（形参）
叫做形式参数是因为，它没有实体，而是一种声明（口嗨）
即```声明```使用add函数，请提供2个数据，2份数据会赋值给x和y

# 实际参数，即：add(10, 20)  这个10和20 称之为实际参数（实参）
是因为在函数的声明要求下，调用的时候```真的```传递的符合要求的数据
即参数是实际存在的。

# 传入实际参数的类型不受限制，随意传，但是能不能跑就看具体代码了

# 传入参数的数量是不限的
"""
```

# 函数传参练习题

```python
def check_temp(temp):
    print("欢迎来到程序员平安，检查体温中...")
    if temp > 37.5:
        print("高烧，隔离")
    else:
        print("正常，请进")

temp = float(input("你的体温是："))
check_temp(temp)        # 实际参数可以传递变量

check_temp(float(input("你的体温是：")))  # 表达式也可以作为实际参数
```

# 带有返回值的函数

## 什么是返回值

![image.png](assets/04_Python函数/file-20260530130618340.png)

![image.png](assets/04_Python函数/file-20260530130618334.png)

如图代码

定义两数相加的函数功能。完成功能后，会将相加的结果返回给函数调用者

所以，变量r接收到了函数的执行结果。

综上所述：

所谓“返回值”，就是程序中函数完成事情后，最后给调用者的结果

## 返回值的语法

语法格式如图：

![image.png](assets/04_Python函数/file-20260530130618337.png)

如图，变量就能接收到函数的返回值

语法就是：通过return关键字，就能向调用者返回数据

```python
def add(x, y):
    print("函数执行开始")
    result = x + y
    return result
    print("函数执行结束")     # return 后的代码不会被执行

r = add(5, 2)       # return向调用方提供结果，add(5, 2)就等于7
print(r)

num = int("123")
```

# None类型

思考：如果函数没有使用return语句返回数据，那么函数有返回值吗？

实际上是：有的。

Python中有一个特殊的字面量：None，其类型是：<class 'NoneType'>

无返回值的函数，实际上就是返回了：None这个字面量

None表示：空的、无实际意义的意思

函数返回的None，就表示，这个函数没有返回什么有意义的内容。

也就是返回了空的意思。

演示：

![image.png](assets/04_Python函数/file-20260530130618265.png)

None可以主动使用return返回，效果等同于不写return语句：

![image.png](assets/04_Python函数/file-20260530130618276.png)

```python
# def say_hi():
#     print("我是渣渣辉来看我")
#
#
# def say_hi2():
#     print("啦啦啦")
#     return None
#
#
# x = say_hi()
# print(x)            # 结果None，表示什么都没有
# print(type(x))      # 类型NoneType，是一个数据类型仅有一个字面量None
#
# y = say_hi2()
# print(y)
# print(type(y))

if None:                # 在if判断中，None等同于False
    print("lalala")
```

# None用于if

None作为一个特殊的字面量，用于表示：空、无意义，其有非常多的应用场景。

•用在函数无返回值上

•用在if判断上

•**在****if****判断中，****None****等同于****False**

•**一般用于在函数中主动返回****None****，配合****if****判断做相关处理**

![image.png](assets/04_Python函数/file-20260530130618284.png)

•

•用于声明无内容的变量上

•**定义变量，但暂时不需要变量有具体值，可以用****None****来代替**

![image.png](assets/04_Python函数/file-20260530130618280.png)

```python
def check_age(age):
    if age < 18:
        return None
    return "SUCCESS"        # 在if中有内容的字符串算作True   空字符串算作False

if check_age(10):
    print("成年人")
else:
    print("未成年人")

"""
只要不是0、False、None、空字符串
其余都是True
"""
```

# None用于初始化变量

```python
# 当使用变量的时候，初始化的值没有任何要求，可以用None代替
age = None

for i in range(5):
    age = int(input("你的年龄是："))
    print(f"age: {age}")

print(f"最后一个同学的年龄是：{age}")
```

# 规范的函数注释写法

函数是纯代码语言，想要理解其含义，就需要一行行的去阅读理解代码，效率比较低。

我们可以给函数添加说明文档，辅助理解函数的作用。

语法如下：

![image.png](assets/04_Python函数/file-20260530130618272.png)

通过多行注释的形式，对函数进行说明解释

​内容应写在函数体之前

​:param 用于解释参数

​:return 用于解释返回值

```python
def add(x, y):
    """
    这里写函数功能说明
    param(parameter(参数)的缩写)
    :param x: 这里对每个参数做解释
    :param y: 这里对每个参数做解释
    :return: 这里对返回值做解释
    """
    return x + y

print(add(1, 2))
```

## 在PyCharm中查看函数说明文档

在PyCharm编写代码时，可以通过鼠标悬停，查看调用函数的说明文档

![image.png](assets/04_Python函数/file-20260530130618287.png)

# 函数的嵌套调用和执行流程分析

## 什么是函数的嵌套

所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数

![image.png](assets/04_Python函数/file-20260530130618293.png)

执行效果：

![image.png](assets/04_Python函数/file-20260530130618302.png)

## 执行过程

![image.png](assets/04_Python函数/file-20260530130618290.png)

如果函数A中，调用了另外一个函数B，那么先把函数B中的任务都执行完毕之后才会回到上次 函数A执行的位置

```python
"""
嵌套调用的基本原则是：```遇到函数就进入执行```，执行完成后再回到当初的位置继续向下
def func_b():
    print("22222")
    func_a()
    print("33333")
比如执行完222后，遇到函数了，则进入，将函数执行完成后再回来继续执行333
"""

def func_a():
    print("11111")

def func_b():
    print("22222")
    func_a()
    print("33333")

def func_c():
    print("44444")
    func_b()
    print("55555")

func_c()
```

# 局部变量

变量作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用）

主要分为两类：局部变量和全局变量

所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效

![image.png](assets/04_Python函数/file-20260530130618314.png)

变量a是定义在\`testA\`函数内部的变量，在函数外部访问则立即报错.

局部变量的作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量

```python
def func():
    # num是局部变量，作用域（生命周期）仅在函数内部有效
    # 局部变量：写在函数内部的变量（也叫做临时变量）
    num = 100
    print("内部输出", num)

func()

# 当函数执行完成后，临时变量（局部变量）num已经不存在了
# 即num存在的时间只有在调用函数的那一会儿

# 在print语句执行的这个地方，num已经不存在了
print("外部输出：", num)
```
```python
内部输出 100
Traceback (most recent call last):
  File "E:\stu\python_new2025\python_code\04函数\12_局部变量.py", line 15, in <module>
    print("外部输出：", num)
NameError: name 'num' is not defined. Did you mean: 'sum'?
```

# 全局变量

所谓全局变量，指的是在函数体内、外都能生效的变量

思考：如果有一个数据，在函数A和函数B中都要使用，该怎么办？

答：将这个数据存储在一个全局变量里面

![image.png](assets/04_Python函数/file-20260530130618297.png)

```python
"""
全局变量就是：不定义在函数内部的变量
"""
# 全局变量
num = 100       # 作用域在于整个代码

def func_a():
    print(f"a: {num}")

def func_b():
    num = 200       # 这个num是一个和全局num同名的局部变量
    print(f"b: {num}")  # 此时访问的num是局部变量num

func_a()
func_b()

print(f"外部：{num}")
```
```python
a: 100
b: 200
外部：100
```

# 全局变量global

思考：\`testB\`函数需要修改变量num的值为200，如何修改程序？

![image.png](assets/04_Python函数/file-20260530130618308.png)

\`testB\`函数内部的 num = 200 是定义了一个局部变量

☆ 使用 global关键字 可以在函数内部声明变量为全局变量, 如下所示

![image.png](assets/04_Python函数/file-20260530130618318.png)

```python
"""
全局变量就是：不定义在函数内部的变量
"""
# 全局变量
num = 100       # 作用域在于整个代码

def func_a():
    print(f"a: {num}")

def func_b():
    global num      # 在此函数内部使用的num是全局变量
    num = 200       # 这个num就是访问全局变量，修改他的值
    print(f"b: {num}")  # 此时访问的num是全局变量num

func_a()
func_b()

print(f"外部：{num}")
```
```python
a: 100
b: 200
外部：200
```