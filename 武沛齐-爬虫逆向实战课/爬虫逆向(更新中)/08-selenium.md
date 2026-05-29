# 代码

[driver.rar](https://www.yuque.com/attachments/yuque/0/2024/rar/25744277/1707194644810-0eb81fbb-947e-4cab-b0b0-7bf7eb95c207.rar)[1.快速上手.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654258-2a8ca775-e281-4eb3-8f24-b0c21a668f76.py)[2.寻找.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654259-18f2ac78-c692-41d1-b427-adfcc33dd7a8.py)[3.操作.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654259-db619db0-c580-4d93-a235-15e967eb45ae.py)[4.脚本.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654244-98dbc532-71b6-4eca-a26e-69d008abc64b.py)[5.值相关.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654263-70dd2403-1a7b-47e3-9cd0-4c84047295af.py)[6.bs4.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654617-ca601c4f-ef41-46aa-91a6-5e4cfb6bde66.py)[7.cookie.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654649-243f89ba-edf5-46fe-a08c-c37a16efb72c.py)[8.代理.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654645-357eb39c-a5b4-461e-8d55-fb5dbb8d6c6e.py)[9.特征.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654658-4e74488d-5bb7-4263-b23e-82cb5a67fd4a.py)[10.无头.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194654670-edbca4de-0ce2-4001-adb1-8c0e2a6fe014.py)[11.jd.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194655158-21530ccc-933a-4890-aad1-7e96860d581b.py)[12.dm.py](https://www.yuque.com/attachments/yuque/0/2024/py/25744277/1707194655037-2c0b25e5-8918-49d5-b4b1-1c2911039d8c.py)

![](assets/08-selenium/08-selenium-1.png)

  

# 1.selenium自动化

  

selenium可以操作浏览器，在浏览器页面上实现：点击、输入、滑动 等操作。

  

不同于selenium自动化，逆向本质是：

  

-   分析请求，例如：请求方法、请求参数、加密方式等。

-   用代码模拟请求去实现同等功能。

  

**逆向 vs 自动化Selenium**

  

-   Selenium，【优】简单不需要逆向，只需要控制浏览器去执行预设的操作即可；【缺点】性能差，不利于批量实现

-   逆向，          【优】算法逆向出来后，性能好且利于批量实现；                               【缺点】语法难搞的js加密算法，不容易逆向

  

# 2.必备操作

  

## 2.1 模块 & 驱动

  

-   安装模块

```plain
pip3.11 install selenium
```

-   下载驱动

```plain
Selenium想要控制谷歌、火狐、IE、Edage等浏览器，必须要使用对应的驱动才行。【Selenium】->【驱动】->【浏览器】
	【Selenium】->【火狐驱动】->【火狐浏览器】
	【Selenium】->【谷歌驱动】->【谷歌浏览器】

谷歌驱动的下载：
	   114及之前版本： http://chromedriver.storage.googleapis.com/index.html
	117/118/119版本： https://googlechromelabs.github.io/chrome-for-testing/
	
浏览器版本的获取：
	在谷歌浏览器上访问 chrome://version/   例如：119.0.6045.200 (正式版本) （64 位） (cohort: Stable)
```

-   快速使用

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

time.sleep(5)
driver.close()
```

  
![](assets/08-selenium/08-selenium-2.png)

  

## 2.2 寻找标签

  

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('打开网址')

# find_element  find_elements
tag = driver.find_element(By.ID, "user")
tag = driver.find_element(By.CLASS_NAME, "c1")
tag = driver.find_element(By.TAG_NAME, "div")
tag = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/div[1]/span[2]")
tag = driver.find_element(By.XPATH, '//*[@id="geetest-wrap"]//input[@name="tel"]')

tag_list = driver.find_elements(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a")
for tag in tag_list:
    print(tag)

time.sleep(5)
driver.close()
```

  

**示例：5xclass.cn**

  

![](assets/08-selenium/08-selenium-3.png)

  

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://www.5xclass.cn/')

# 根据ID寻找
tag = driver.find_element(By.ID, "bs-example-navbar-collapse-1")
print(tag.text)
print(10 * "-")

# 根据类名寻找
tags = driver.find_elements(By.CLASS_NAME, "panel-heading")
for tag in tags:
    print(tag.text)
print(10 * "-")

# 根据标签名称寻找
tags = driver.find_elements(By.TAG_NAME, "li")
for tag in tags:
    print(tag.text)
print(10 * "-")

# 根据XPATH寻找
tag = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[1]")
print(tag.text)
print(10 * "-")

# 根据XPATH寻找
tag = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[1]/a')
print(tag.text)
print(10 * "-")

# 根据XPATH寻找多个
tags = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a')
for tag in tags:
    print(tag.text)
print(10 * "-")

# 根据父子关系嵌套寻找
parent = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div')
tags = parent.find_elements(By.XPATH, "div[@class='course']/a")
for tag in tags:
    print(tag.text)

time.sleep(5)
driver.close()
```

  

## 2.3 执行操作

  

常见的执行操作：点击、输入

  

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

# 1.点击短信登录
time.sleep(3)
sms_btn = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()  # 点击

# 2.输入账号
phone_txt = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input'
)
phone_txt.send_keys("18630087660")  # 输入

time.sleep(55)
driver.close()
```

  

![](assets/08-selenium/08-selenium-4.png)

  

## 2.4 执行JavaScript

  

如果【选择标签】【执行操作】这种操作起来比较繁琐，也可以直接在页面上去执行js代码实现功能。

  

![](assets/08-selenium/08-selenium-5.png)

  

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

# #############  1.点击短信登录 #############
time.sleep(3)
sms_btn = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()

# #############  2.输入账号 #############
phone_txt = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input'
)
phone_txt.send_keys("18630087660")

# ############# 3.选择国家 #############
time.sleep(2)
driver.execute_script('document.querySelector(".area-code-select").children[18].click()')

# ############# 4.读取cookie #############
data_string = driver.execute_script('return document.cookie;')   # return document.title;
print(data_string)

# ############# 5.读取cookie #############
cookie_list = driver.get_cookies()
print(cookie_list)

time.sleep(2550)
driver.close()
```

  

## 2.5 等待

  

如果页面加载比较慢，需要等待某个元素加载成功后，再执行某些操作。

  

**示例1：基于lambda表达式**

  

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

# #############  方式1：点击短信登录 #############
time.sleep(3)
sms_btn = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()

# #############  方式2：点击短信登录（推荐） #############
sms_btn = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
))
sms_btn.click()
```

  

**示例2：自定义函数**

  

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

def func(dv):
    print("无返回值，则间隔0.5s执行一次此函数；如有返回值，则复制给sms_btn变量")
    # <div xxx="123" id="uuu"></div>
    # <img src="..."/>
    tag = dv.find_element(
        By.XPATH,
        '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
    )
    img_src = tag.get_attribute("xxx")
    if img_src:
        return tag
    return

sms_btn = WebDriverWait(driver, 30, 0.5).until(func)
sms_btn.click()

time.sleep(250)
driver.close()
```

  

**示例3：全局配置**

  

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 后续找元素时，没找到时则等待10去寻找（一旦找到则继续）
driver.implicitly_wait(30)

driver.get('https://passport.bilibili.com/login')

sms_btn = driver.find_element(
    By.XPATH,
    # '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
    '//*[@id="xxxxxxxxxapp"]/div[2]/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()
print("找到了")
time.sleep(250)
driver.close()
```

  

## 2.6 获取值

  

当找到某个标签之后，想要获取标签内部值。

  

**示例1：文本和属性**

  

例如：`<a id='x1' class="info mine" href="5xclass.cn">武沛齐</a>`

  

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://www.5xclass.cn')

tag = driver.find_element(
    By.XPATH,
    '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a[1]'
)
print(tag.text)
print(tag.get_attribute("target"))
print(tag.get_attribute("data-toggle"))

driver.close()
```

  

**示例2：获取值**

  

例如：`<input type='text' value="?" placeholder="?" />`

  

例如：`<select ><option value='1'>北京</option> </option value='2'>上海</option> </select>` ，获取select标签的value属性

  

```python
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://www.bilibili.com/')

time.sleep(10)

tag = driver.find_element(
    By.XPATH,
    '//*[@id="nav-searchform"]/div[1]/input'
)
print(tag)
print(tag.text)
print(tag.get_attribute("placeholder"))
print(tag.get_attribute("value"))

time.sleep(1000)
driver.close()
```

  

**示例3：选择相关**

  

```html
<input type="radio" name="findcar" value="1" checked="">新车
<input type="radio" name="findcar" value="2">二手机
```

  

![](assets/08-selenium/08-selenium-6.png)

  

```python
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://www.autohome.com.cn/beijing/')

# ############### 1.单独找到每一个 ###############
tag = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]/label[1]/span/input'
)
print(tag.get_property("checked")) # True

tag = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]/label[2]/span/input'
)
print(tag.get_property("checked")) # False

# ############### 2.循环找到每一个 ###############
parent = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]'
)

tag_list = parent.find_elements(
    By.XPATH,
    'label/span/input'
)
for tag in tag_list:
    print( tag.get_property("checked"), tag.get_attribute("value") )

driver.close()
```

  

## 2.7 源码+bs4

  

打开页面后，如果基于selenium不太容易定位和寻找，也可以结合bs4来进行寻找。

  

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://car.yiche.com/')

html_string = driver.page_source

soup = BeautifulSoup(html_string, features="html.parser")
tag_list = soup.find_all(name="div", attrs={"class": "item-brand"})
for tag in tag_list:
    child = tag.find(name='div', attrs={"class": "brand-name"})
    print(child.text)

driver.close()
```

  

## 2.8  携带Cookie

  

```python
driver.add_cookie({'name': 'foo', 'value': 'bar'})
```

  

```python
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 注意：一定要先访问，不然Cookie无法生效
driver.get('https://dig.chouti.com/about')

# 加cookie
driver.add_cookie({
    'name': 'token',
    'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqaWQiOiJjZHVfNDU3OTI2NDUxNTUiLCJleHBpcmUiOiIxNzA0MzI5NDY5OTMyIn0.8n_tWcEHXsBSXWIY9rBoGWwaLPF8iWIruryhKTe5_ks'
})

# 再访问
driver.get('https://dig.chouti.com/')

time.sleep(2000)
driver.close()
```

  

![](assets/08-selenium/08-selenium-7.png)

  

## 2.9 IP检测和代理

  

如果网站进行了IP访问限制，例如：每个IP每天只能操作5次。此时可以选择购买IP，然后在请求时添加代理IP即可，具体步骤：

  

-   购买IP

-   登录购买IP渠道的后台，配置自己IP白名单

-   代码携带代理

  

![](assets/08-selenium/08-selenium-8.png)

  

![](assets/08-selenium/08-selenium-9.png)

  

![](assets/08-selenium/08-selenium-10.png)

  

![](assets/08-selenium/08-selenium-11.png)

  

![](assets/08-selenium/08-selenium-12.png)

  

![](assets/08-selenium/08-selenium-13.png)

  

```python
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 换成自己生成的代理
res = requests.get(url="https://dps.kdlapi.com/api/getdps/?secret_id=o60wwtxvs5ukaqqz18ai&num=1&signature=i6s9shfjfiogat5ijecbyfwwc5grwrzj&pt=1&format=json&sep=1")
proxy_string = res.json()['data']['proxy_list'][0]
print(f"获取代理：{proxy_string}") # "182.106.136.218:40192"

service = Service("driver/chromedriver.exe")

opt = webdriver.ChromeOptions()
# opt.add_argument(f'--proxy-server=222.89.70.40:40001')  # 代理
opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
driver = webdriver.Chrome(service=service, options=opt)

driver.get('https://myip.ipip.net/')

time.sleep(2000)
driver.close()
```

  

## 2.10 特征检测

  

有些网站为了防止selenium，会检测特征，并禁止访问。

  

![](assets/08-selenium/08-selenium-14.png)

  

如果想要正常使用selenium访问，那就需要隐藏浏览器相关的特征。

  

```python
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")

opt = webdriver.ChromeOptions()

opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=opt)

# Selenium在打开任何页面之前，先运行这个Js文件。
with open('driver/hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})

driver.get('https://www.5xclass.cn')

time.sleep(2000)
driver.close()
```

  

## 2.11 无头和其他

  

如果不想显示展示在浏览器上的操作，只想偷偷的在后台运行。

  

```plain
opt.add_argument('--headless')
```

  

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=opt)

driver.get('https://www.5xclass.cn')
tag = driver.find_element(
    By.XPATH,
    '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a[1]'
)
print(tag.text)
print(tag.get_attribute("target"))
print(tag.get_attribute("data-toggle"))

driver.close()
```

  

其他配置：

  

```python
opt.add_argument('--disable-infobars')                    # 禁止策略化
opt.add_argument('--no-sandbox')                          # 解决DevToolsActivePort文件不存在的报错
opt.add_argument('window-size=1920x3000')                 # 指定浏览器分辨率
opt.add_argument('--disable-gpu')                         # 谷歌文档提到需要加上这个属性来规避bug
opt.add_argument('--incognito')                           # 隐身模式（无痕模式）
opt.add_argument('--disable-javascript')                  # 禁用javascript
opt.add_argument('--start-maximized')                     # 最大化运行（全屏窗口）,不设置，取元素会报错
opt.add_argument('--hide-scrollbars')                     # 隐藏滚动条, 应对一些特殊页面
opt.add_argument('lang=en_US')                            # 设置语言
opt.add_argument('blink-settings=imagesEnabled=false')    # 不加载图片, 提升速度
opt.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Androi....')      # 设置User-Agent
opt.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置
```

  

## 2.12 截屏

  

找到某个标签后，可以通过截图的形式保存图片。

  

![](assets/08-selenium/08-selenium-15.png)

  

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://www.5xclass.cn')
tag = driver.find_element(
    By.XPATH,
    '/html/body/div/div[2]/div/div[2]/div/div[2]'
)

# 截图&保存
tag.screenshot("demo.png")

# 截图&图片内容
body = tag.screenshot_as_png
print(body)

# 截图&Base64编码格式图片内容
b64_body = tag.screenshot_as_base64
print(b64_body)

driver.close()
```

  

# 3.案例：x东搜索

  

![](assets/08-selenium/08-selenium-16.png)

  

```python
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 换成自己生成的代理
res = requests.get(url="https://dps.kdlapi.com/api/getdps/?secret_id=o60wwtxvs5ukaqqz18ai&num=1&signature=i6s9shfjfiogat5ijecbyfwwc5grwrzj&pt=1&format=json&sep=1")
proxy_string = res.json()['data']['proxy_list'][0]
print(f"获取代理：{proxy_string}")

service = Service("driver/chromedriver.exe")
opt = webdriver.ChromeOptions()

opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
opt.add_argument('blink-settings=imagesEnabled=false') # 不加载图片

opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=opt)

driver.implicitly_wait(10)

with open('driver/hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})

# 1.打开京东
driver.get('https://www.jd.com/')

# 2.搜索框+输入
tag = driver.find_element(
    By.XPATH,
    '//*[@id="key"]'
)
tag.send_keys("iphone手机")

# 3.点击搜索
tag = driver.find_element(
    By.XPATH,
    '//*[@id="search"]/div/div[2]/button'
)
tag.click()

# 4.查询列表
tag_list = driver.find_elements(
    By.XPATH,
    '//*[@id="J_goodsList"]/ul/li'
)
for tag in tag_list:
    # title = tag.find_element(By.XPATH, 'div/div[@class="p-name p-name-type-2"]//em').text
    title = tag.find_element(By.XPATH, 'div/div[@class="p-name p-name-type-2"]/a/em').text
    print(title)

driver.close()
```

  

# 4.案例：x麦网

  

![](assets/08-selenium/08-selenium-17.png)

  

```python
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 换成自己生成的代理
res = requests.get(
    url="https://dps.kdlapi.com/api/getdps/?secret_id=o60wwtxvs5ukaqqz18ai&num=1&signature=i6s9shfjfiogat5ijecbyfwwc5grwrzj&pt=1&format=json&sep=1")
proxy_string = res.json()['data']['proxy_list'][0]
print(f"获取代理：{proxy_string}")

service = Service("driver/chromedriver.exe")
opt = webdriver.ChromeOptions()
opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
opt.add_argument('blink-settings=imagesEnabled=false')
opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=service, options=opt)
driver.implicitly_wait(10)
with open('driver/hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})

# 1.打开大麦网
driver.get('https://www.damai.cn/')

# 2.搜索框+输入
tag = driver.find_element(
    By.XPATH,
    '//input[@class="input-search"]'
)
tag.send_keys("周杰伦")

# 3.点击搜索
tag = driver.find_element(
    By.XPATH,
    '//div[@class="btn-search"]'
)
tag.click()

# 4.查询列表
tag_list = driver.find_elements(
    By.XPATH,
    '//div[@class="search__itemlist"]//div[@class="items"]'
)
for tag in tag_list:
    title = tag.find_element(By.XPATH, 'div[@class="items__txt"]/div[1]/a').text
    print(title)

time.sleep(2000)
driver.close()
```

  

如果不加代理，访问频繁时会提示验证码，后续讲：滑动验证、文字识别点选验证

  

![](assets/08-selenium/08-selenium-18.png)