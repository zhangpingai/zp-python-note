

def check_age(age):
    if age < 18:
        return None
    return "SUCCESS"        # 在if中有内容的字符串算作True   空字符串算作False


if check_age(10):
    print("成年人")
else:
    print("未成年人")


"""
只要不是0、False、None、空字符串
其余都是True
"""
