u闭包

u装饰器

u设计模式

u多线程

u网络编程

u正则表达式

u递归

u

通过全局变量account\_amount来记录余额

尽管功能实现是ok的，但是仍有问题：

•代码在命名空间上（变量定义）不够干净、整洁

•全局变量有被修改的风险

如何解决？

•将变量定义在函数内部是行不通的

•我们需要使用闭包

  

![image.png](assets/16-【拓展】Python高阶技巧/16-【拓展】Python高阶技巧-1.png)

![image.png](assets/16-【拓展】Python高阶技巧/16-【拓展】Python高阶技巧-2.png)