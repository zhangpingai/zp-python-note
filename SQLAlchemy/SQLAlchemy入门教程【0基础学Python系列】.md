[https://zhuanlan.zhihu.com/p/583117190](https://zhuanlan.zhihu.com/p/583117190)

## 我的代码

[app1.py](https://www.yuque.com/attachments/yuque/0/2025/py/25744277/1746784755180-7b9bf963-9d61-43be-9507-7ffbed2cb738.py)

```python
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.operators import or_

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/test_db', echo=True)
print(f'engine: {engine}')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class ProductComment(Base):
    """创建实体类，继承Base基类"""
    __tablename__ = 'pro_comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    goodsid = Column(String(50), index=True, nullable=False)
    brand = Column(String(50), nullable=False)
    comment = Column(String(200))
    join_time = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        """重写显示方法，定义后查询时可以显示数据，不会显示内存地址"""
        Id = self.id
        Goods_id = self.goodsid
        Brand = self.brand
        Comment = self.comment
        Join_time = self.join_time
        return f'<ProductComment(Id={Id}, Goods_id={Goods_id}, Brand={Brand}, Comment={Comment}, Join_time={Join_time})>'

# 首次可通过此语句创建表
Base.metadata.create_all(engine)

print(f'创建表成功：{ProductComment.__tablename__}')

def add_data():
    # 创建一条数据
    NewComment = ProductComment(goodsid="123456789", brand="abcd", comment="这是一条评论")
    # 往数据库插入一条数据
    session.add(NewComment)
    # 提交数据
    session.commit()

    print(f'添加多条数据')
    # 创建多条数据
    com1 = ProductComment(goodsid="682779140960", brand="国产品牌", comment="这是一条评论2", join_time="2022-11-13")
    com2 = ProductComment(goodsid="682779140961", brand="美国品牌", comment="这也是一条评论3", join_time="2022-11-14")
    com3 = ProductComment(goodsid="682779140962", brand="英国品牌", comment="这又是一条评论4", join_time="2022-11-13")
    Comments = [com1, com2, com3]
    session.add_all(Comments)
    session.commit()

# add_data()

def query_data():
    # 查询所有数据
    all = session.query(ProductComment).all()
    # print(f'all = {all}')
    for p in all:
        print(f'p = {p}')

    # 条件查询一条数据
    first = session.query(ProductComment).filter(ProductComment.comment == '这是一条评论3').first()
    print(f'first = {first}')

    # 模糊查询
    like_all = session.query(ProductComment).filter(ProductComment.comment.like('%评论1%')).all()
    for p in like_all:
        print(f'like p = {p}')

    # 条件 and 操作: filter 写多个条件
    and_p = session.query(ProductComment).filter(ProductComment.goodsid == '682779140960', ProductComment.brand == '国产品牌4').first()
    print(f'and p = {and_p}')

    # 条件 or 操作: filter 写or_(多个条件)
    or_all = session.query(ProductComment).filter(or_(ProductComment.goodsid == '123456789', ProductComment.brand == '国产品牌4')).all()
    for p in or_all:
        print(f'or p = {p}')

    # 条件 in 操作: filter 条件.in_([数据, 数据])
    in_all = session.query(ProductComment).filter(ProductComment.goodsid.in_(['123456789', '682779140962'])).all()
    for p in in_all:
        print(f'in p = {p}')

    # 条件 not in 操作: filter 条件.notin_([数据, 数据])
    not_in_all = session.query(ProductComment).filter(ProductComment.goodsid.notin_(['123456789', '682779140962'])).all()
    for p in not_in_all:
        print(f'not in p = {p}')

# query_data()

def delete_data():
    # .query（）查询数据表.fiLter（）过滤函数.first（）选取第一个
    first = session.query(ProductComment).filter(ProductComment.goodsid == '123456789').first()
    print(f'first = {first}')
    # 删除数据
    session.delete(first)
    session.commit()

# delete_data()

def batch_delete_data():
    # 批量删除数据
    session.query(ProductComment).filter(ProductComment.goodsid == '682779140961').delete()
    session.commit()

# batch_delete_data()

def query_update_data():
    # 查询和更新数据
    result = session.query(ProductComment).filter(ProductComment.goodsid == '682779140960').first()
    # 查询的数据可以直接修改
    result.brand = '国产品牌2'
    session.commit()

    all = session.query(ProductComment).filter().all()

    for p in all:
        if p.id % 2 == 0:
            # 查询和更新数据
            result = session.query(ProductComment).filter(ProductComment.id == p.id).first()
            result.brand = '国产品牌4'
            session.commit()

# query_update_data()

def upate_data():
    session.query(ProductComment).filter(ProductComment.goodsid == '682779140960').update({'brand': '国产品牌3', 'comment': '这是一条评论3'})
    session.commit()

# upate_data()
```

## 一、基础介绍

### 1\. ORM简介

ORM(Object Relational Mapping，[对象关系映射](https://zhida.zhihu.com/search?content_id=217715985&content_type=Article&match_order=1&q=%E5%AF%B9%E8%B1%A1%E5%85%B3%E7%B3%BB%E6%98%A0%E5%B0%84&zhida_source=entity))

一个天才发明的简易操作数据库的方法，可以绕过繁琐的SQL语句，把数据库的table(表)映射为class(类)，把行作为实例，把字段作为属性，在执行对象操作时最终会把对象的操作转换为数据库的原生语句。

### 2\. 安装方法

```python
pip install pymysql
pip install sqlalchemy
```

### 3\. 连接数据库

```python
from sqlalchemy import create_engine  # 导入连接数据库函数

# create_engine("数据库类型+数据库驱动://数据库用户名:数据库密码@IP地址:端口号/数据表名称", 其它参数)
engine = create_engine("mysql+pymysql://user:password@localhost:3306/database",echo=True) # 实例化数据库连接
```

echo=True，用来设置[SQLAlchemy](https://zhida.zhihu.com/search?content_id=217715985&content_type=Article&match_order=1&q=SQLAlchemy&zhida_source=entity)日志，记录所有数据库的操作记录

create\_engine( )，返回的是Engine的一个实例，并不会真正连接数据库，只有执行命令的时候才会尝试建立连接，目的是节省资源。

### 4\. 映射声明

```python
from sqlalchemy.ext.declarative import declarative_base # 导入映射声明函数
Base = declarative_base（）# 实例化ORM的基类
```

需要先定义一个基类，后续才可以使用ORM映射的子类(class)

## 二、创建数据表

### 5\. 创建class类

创建数据表的全部代码

```python
from sqlalchemy import create_engine  # 导入连接数据库函数
from sqlalchemy.ext.declarative import declarative_base  # 导入映射声明函数
from sqlalchemy import Column, String, Integer, DateTime  # 导入创建字段函数及字段类型
from datetime import datetime  # 时间库，用于获取当前时间

engine = create_engine("mysql+pymysql://user:password@localhost:3306/database",echo=True) # 实例化数据库连接
Base = declarative_base()  # 实例化ORM的基类

class ProductComment(Base):
    """创建class类，继承Base基类"""
    __tablename__ = 'prd_Comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    goodsid = Column(String(50), index=True, nullable=False)
    brand = Column(String(50), nullable=False)
    comment = Column(String(200))
    join_time = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        """重写显示方法，定义后查询时可以显示数据，不会显示内存地址"""
        Id = self.id
        Goods_id = self.goodsid
        Brand = self.brand
        Comment = self.comment
        Join_time = self.join_time
        return f"id:{Id}, goods_id:{Goods_id}, brand:{Brand}, comment:{Comment}, join_time:{Join_time}"

Base.metadata.create_all(engine)	# 首次可通过此语句创建表
```

\_\_tablename\_\_指定表名，Column()指定字段属性。

### 6\. 常用字段

Column函数常用的**字段类型**有：

```css
常用字段名    python类型    mysql类型    说明
Integer       int           int          整数
Float         float         float        小数
Boolean       bool          tinyint      极小范围的整数
String        str           varchar      字符串，必须限定长度
Text          str           text         文本类型，最大64KB
LongText      str           longtext     文本类型，最大4BG
Date          date          date         只有日期
Time          time          time         只有时间
DateTime      datetime      datetime     日期和时间
```

### 7\. 常用属性

Column函数常用的**字段属性**有：

```css
常用属性名      说明
primary_key     主键，默认自增
unique          唯一
nullable        非空
default         默认
index           索引
```

### 8\. 查看表信息

查看创建好的表信息

```python
ProductComment.__table__  # 表名.__table__
```

## 三、数据操作

### 9\. 创建实例

ProductComment为class类方法，通过调用类方法创建实例。

```python
NewComment = ProductComment(goodsid="123456789", brand="abcd", comment="这是一条评论")
```

### 10\. 创建会话

要真正应用类对象操作数据表，还需要一个Session对象，**ORM对数据库的入口即Session**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@localhost:3306/apptest", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
```

### 11\. 增加数据

主要用.add( )方法，括号内放创建好的实例数据。

```python
from sqlalchemy import create_engine  # 导入连接数据库函数
from sqlalchemy.ext.declarative import declarative_base  # 导入映射声明函数
from sqlalchemy import Column, String, Integer, DateTime  # 导入创建字段函数及字段类型
from datetime import datetime  # 时间库，用于获取当前时间

engine = create_engine("mysql+pymysql://user:password@localhost:3306/database",echo=True) # 实例化数据库连接
Base = declarative_base()  # 实例化ORM的基类
Session = sessionmaker(bind=engine)
session = Session()

class ProductComment(Base):
    __tablename__ = 'prd_Comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    goodsid = Column(String(50), index=True, nullable=False)
    brand = Column(String(50), nullable=False)
    comment = Column(String(200))
    join_time = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        Id = self.id
        Goods_id = self.goodsid
        Brand = self.brand
        Comment = self.comment
        Join_time = self.join_time
        return f"id:{Id}, goods_id:{Goods_id}, brand:{Brand}, comment:{Comment}, join_time:{Join_time}"

# 增加数据
# 创建数据实例，id是自增的，可以不写；join_time默认当前时间，也可以不写
NewComment = ProductComment(goodsid="123456789", brand="abcd", comment="这是一条评论") 
session.add(NewComment)  #  添加数据
session.commit()  # 最后需要调用commit()方法提交事务。
```

增加多条数据可以用.add\_all( [ ] ), 数组内为创建好的实例数据

```python
# 增加多条数据
com1 = ProductComment(goodsid="682779140960", brand="国产品牌", sku="蓝宝石-紫色款", comment="这是一条评论", com_date="2022-11-13", user_id="1193348147545")  # 创建多条数据实例
com2 = ProductComment(goodsid="682779140961", brand="美国品牌", sku="蓝宝石-白色款", comment="这也是一条评论", com_date="2022-11-14", user_id="1193348147545")
com3 = ProductComment(goodsid="682779140962", brand="英国品牌", sku="蓝宝石-绿色款", comment="这又是一条评论", com_date="2022-11-13", user_id="1193348147545")
session.add_all([com1, com2, com3])
session.commit()
```

### 12\. 删除数据

主要用.delete( )方法，通过.query( ).filter( ).first( )方法获取一行数据后删除。

```python
from sqlalchemy import create_engine  # 导入连接数据库函数
from sqlalchemy.ext.declarative import declarative_base  # 导入映射声明函数
from sqlalchemy import Column, String, Integer, DateTime  # 导入创建字段函数及字段类型
from datetime import datetime  # 时间库，用于获取当前时间

engine = create_engine("mysql+pymysql://user:password@localhost:3306/database",echo=True) # 实例化数据库连接
Base = declarative_base()  # 实例化ORM的基类
Session = sessionmaker(bind=engine)
session = Session()

# 继承Base基类
class ProductComment(Base):
    __tablename__ = 'prd_Comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    goodsid = Column(String(50), index=True, nullable=False)
    brand = Column(String(50), nullable=False)
    comment = Column(String(200))
    join_time = Column(DateTime, nullable=False, default=datetime.now)

# 删除数据
# .query()查询数据表.filter()过滤函数.first()选取第一个
result = session.query(ProductComment).filter(ProductComment.goodsid=="123456789").first()
session.delete(result)  # 删除数据
session.commit()  # 提交事务
```

按条件删除数据，支持批量删除

```python
session.query(ProductComment).filter(ProductComment.goodsid=="686004773552").delete()
session.commit()
```

### 13\. 修改数据

直接修改数据，批量可以使用for循环

```python
result = session.query(ProductComment).filter(ProductComment.goodsid=="123456789").first()
result.brand = "国产品牌"
session.commit()

# 通过for循环修改
result = session.query(ProductComment).filter(ProductComment.sku=='兰博基尼').all()
for i in result:
    if i.id%2 == 0:  # 隔行修改
        result = session.query(ProductComment).filter(ProductComment.goodsid==i.id).first()
        result.brand = "国产品牌"
        session.commit()
```

按条件修改数据，支持批量修改

```python
session.query(ProductComment).filter(ProductComment.sku=='兰博基尼').update({'goodsid': '686004773552', 'brand': 'Abc'})
session.commit()
```

### 14\. 查询数据

```python
# 查询数据
query = session.query(ProductComment).all()  # 返回全部
print(query)
result = session.query(ProductComment).filter(ProductComment.comment=='这是一条评论').first()  # 返回首个
print(result)
```

### 15\. 模糊查询

相对于精确查询，模糊查询的匹配范围更广

```python
# 模糊查询
query = session.query(ProductComment).filter(ProductComment.comment.like("%评论%")).all()
print(query)
```

### 16\. 高级查询

数据库筛选时的逻辑判断

```python
# and 操作
query_and = session.query.filter(table_name.column_name == 'python', User.id > 1)  # filter()中设置多个表达式
# or 操作
query_or = session.query.filter(or_(table_name.column_name == 'python', User.id > 1)) # filter()中写or_()
# in 操作
query_in = session.query.filter(table_name.column_name.in_(["python", "C"]))  # filter()中写“表名.字段名.in([数组])”
# not in 操作
query_in = session.query.filter(~table_name.column_name.in_(["python", "C"]))  # 在 in 操作的基础加上运算符‘~’。
```

### 17\. 限制查询

如果数据库内容较多，可以限制分页查询，用到函数: limit、offset、slice

```python
# limit 限制只查询前几条数据
context = session.query(ProductComment).filter(ProductComment.goodsid=='123456789').limit(10).all()
for v in context:
    print(v.id)

# offset 限制过滤掉前面多少条，可指定从第几条开始查询。
context = session.query(ProductComment).filter(ProductComment.goodsid=='123456789').offset(50).limit(10).all()
for v in context:
    print(v.id)

# slice 限制从第几条到第几条开始查询，offset()和limit()的效果集合
context = session.query(ProductComment).filter(ProductComment.goodsid=='123456789').slice(50, 60).all()
for v in context:
    print(v.id)
```