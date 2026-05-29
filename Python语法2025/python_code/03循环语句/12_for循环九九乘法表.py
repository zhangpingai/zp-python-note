
# 外层控制行  内层控制列
# 外层 9行

for row in range(1, 10):
    for col in range(1, row + 1):
        print(f"{col} * {row} = {col*row}", end="\t")

    print()
