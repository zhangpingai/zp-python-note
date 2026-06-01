# 双层循环，外层控制行  内层控制列

row = 1  # 外层循环因子

while row <= 9:  # 基于因子的条件

    col = 1  # 内层循环因子
    while col <= row:  # 基于因子的条件
        print(f"{col}*{row}={col * row}", end="\t")
        col += 1  # 内层循环因子更新

    print()  # 外层循环功能，换一行
    row += 1  # 外层循环因子更新

"""
*
**
***
****
*****
"""
