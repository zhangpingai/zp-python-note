**mitmproxy**是一个代理工具（软件安装 或 **Python模块安装**），实现代理请求（拦截请求或修改请求）。

  

![](assets/15-mitmproxy/15-mitmproxy-1.png)

  

# 1.安装报错

  

基于 Python3.9.10 解释器创建了个虚拟环境，然后在虚拟环境中安装 `mitmproxy`

  

```plain
pip install mitmproxy
```

  

报错信息：

  

```plain
return _msvc14_get_vc_env(plat_spec)
File "E:\PycharmProjects\mitmproxy_example\.venv\lib\site-packages\setuptools\msvc.py", line 270, in _msvc14_get_vc_env
raise distutils.errors.DistutilsPlatformError(
setuptools._distutils.errors.DistutilsPlatformError: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.mi
crosoft.com/visual-cpp-build-tools/
```

  

需要去下载`Visual C++ Build Tools for Visual Studio 2015`安装到电脑，然后再重新 `pip install mitmproxy` 才行。

  

[https://my.visualstudio.com/Downloads?q=Visual Studio 2015 update 3](https://my.visualstudio.com/Downloads?q=Visual%20Studio%202015%20update%203)

  

![](assets/15-mitmproxy/15-mitmproxy-2.png)

  

解压 `mu_visual_cpp_build_tools_2015_update_3_x64_dvd_dfd9a39c.iso`文件，然后默认安装。

  

![](assets/15-mitmproxy/15-mitmproxy-3.png)

  

再次安装成功：

  

```plain
pip install mitmproxy
```

  

![](assets/15-mitmproxy/15-mitmproxy-4.png)

  

# 2.Https请求

  

如果想要让**mitmproxy**支持：http和**https**请求，就需要安装证书。

  

![](assets/15-mitmproxy/15-mitmproxy-5.png)

  

## 2.1 启动 Mitmproxy

  

启动mitmproxy，去本地用户目录中寻找证书。

  

```plain
>>>mitmdump -q  -p 8888 -s v1.py
```

  

![](assets/15-mitmproxy/15-mitmproxy-6.png)

  

```python
from mitmproxy import http
from mitmproxy.http import Request

def request(flow: http.HTTPFlow):
    print("请求->", flow.request.path)

def response(flow: http.HTTPFlow):
    pass
```

  

## 2.2 获取证书

  

### 1.本地读取

  

在电脑 `C:\Users\Administrator\.mitmproxy` 中去获取。

  

![](assets/15-mitmproxy/15-mitmproxy-7.png)

  

### 2.代理下载

  

在电脑上配置mitmproxy为代理，访问 `http://mitm.it/`下载证书。

  

![](assets/15-mitmproxy/15-mitmproxy-8.png)

  

![](assets/15-mitmproxy/15-mitmproxy-9.png)

  

## 2.3 安装证书

  

![](assets/15-mitmproxy/15-mitmproxy-10.png)

  

![](assets/15-mitmproxy/15-mitmproxy-11.png)

  

![](assets/15-mitmproxy/15-mitmproxy-12.png)

  

![](assets/15-mitmproxy/15-mitmproxy-13.png)

  

![](assets/15-mitmproxy/15-mitmproxy-14.png)

  

![](assets/15-mitmproxy/15-mitmproxy-15.png)

  

## 2.4 运行测试

  

![](assets/15-mitmproxy/15-mitmproxy-16.png)

  

# 3.请求

  

![](assets/15-mitmproxy/15-mitmproxy-17.png)

  

## 3.1 读取请求

  

```python
from mitmproxy import http
from mitmproxy.http import Request

def request(flow):
    print("请求-->", flow.request.url)
    print("请求-->", flow.request.host)
    print("请求-->", flow.request.path)
    print("请求-->", flow.request.query)
    print("请求-->", flow.request.cookies)
    print("请求-->", flow.request.headers)
    print("请求-->", flow.request.method)
    print("请求-->", flow.request.content)

def response(flow: http.HTTPFlow):
    pass
```

  

```plain
>>>mitmdump -q  -p 8888 -s v1.py
```

  

![](assets/15-mitmproxy/15-mitmproxy-18.png)

  

## 3.2 修改请求

  

```python
from mitmproxy import http
from mitmproxy.http import Request
from mitmproxy.http import HTTPFlow

def request(flow: HTTPFlow):
    flow.request.url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20"

def response(flow: http.HTTPFlow):
    pass
```

  

![](assets/15-mitmproxy/15-mitmproxy-19.png)

  

## 3.4 拦截请求

  

可以拦截请求，并返回指定内容：

  

```python
from mitmproxy import http
from mitmproxy.http import Request
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Response

def request(flow: HTTPFlow):
    if flow.request.url.startswith("https://dig.chouti.com/"):
        flow.response = Response.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )

def response(flow: http.HTTPFlow):
    pass

# mitmdump -q  -p 8888 -s v1.py
```

  

![](assets/15-mitmproxy/15-mitmproxy-20.png)

  

拦截的形式，也可以是kill当前请求：

  

```python
from mitmproxy import http
from mitmproxy.http import Request
from mitmproxy.http import HTTPFlow

def request(flow: HTTPFlow):
    if flow.request.url.startswith("https://dig.chouti.com/"):
        flow.kill()

def response(flow: http.HTTPFlow):
    pass

# mitmdump -q  -p 8888 -s v1.py
```

  

![](assets/15-mitmproxy/15-mitmproxy-21.png)

  

## 3.3 案例：免账号登录

  

-   正常账号登录：获取凭证

-   集成mitmproxy

-   配置代理

  

```plain
武沛齐：192.168.140.1    8888
 舍友：...
```

  

![](assets/15-mitmproxy/15-mitmproxy-22.png)

  

![](assets/15-mitmproxy/15-mitmproxy-23.png)

  

```python
from mitmproxy import http
from mitmproxy.http import Request
from mitmproxy.http import HTTPFlow

def request(flow: HTTPFlow):
    print(flow.request.url)
    flow.request.cookies = [
        ("token","eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqaWQiOiJjZHVfNDU3OTI2NDUxNTUiLCJleHBpcmUiOiIxNzA0MzI5NDY5OTMyIn0.8n_tWcEHXsBSXWIY9rBoGWwaLPF8iWIruryhKTe5_ks")
    ]

def response(flow: http.HTTPFlow):
    pass

# mitmdump -q  -p 8888 -s v1.py
```

  

![](assets/15-mitmproxy/15-mitmproxy-24.png)

  

![](assets/15-mitmproxy/15-mitmproxy-25.png)

  

# 4.响应

  

![](assets/15-mitmproxy/15-mitmproxy-26.png)

  

## 4.1 读取响应

  

```python
from mitmproxy import http
from mitmproxy.http import Request
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Response

def response(flow: http.HTTPFlow):
    print(flow.request.url)
    
    print(flow.response.status_code)
    print(flow.response.cookies)
    print(flow.response.headers)
    print(flow.response.content)

# mitmdump -q  -p 8888 -s v1.py
```

  

![](assets/15-mitmproxy/15-mitmproxy-27.png)

  

## 4.2 修改响应

  

```python
from mitmproxy import http
from mitmproxy.http import Request
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Response

def response(flow: http.HTTPFlow):
    print(flow.request.url)
    print(flow.response.status_code)
    print(flow.response.cookies)
    print(flow.response.headers)
    # print(flow.response.content)
    
    flow.response = Response.make(
        200,  # (optional) status code
        b"Hello World",  # (optional) content
        {"Content-Type": "text/html"}  # (optional) headers
    )

# mitmdump -q  -p 8888 -s v1.py
```

  

![](assets/15-mitmproxy/15-mitmproxy-28.png)