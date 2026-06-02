def f02():
    print("02start")
    open("asd", "r")
    print("02end")


def f01():
    print("01start")
    f02()
    print("01end")


def main():
    f01()


main()
# try:
#     main()
# except Exception as e:
#     print("有异常：", e)
