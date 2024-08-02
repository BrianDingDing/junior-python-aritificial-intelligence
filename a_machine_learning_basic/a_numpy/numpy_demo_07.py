"""
    多维数组切片操作
    切片不降低维度, 索引会降低一个维度.
"""
import numpy as np

ary = np.arange(1, 28).reshape(9, 3)

# 前两行前两列
print(ary[:2, :2])

# 最后一行的后两列
print(ary[-1, -2:])  # 一维数组
print(ary[-1:, -2:])  # 二维

# 拆分ary, x是二维数据, y是一维数据
# 所有行，不要最后一列(二维)
x = ary[:, :-1]
# 所有行，只要最后一列(一维)
y = ary[:, -1]
print(x)
print(y)
