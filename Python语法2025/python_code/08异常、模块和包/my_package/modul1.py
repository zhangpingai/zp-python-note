
# Python的模块是单例，多次引入只会执行一次
print('执行 modul1')
count = 1

def hi():
    print(f'Hello World! {count}')