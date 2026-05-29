

money = 1000
name = "王大锤"
salary = 100

# 扩展语法：()表示内部的内容是整体，哪怕换行了也是整体
message = ("我是" + name + "，钱包有" + str(money) +
           "元，今天发放工资" + str(salary) +
           "元，目前钱包有" + str(money+salary) + "元")
print(message)
