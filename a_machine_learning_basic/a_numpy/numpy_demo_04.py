"""
    数组的索引
"""
import numpy as np

ary = np.arange(1, 19)
ary.shape = (2, 3, 3)

# 直接索引取数据，会降低维度
print(ary[0][1][2])  # 6
# 新的写法: ary[页，行，列]
print(ary[0, 1, 2])  # 6

# # 取到三维数组中的每一个元素(每页的每行的每列)
# # 方法一
# ary.shape = (ary.size,)
# for i in ary:
#     print(i, end=' ')

# 方法二
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i, j, k], end=' ')
