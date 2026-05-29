# 介绍

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-1.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-2.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-3.png)

## 同步与异步

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-4.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-5.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-6.png)

## 类型提示与验证和可交互式文档

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-7.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-8.png)

## 第一个FastAPI程序

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-9.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-10.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-11.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-12.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-13.png)

# 路由

## 路由介绍

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-14.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-15.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-16.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-17.png)

## 代码

```python
from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World888"}

# 访问 /hello  响应结果 msg: 你好 FastAPI
@app.get("/hello")
async def get_hello():
    return {"msg": "你好 FastAPI"}
```

## 练习

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-18.png)

# 请求参数

## 请求参数介绍

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-19.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-20.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-21.png)

## 请求参数分类

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-22.png)

### 路径参数

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-23.png)

  

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-24.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-25.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-26.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-27.png)

### 路径参数代码

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/book/{id}")
async def get_book(id: int = Path(..., gt=0, lt=101, description="书籍id，取值范围1-100")):
    return {"id": id, "title": f"这是第{id}本书"}

# 需求：查找书籍的作者，路径参数 name，长度范围 2-10
@app.get("/author/{name}")
async def get_name(name: str = Path(..., min_length=2, max_length=10)):
    return {"msg": f"这是{name}的信息"}

```

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-28.png)

### 查询参数

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-29.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-30.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-31.png)

### 查询参数代码

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 需求 查询新闻 → 分页，skip: 跳过的记录数， limit：返回的记录数 10
@app.get("/news/news_list")
async def get_news_list(
    skip: int = Query(0, description="跳过的记录数", lt=100),
    limit: int = Query(10, description="返回的记录数")
):
    return {"skip": skip, "limit": limit}
```

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-32.png)

### 请求体参数

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-33.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-34.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-35.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-36.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-37.png)

### 请求体参数代码

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 注册： 用户名和密码 → str
class User(BaseModel):
    username: str = Field(default="张三", min_length=2, max_length=10, description="用户名，长度要求2-10个字")
    password: str = Field(min_length=3, max_length=20)

@app.post("/register")
async def register(user: User):
    return user

```

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-38.png)

## 请求与响应

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-39.png)

### 响应类型

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-40.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-41.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-42.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-43.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-44.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-45.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-46.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-47.png)

### 响应 HTML 格式代码

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 接口 → 响应 HTML 代码
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>这是一级标题</h1>"
```

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-48.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-49.png)

### 响应类型-文件格式代码

```python
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 接口： 返回一张图片内容
@app.get("/file")
async def get_file():
    path = "./files/1.jpeg"
    return FileResponse(path)

```

### 自定义响应数据格式

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-50.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-51.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-52.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-53.png)

### 自定义响应数据格式代码

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 需求：新闻接口 → 响应数据格式 id、title、content
class News(BaseModel):
    id: int
    title: str
    content: str

@app.get("/news/{id}", response_model=News)
async def get_news(id: int):
    return {
        "id": id,
        "title": f"这是第{id}本书",
        "content": "这是一本好书"
    }

```

### FastAPI内置响应类型

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-54.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-55.png)

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-56.png)

# 异常处理

![image.png](assets/第一章_FastAPI入门/第一章_FastAPI入门-57.png)