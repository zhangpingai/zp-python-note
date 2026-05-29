# day01 编程基础

  

![](assets/day01_编程基础/day01_编程基础-1.png)

  

**关于课程：学会之后可以做什么？**

  

![](assets/day01_编程基础/day01_编程基础-2.png)

  

![](assets/day01_编程基础/day01_编程基础-3.png)

  

![](assets/day01_编程基础/day01_编程基础-4.png)

  

**常见问题**

  

-   关于笔记，typora -> PDF。

-   关于课堂案例，动手写。

-   关于录播视频，每天录制，晚点时候给你。

  

## 1.关于编程

  

编程，就是学一门外语。

  

![](assets/day01_编程基础/day01_编程基础-5.png)

  

程序员vs非程序员

  

![](assets/day01_编程基础/day01_编程基础-6.png)

  

学习编程的本质：

  

-   学习一门编程语言的语法（Python、Java、PHP...），写代码

-   安装相应的 解释器/编译器，由解释器去对代码文件进行翻译，计算机能识别的语言。

  

![](assets/day01_编程基础/day01_编程基础-7.png)

  

```plain
D:\code\hello.py
```

  

![](assets/day01_编程基础/day01_编程基础-8.png)

  

![](assets/day01_编程基础/day01_编程基础-9.png)

  

## 2.Python解释器

  

解释器，就是一个软件。

  

### 2.1 下载

  

[https://www.python.org/downloads/](https://www.python.org/downloads/)

  

![](assets/day01_编程基础/day01_编程基础-10.png)

  

![](assets/day01_编程基础/day01_编程基础-11.png)

  

### 2.2 安装

  

![](assets/day01_编程基础/day01_编程基础-12.png)

  

![](assets/day01_编程基础/day01_编程基础-13.png)

  

![](assets/day01_编程基础/day01_编程基础-14.png)

  

注意：不要有中文路径；安装路径尽可能短；不要去里面操作；

  

![](assets/day01_编程基础/day01_编程基础-15.png)

  

### 2.3 测试运行

  

-   编写代码文件：`C:\code\hello.py`

-   解释器去运行

```plain
C:\Python39
	- python.exe       解释器，可以去运行并翻译代码
	- Scripts
		- pip.exe      包管理工具，下载第三方工具    C:\Python39\Scripts\pip.exe install requests
	- Lib
		- Python内置的功能
		- site-packages 从第三方下载的工具
			- requests
			- ...
```

  

想要运行：

  

-   终端  
    ![](assets/day01_编程基础/day01_编程基础-16.png)

-   通过终端去运行  
    ![](assets/day01_编程基础/day01_编程基础-17.png)

  

为什么要在终端去运行代码？

  

-   终端

-   GUI程序

-   网站

  

### 2.4 环境变量

  

```plain
>>>C:\Python39\python.exe  C:\code\v1.py
>>>C:\Python39\python.exe  C:\code\v2.py
>>>C:\Python39\python.exe  C:\code\v3.py
```

  

计算机中提供了一个叫环境变量的东西。

  

-   将Python解释器的安装目录加入到系统环境变量 `C:\Python39\`

-   以后再在终端去运行代码

```plain
>>>python  C:\code\v1.py
>>>python  C:\code\v2.py
>>>python  C:\code\v3.py
```

  

![](assets/day01_编程基础/day01_编程基础-18.png)

  

注意：想要生效，必须要重新打开终端。

  

对于win7的同学：

  

```plain
C:\Python39\;C:\Pythoxxxxxxx\;C:\Pythoxxxxxxx\;C:\Pythoxxxxxxx\;C:\Pythoxxxxxxx\;
```

  

同理，对于pip管理工具所在的目录也可以添加到环境变量。

  

```plain
>>>C:\Python39\Scripts\pip.exe install requests
```

  

```plain
>>>pip install requests
```

  

![](assets/day01_编程基础/day01_编程基础-19.png)

  

添加好环境变量后，在终端以后就可以方便的做如下操作：

  

```plain
>>>python 代码文件的路径
>>>pip install 第三方包
```

  

作为测试：

  

```plain
pip install requests
```

  

![](assets/day01_编程基础/day01_编程基础-20.png)

  

### 关于Mac

  

![](assets/day01_编程基础/day01_编程基础-21.png)

  

```plain
/Library/Frameworks/Python.framework/Versions/3.9/python  代码文件
/Library/Frameworks/Python.framework/Versions/3.9/bin/pip install 第三方包
```

  

![](assets/day01_编程基础/day01_编程基础-22.png)

  

![](assets/day01_编程基础/day01_编程基础-23.png)

  

![](assets/day01_编程基础/day01_编程基础-24.png)

  

## 3.IDE

  

集成开发环境，软件。

  

-   编辑器，优势：智能提示、错误提示。

-   调用Python解释器运行代码。

  

主流编写Python代码的相关IDE有两种：

  

-   vscode + Python相关各种插件，免费。

-   Pycharm（推荐）

-   专业版，收费（购买，激活工具）

-   社区版，免费

  

[https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

  

![](assets/day01_编程基础/day01_编程基础-25.png)

  

![](assets/day01_编程基础/day01_编程基础-26.png)

  

### 3.1 安装

  

![](assets/day01_编程基础/day01_编程基础-27.png)

  

![](assets/day01_编程基础/day01_编程基础-28.png)

  

![](assets/day01_编程基础/day01_编程基础-29.png)

  

### 3.2 激活（专业版）

  

![](assets/day01_编程基础/day01_编程基础-30.png)

  

![](assets/day01_编程基础/day01_编程基础-31.png)

  

![](assets/day01_编程基础/day01_编程基础-32.png)

  

![](assets/day01_编程基础/day01_编程基础-33.png)

  

```plain
https://jetbra.in
```

  

激活后，可以看到界面：

  

![](assets/day01_编程基础/day01_编程基础-34.png)

  

![](assets/day01_编程基础/day01_编程基础-35.png)

  

### 3.3 编写代码&运行

  

![](assets/day01_编程基础/day01_编程基础-36.png)

  

![](assets/day01_编程基础/day01_编程基础-37.png)

  

![](assets/day01_编程基础/day01_编程基础-38.png)

  

![](assets/day01_编程基础/day01_编程基础-39.png)

  

## 4\. 无法激活问题

  

暂时先用社区版，来进行学习。

  

### 4.1 下载社区版

  

[https://www.jetbrains.com/pycharm/download/other.html](https:_www.jetbrains.com_pycharm_download_other)

  

![](assets/day01_编程基础/day01_编程基础-40.png)

  

### 4.2 安装

  

![](assets/day01_编程基础/day01_编程基础-41.png)

  

![](assets/day01_编程基础/day01_编程基础-42.png)

  

![](assets/day01_编程基础/day01_编程基础-43.png)

  

### 4.3 创建项目

  

![](assets/day01_编程基础/day01_编程基础-44.png)

  

![](assets/day01_编程基础/day01_编程基础-45.png)

  

![](assets/day01_编程基础/day01_编程基础-46.png)

  

## 小结

  

-   Python解释器

```plain
C:\Python
	- python.exe
	- Scripts
		- pip.exe
	Lib
		...
```

-   解释器运行代码文件

```plain
>>>C:\Python\python.exe  代码文件的路径

C:\Python\ 添加到环境变量

>>>python.exe  代码文件的路径
```

-   运行pip去安装第三方包

```plain
>>>C:\Python\Scripts\pip.exe install requests 

C:\Python\Scripts\ 添加到环境变量

>>>pip install requests
```

  

如果我们把上述过程做完之后，可以文编辑器编写代码 + 终端 `python.exe 代码文件的路径` 运行代码 -> 费劲。

  

-   Pycharm，编辑器 + 运行代码 => 集成开发环境 IDE。

-   专业版安装+激活，激活工具出问题了。

-   社区版，安装。

  

## 5.创建项目&运行

  

本质上：创建文件夹，以后再创建代码文件。 再由解释器去运行代码文件。

  

![](assets/day01_编程基础/day01_编程基础-47.png)

  

![](assets/day01_编程基础/day01_编程基础-48.png)

  

后期再想创建项目：

  

![](assets/day01_编程基础/day01_编程基础-49.png)

  

![](assets/day01_编程基础/day01_编程基础-50.png)

  

![](assets/day01_编程基础/day01_编程基础-51.png)

  

![](assets/day01_编程基础/day01_编程基础-52.png)

  

![](assets/day01_编程基础/day01_编程基础-53.png)

  

![](assets/day01_编程基础/day01_编程基础-54.png)

  

建议：

  

-   不要汉化，功能会被阉割。

-   目录要区分开

-   Python解释器目录，不要手动做任何操作。

```plain
C:\Python39
	- python.exe
	- Scripts
		..
```

-   Python代码的目录，代码存放到哪里。

```plain
/Users/wupeiqi/PycharmProjects/
	day01
	day02
	day03
	crm
	web
```

-   Pycharm的安装目录，无所谓。

  

## 6.编码

  

你们是否遇到过乱码的情况？

  

-   文件

```plain
在计算机中存储任何数据都是以 0101010101010101（二进制）的形式存储起来。

中国移动           1000100101 1111101010 100000110  1111101010101

密码本A -> 编码
中   1000100101
国   1111101010

密码本B -> 编码
中   1011111111
国   1100001010

如果在文件存储时使用的A编码，打开文件时，也要使用A编码，这样才能正常显示。

推荐：保存文件时使用 UTF-8 编码。
```

  
![](assets/day01_编程基础/day01_编程基础-55.png)

-   Python解释器默认打开代码文件时，UTF-8编码

```python
>>>python xxxx.py
```

  

## 7.输出

  

输出，结果呈现出来。

  

```python
print("欢迎使用xxx系统")
```

  

```python
print("中国上海移动")
print("中国", "上海", "移动")
```

  

```python
print("中国上海移动", end="")
print("中国北京移动")
```

  

应用场景：欢迎信息。

  

```python
print("欢迎登录中国移动客服系统")
print("1.管理员登录；2.VIP登录；3.普通用户登录")
```

  

## 8.数据类型

  

### 8.1 整型（int）

  

平时生活中说的说的数字，例如：年龄、高低、重量。

  

```python
19
20
99
140
```

  

```python
1 + 1
2 - 1
8 * 7
100 / 5
```

  

```python
print(999)
print(8*7)
```

  

### 8.2 字符串（str）

  

平时生活中想要表示文本信息，例如：地址、城市、个人介绍。

  

```python
"我是上海移动的一名优秀员工"
"我是渣渣"

'我是优秀员工'
'你在做梦'
```

  

```python
"我叫" + "武沛齐" + "我在北京等你"
"我叫武沛齐我在北京等你"
```

  

```python
print("我是渣渣")
print("我叫" + "武沛齐" + "我在北京等你")
```

  

### 8.3 列表类型（list）

  

容器，可以帮你容纳好多数据。

  

```python
"吴丽,周杰,张三"

["吴丽","周杰","张三"]
["吴丽","周杰","张三",999]

[111,22,33]
```

  

### 8.4 字典类型 （dict）

  

```python
{ 键:值, 键:值, 键:值, 键:值 }
```

  

```python
{ "name":"武沛齐", "age":20, "email":"xxx@live.com"}

["武沛齐",20,"xxx@live.com"]
```

  

```python
[ "吴丽", "周杰", "张三" ]

[ {"name":"吴丽", "age":20}, {"name":"周杰", "age":20}, {"name":"张三", "age":20},  ]
```

  

## 9.变量

  

给一个值起外号，外号代指值。

  

```python
print("中国上海移动宝山总公司")
print("中国上海移动宝山总公司")
print("中国上海移动宝山总公司")
print("中国上海移动宝山总公司")
print("中国上海移动宝山总公司")
```

  

```python
v1 = "中国上海移动宝山分公司"
print(v1)
print(v1)
print(v1)
print(v1)
print(v1)

salary = 20000
print(salary)
print("我的工资", salary)  # 我的工资 20000
```

  

```python
v1 = 100
v2 = 200
v3 = v1 + v2 + 200
print(v3)  # 500
```

  

```python
num_list = [11,22,33,44,55]
info = {"name":"武沛齐","age":99}
```

  

**变量名规范：**

  

-   只能出现：字母、数字、下划线

-   不能以数字开头

```plain
9 = 100
3a = 100
```

-   不能是Python内部关键字

```python
[‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘exec’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘not’, ‘or’, ‘pass’, ‘print’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]
```

  

**问题**

  

```plain
v1 = 999
_name = 666
v_9 = 123
_ = "武沛齐"
```

  

**潜规则（建议）**

  

-   变量名不要用拼音

-   见名知意

```python
v1 = 123
v2 = 999

name = "武沛齐"
age = "xxxxx"
hobby = "篮球"
```

-   多个单词下划线连接

```python
first_name = "xxxxxxxxx"   # 建议，小驼峰
firstName = "xxxxxxx"      # 不建议，大驼峰
```

  

## 10.输入

  

让用户输入内容，实现交互。

  

```python
变量名 = input("提示信息")
```

  

```python
print("欢迎使用中国移动后台系统")

text = input("请输入姓名：")

data_string = "欢迎VIP用户" + text + "登录系统"

print(data_string)
```

  

![](assets/day01_编程基础/day01_编程基础-56.png)

  

## 11.注释

  

-   单行注释

```python
print("欢迎使用中国移动后台系统")

# 提示用户输入信息
text = input("请输入姓名：")

data_string = "欢迎VIP用户" + text + "登录系统"

print(data_string)  # xxx
```

-   多行注释

```python
print("欢迎使用中国移动后台系统")

"""
这是让用户输入的功能。
1.输入
2.赋值
"""
text = input("请输入姓名：")
data_string = "欢迎VIP用户" + text + "登录系统"

print(data_string)  # xxx
```

  

## 12.条件语句

  

```python
if 条件判断等到结果 :
    print(1)
    print(2)
    ...
else:
    print(9)
    print(8)
    print(7)
    ...
```

  

```python
# True/False
if 1 > 2:
    print("成功")
else:
    print("失败")
```

  

```python
# True/False
if 3==3 :
    print(666)
else:
    print(999)
```

  

```python
if True:
    print(123)
else:
    print(999)
```

  

```python
if False:
    print(123)
else:
    print(999)
```

  

```python
size = 19
if size > 8:
    print(123)
else:
    print(456)
```

  

```python
name = input("请输入姓名：")  # name = "eric"

if name == "武沛齐":
    print("登录成功")
else:
    print("登录失败")
```

  

案例：输入用户名和密码，判断用户名和密码是否正确，成功；否则失败。

  

![](assets/day01_编程基础/day01_编程基础-57.png)

  

案例：输入两个值相加。

  

```python
v1 = input("请输入数字：")  # v1 = "100"
v2 = input("请输入数字：")  # v2 = "200"
v3 = v1 + v2
print(v3)  # "100200"
```

  

```python
v1 = input("请输入数字：")  # v1 = "100"
v2 = input("请输入数字：")  # v2 = "200"
v3 = int(v1) + int(v2)
print(v3)  # 300
```

  

## 13.循环

  

在Python中有两种循环：while循环、for循环。

  

### 13.1 while循环

  

```python
while 条件判断的结果 :
    print("...")
    print("...")
```

  

```python
while True:
    print("欢迎过来")
```

  

```python
count = 0
while count < 5:
    print("欢迎登录")
    count = 10
```

  

```python
print("开始")
count = 0
while count < 5:
    print("欢迎登录")
    count = count + 1
print("结束")
```

  

![](assets/day01_编程基础/day01_编程基础-58.png)

  

### 13.2 for循环

  

```python
data_list = ["武沛齐","百灵","红颜"]

for item in data_list:
    print(item) # "武沛齐"
```

  

在开发的过程中还会和range结合使用。

  

```python
v1 = range(5)    # [0,1,2,3,4]
v2 = range(1,5)  # [1,2,3,4]
```

  

```python
for i in range(5): # [0,1,2,3,4]
    print(i)
```

  

### 13.3 break和continue

  

只能在while循环和for循环中使用这个两个关键字。

  

-   break，终止循环。

```python
print("开始")
while True:
    print(123)
    break
    print(456)
print("结束")
```

-   continue，停止本次循环，开始下次循环

```python
print("开始")
while True:
    print(123)
    continue
    print(456)
print("结束")
```

  

案例：让用户一直可以输入关键字。

  

```python
# 代码代替浏览器发送网络请求，实现搜索的功能

import requests

key = input("请输入关键字：")

res = requests.post(
    url="https://jf.10086.cn/cmcc-web-shop/search/query",
    data={
        "sortColumn": "default",
        "sortType": "DESC",
        "pageSize": "60",
        "pageNum": "1",
        "firstKeyword": key,
        "integral": "",
        "province": "",
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }
)
print(res.json())
```

  

```python
# 代码代替浏览器发送网络请求，实现搜索的功能

import requests

key = input("请输入关键字：")

while True:
    res = requests.post(
        url="https://jf.10086.cn/cmcc-web-shop/search/query",
        data={
            "sortColumn": "default",
            "sortType": "DESC",
            "pageSize": "60",
            "pageNum": "1",
            "firstKeyword": key,
            "integral": "",
            "province": "",
        },
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
        }
    )
    print(res.json())
```

  

```python
import requests

while True:
    key = input("请输入关键字：")

    res = requests.post(
        url="https://jf.10086.cn/cmcc-web-shop/search/query",
        data={
            "sortColumn": "default",
            "sortType": "DESC",
            "pageSize": "60",
            "pageNum": "1",
            "firstKeyword": key,
            "integral": "",
            "province": "",
        },
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
        }
    )
    print(res.json())
```

  

```python
import requests

print("开始")
while True:
    key = input("请输入关键字：")

    if key == "q" or key == "Q":
        break

    res = requests.post(
        url="https://jf.10086.cn/cmcc-web-shop/search/query",
        data={
            "sortColumn": "default",
            "sortType": "DESC",
            "pageSize": "60",
            "pageNum": "1",
            "firstKeyword": key,
            "integral": "",
            "province": "",
        },
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
        }
    )
    print(res.json())
    
print("结束")
```