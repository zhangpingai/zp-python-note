"""
print(内容, 内容, ..., ..., 内容,..., end=?)
end是print的一个形式参数，它决定了输出内容的最后是什么
默认我们没有使用end参数，则它的值默认是：end="\n"
如果不需要自动带有\n效果，可以用end=?修改，比如end="" 最后什么都不加
"""
# 这是print语句的默认效果
print("hello", end="\n")
print("world", end="\n")
# 如果要求不换行，可以
print("hello", end="")
print("world", end="")
print()
# \t制表符 相当于键盘按tab键，默认按4个宽度补齐空格
print("abc\t\t你好")
print("a\t\t你好")
print("abcde\t你好")
