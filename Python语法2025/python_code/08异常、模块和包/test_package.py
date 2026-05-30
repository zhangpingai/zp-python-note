"""
import 和 from 语句中
.是用来区分层级的
"""
# import my_package.modul1 as m1
# import my_package.modul2 as m2
#
#
# # my_package.modul1.hi()
# # my_package.modul2.haha()
# m1.hi()
# m2.haha()
#
#
# from my_package import modul1
# modul1.hi()
# from my_package.modul1 import hi
# hi()

from my_package import *
modul1.hi()
modul2.haha()

