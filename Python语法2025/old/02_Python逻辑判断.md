进行逻辑判断，是生活中常见的行为。同样，在程序中，进行逻辑判断也是最为基础的功能。

![image.png](assets/02_Python逻辑判断/file-20260530130602971.png)

# **为什么学习判断语句**

判断在程序中广泛应用，如果没有它，这些功能都难以实现。

![image.png](assets/02_Python逻辑判断/file-20260530130602978.png)

# 布尔类型和比较运算符

进行判断，只有2个结果：

是

否

![](assets/Python逻辑判断/Python逻辑判断-3.png)

**程序中，如何描述：是或否呢？**

**使用：布尔类型**

## Python中常用的有6种值（数据）的类型

| 类型 | 描述 | 说明 |
| --- | --- | --- |
| 数字（Number） | 支持<br>•整数（int）<br>•浮点数（float）<br>•复数（complex）<br>•布尔（bool） | 整数（int），如：10、-10 |
|  |  | 浮点数（float），如：13.14、-13.14 |
|  |  | 复数（complex），如：4+3j，以j结尾表示复数 |
|  |  | 布尔（bool）表达现实生活中的逻辑，即真和假<br>•True表示真<br>•False表示假。<br>True本质上是一个数字记作1，False记作0 |
| 字符串（String） | 描述文本的一种数据类型 | 字符串（string）由任意数量的字符组成 |
| 列表（List） | 有序的可变序列 | Python中使用最频繁的数据类型，可有序记录一堆数据 |
| 元组（Tuple） | 有序的不可变序列 | 可有序记录一堆不可变的Python数据集合 |
| 集合（Set） | 无序不重复集合 | 可无序记录一堆不重复的Python数据集合 |
| 字典（Dictionary） | 无序Key-Value集合 | 可无序记录一堆Key-Value型的Python数据集合 |

## 布尔类型的定义

布尔类型的字面量：

•True 表示真（是、肯定）

•False 表示假（否、否定）

定义变量存储布尔类型数据：

变量名称 = 布尔类型字面量

> **布尔类型不仅可以自行定义**
> 
> **同时也可以通过计算的来。**
> 
> **也就是使用比较运算符进行比较运算得到布尔类型的结果。**

```plain
# bool类型本身，2个字面量
v1 = True       # 真
v2 = False      # 假
print(type(v1), type(v2)) # <class 'bool'> <class 'bool'>
```

## 比较运算符

布尔类型的数据，不仅可以通过定义得到，也可以通过比较运算符进行内容比较得到。

如下代码：

![image.png](assets/02_Python逻辑判断/file-20260530130602985.png)

  

| **运算符** | **描述** | **示例** |
| --- | --- | --- |
| == | 判断内容是否相等，满足为True，不满足为False | 如a=3,b=3，则(a == b) 为 True |
| != | 判断内容是否不相等，满足为True，不满足为False | 如a=1,b=3，则(a != b) 为 True |
| > | 判断运算符左侧内容是否大于右侧<br>满足为True，不满足为False | 如a=7,b=3，则(a > b) 为 True |
| < | 判断运算符左侧内容是否小于右侧<br>满足为True，不满足为False | 如a=3,b=7，则(a < b) 为 True |
| >= | 判断运算符左侧内容是否大于等于右侧<br>满足为True，不满足为False | 如a=3,b=3，则(a >= b) 为 True |
| <= | 判断运算符左侧内容是否小于等于右侧<br>满足为True，不满足为False | 如a=3,b=3，则(a <= b) 为 True |

  

```python

# bool类型本身，2个字面量
v1 = True       # 真
v2 = False      # 假
print(type(v1), type(v2)) # <class 'bool'> <class 'bool'>

# 可以通过比较运算得到布尔结果
# == 相等判断
print("-"*10, "==判断")
print("cxypa 等于 cxypp 吗？ %s" % ("cxypa" == "cxypp")) # False
print("5 = 5.0 吗？ %s" % (5 == 5.0)) # True
print('"5" = "5.0" 吗？ %s' % ("5" == "5.0")) # False

# != 不相等判断
print("-"*10, "!=判断")
print("cxypa 不等于 cxypp 吗？ %s" % ("cxypa" != "cxypp")) # True
print("5 != 5.0 吗？ %s" % (5 != 5.0)) # False
print('"5" != "5.0" 吗？ %s' % ("5" != "5.0")) # True

# > <  >=  <= 判断
print("-"*10, "> <  >=  <= 判断")
print("5 > 5 ? = %s" % (5 > 5)) # False
print("5 >= 5 ? = %s" % (5 >= 5)) # True
print("4 < 5 ? = %s" % (4 < 5)) # True
print("4 <= 5 ? = %s" % (4 <= 5)) # True

# 字符串比较
"""
字符串比较是按位比较，第一位和对方第一位比较，如果出结果后续不比了，如果没有结果继续向后比，条件：
"1" < "2" ...
"a" < "b" ...
"A" < "B" ...
"A" < "a" ... 大写字母小于小写字母
无内容 < 有内容  比如：  a 和 aa  大的是aa

速记：全部小写字母 > 全部大写字母 > 全部数字

"12" > "11"  True
"12" > "123" False

非中文字符的详细比较关系，需要参考ASCII码表
中文字符详细比较关系，需要参考UTF8编码表
"""
print("-"*10, "字符串比较")
print('"12" > "5" ? = %s' % ("12" > "5"))

print("你 > 我 = ? %s" % ("你" > "我"))
```
```python
<class 'bool'> <class 'bool'>
---------- ==判断
cxypa 等于 cxypp 吗？ False
5 = 5.0 吗？ True
"5" = "5.0" 吗？ False
---------- !=判断
cxypa 不等于 cxypp 吗？ True
5 != 5.0 吗？ False
"5" != "5.0" 吗？ True
---------- > <  >=  <= 判断
5 > 5 ? = False
5 >= 5 ? = True
4 < 5 ? = True
4 <= 5 ? = True
---------- 字符串比较
"12" > "5" ? = False
你 > 我 = ? False
```

# 逻辑运算符

```python
"""
运算符：逻辑运算
1. 与 AND
    多条件```同时```满足，则结果为True，否则是False
2. 或 OR
    多条件满足任意1个，则结果为True，否则是False
3. 非 NOT
    取反结果，True变成False或False变成True
"""
age = 19
print("5 < age < 18 = ? %s " % (age > 5 and age < 18)) # False
print("5 < age 或 age < 18 = ? %s " % (age > 5 or age < 18)) # True
print("age 不是成年人? %s" % (not age > 18)) # False
```

  

```python
5 < age < 18 = ? False 
5 < age 或 age < 18 = ? True 
age 不是成年人? False
```

  

# **if判断语句**

![image.png](assets/02_Python逻辑判断/file-20260530130602988.png)

  

```python
"""
语法：

if 条件判断（表达式）:
    条件成立的代码
    ...
    ...

- 条件判断（表达式）必须是产出布尔结果的
- : 号不要忘记
- 条件成立的代码和if语句在缩进上不是一个层级，要求是4个空格
"""

age = int(input("请输入你的年龄："))
height = int(input("请输入你的身高："))

# 条件判断满足才会执行里面的语句代码
if age >= 18:
    print("你已经成年了")

print("-" * 20)

# 必须满足年龄小于18岁，身高小于120，则输出你可以免票
if age < 18 and height < 120:
    print("你可以免票")

print("欢迎来游玩")
```
```python
请输入你的年龄：20
请输入你的身高：188
你已经成年了
--------------------
欢迎来游玩
```

## if语句的注意点

**判断语句的结果，必须是布尔类型True或False**

**True****会执行****if****内的代码语句**

**False则不会执行**

**​**  

**归属于if判断的代码语句块，需在前方填充4个空格缩进**

**Python通过缩进判断代码块的归属关系。**

![image.png](assets/02_Python逻辑判断/file-20260530130602982.png)

# if条件判断练习题

结合前面学习的input输入语句，完成如下案例：

1\. 通过input语句，获取键盘输入，为变量age赋值。（注意转换成数字类型）

2\. 通过if判断是否是成年人，满足条件则输出提示信息，如下：

提示：您已成年，需要补票的信息输出，来自if判断

  

```python
age = int(input("请输入你的年龄："))

if age >= 18:
    print("你已经成年，补票18元")

print("祝你愉快")
```
```python
请输入你的年龄：20
你已经成年，补票18元
祝你愉快
```

  

# if else条件判断

if满足条件会执行相应的代码语句，如果不满足呢？

有没有不满足的情况下，可供执行的代码呢？

**if else 语句可以实现**

![image.png](assets/02_Python逻辑判断/file-20260530130602997.png)

**​**  

**​**  

```python
money = int(input("请告诉我你还有多少钱："))

if money >= 10000:
    print("去买个新电脑")
else:
    print("洗洗睡吧")
```

  

```python
请告诉我你还有多少钱：666
洗洗睡吧

请告诉我你还有多少钱：99999
去买个新电脑
```

  

## if else语句注意点

**1\. else后，不需要判断条件**

**2\. 和if的代码块一样，else的代码块同样需要4个空格作为缩进**

  

# if else条件判断练习题

通过input语句获取键盘输入的身高

判断身高是否超过120cm，并通过print给出提示信息。

```python
height = float(input("请输入你的身高"))

if height > 120:
    print("你身高超出120cm，购票10元")
else:
    print("你身高不满足，可以免费")

print("祝你游玩愉快")
```
```python
请输入你的身高111
你身高不满足，可以免费
祝你游玩愉快

请输入你的身高188
你身高超出120cm，购票10元
祝你游玩愉快
```

# if elif else条件判断

某些场景下，判断条件不止一个，可能有多个。

这种需求能用Python实现吗？

**if elif else 语句可以实现**

![image.png](assets/02_Python逻辑判断/file-20260530130603000.png)

**​**  

```python
"""
if 条件：
    ...
elif 条件:
    ...
elif 条件:
    ...
elif 条件:
    ...
...
...
else:
    ...
"""

# height = int(input("请输入身高："))
# vip_level = int(input("请输入VIP级别："))
# day = int(input("今天几号："))
#
# # 如果身高小于120 免费、或者VIP级别大于3 免费、或者今天1号 免费、否则收费10元
# if height < 120:
#     print("免费(身高)")
# elif vip_level > 3:
#     print("免费(vip)")
# elif day == 1:
#     print("免费(1号)")
# else:
#     print("都不满足，收费10元")

# 如果身高小于120 免费、或者VIP级别大于3 免费、或者今天1号 免费、否则收费10元
if int(input("请输入身高：")) < 120:
    print("免费(身高)")
elif int(input("请输入VIP级别：")) > 3:
    print("免费(vip)")
elif int(input("今天几号：")) == 1:
    print("免费(1号)")
else:
    print("都不满足，收费10元")
```

# 猜数字练习题

1\. 定义一个变量，数字类型，内容随意。

2\. 基于input语句输入猜想的数字，通过if和多次elif的组合，判断猜想数字是否和心里数字一致。

```python
"""
num = 10

if input(请输入数字)==10?
    ...
elif input(请输入数字)== 10?
    ...
elif input(请输入数字)== 10?
    ...
else:
    ...
"""

num = 10
# 假设给3次猜测的机会
if int(input("请猜测第一个数字")) == num:
    print("猜中了你真棒")
elif int(input("请猜测第二次")) == num:
    print("第二次猜中")
elif int(input("请猜测第三次")) == num:
    print("第三次猜中")
else:
    print("憨货")
```

# if的嵌套判断

有很多场景，不仅仅是多个并列条件，还会有满足前置条件才会二次判断的多层判断需求。

**对这种需求，嵌套判断语句可以实现**

![image.png](assets/02_Python逻辑判断/file-20260530130602994.png)

许多逻辑的判断，是嵌套的，多层次的。

对于这种需求，我们可以：自由组合 if elif else，完成特定需求的要求。

![image.png](assets/02_Python逻辑判断/file-20260530130602975.png)

如上图，第二个if，属于第一个if内，只有第一个if满足条件，才会执行第二个if。

嵌套的关键点，在于：空格缩进

通过空格缩进，来决定语句之间的：层次关系

```python
# 需求： 身高大于120需要判断VIP级别大于3 可以免费， 身高小于等于120 直接免费

if int(input("请输入身高：")) > 120:
    if int(input("请输入VIP级别：")) > 3:
        print("VIP级别免费")
    else:
        print("收费10元")
else:
    print("欢迎你免费")
```

  

# if嵌套判断2

自由组合嵌套，需求如下：

公司要发礼物，条件是：

1\. 必须是大于等于18岁小于30岁的成年人

2\. 同时入职时间需满足大于两年，或者级别大于3才可领取

```python
age = int(input("请输入年龄"))
year = int(input("入职时间？"))
level = int(input("级别？"))

if age >= 18:
    if age < 30:
        if year >= 2:
            print("入职时间满2年，发礼物")
        elif level > 3:
            print("级别大于3，发礼物")
        else:
            print("级别和入职时间都不满足，无礼物")
    else:
        print("虽然成年但年龄超标，无礼物")
else:
    print("未成年不可以领取礼物")
```

  

# if判断实战案例

```python
age = int(input("请输入年龄"))
year = int(input("入职时间？"))
level = int(input("级别？"))

if age >= 18:
    if age < 30:
        if year >= 2:
            print("入职时间满2年，发礼物")
        elif level > 3:
            print("级别大于3，发礼物")
        else:
            print("级别和入职时间都不满足，无礼物")
    else:
        print("虽然成年但年龄超标，无礼物")
else:
    print("未成年不可以领取礼物")
```

# 猜数字游戏

```python
import random
random_num = random.randint(1, 10)

# 第一次要求用户猜数字
num = int(input("第一次输入猜测数字："))
#
# if num == random_num:
#     print("你真棒一次就猜对了")
# else:
#     if num > random_num:
#         print("你猜大了")
#     else:
#         print("你猜小了")
#
#     num = int(input("第二次输入猜测数字："))
#
#     if num == random_num:
#         print("真棒，第二次猜对了")
#     else:
#         if num > random_num:
#             print("你猜大了")
#         else:
#             print("你猜小了")
#
#         num = int(input("第三次输入猜测数字："))
#
#         if num == random_num:
#             print("你最后猜对了")
#         else:
#             print("机会用完，全部猜错")
print(-6 % 2, 'a')
# 无法提示大了小了
if int(input("第一次输入猜测数字：")) == random_num:
    print("你真棒一次就猜对了")
elif int(input("第2次输入猜测数字：")) == random_num:
    print("你2就猜对了")
elif int(input("第3次输入猜测数字：")) == random_num:
    print("你3就猜对了")
else:
    print("全错")

```
