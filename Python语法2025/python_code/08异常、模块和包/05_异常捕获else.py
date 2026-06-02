"""
如果抓住异常了，则处理
如果没异常呢？也可以有处理
"""

try:
    print(1)
except Exception as e:
    print("有问题了, ", e)
else:
    print("一切正常")
