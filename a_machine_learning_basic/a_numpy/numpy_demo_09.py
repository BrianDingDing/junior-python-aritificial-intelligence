"""
    多维数组的组合与拆分
"""
import numpy as np

x = np.arange(1, 7).reshape(2, 3)
y = np.arange(7, 13).reshape(2, 3)

# 垂直合并
res = np.vstack((x, y))
print(res)

# 垂直拆分
x, y = np.vsplit(res, 2)
print(x)
print(y)

print('----' * 30)

# 水平合并
res = np.hstack((x, y))
print(res)

# 垂直拆分
x, y = np.hsplit(res, 2)
print(x)
print(y)

print('----' * 30)

# 深度合并
res = np.dstack((x, y))
print(res)

# 深度拆分, 拆分仍然是三维数据
x, y = np.dsplit(res, 2)
print(x)
print(y)

print('----' * 30)

# 通过axis作为关键字参数指定组合的方向, 取值如下:
# 若待组合的数组都是二维数组:
#   0: 垂直方向组合
#   1: 水平方向组合
# 若待组合的数组都是三维数组:
#   0: 垂直方向组合
#   1: 水平方向组合
#   2: 深度方向组合

x = np.arange(1, 7).reshape(2, 3)
y = np.arange(7, 13).reshape(2, 3)

ary = np.concatenate((x, y), axis=0)
print(ary)
# 通过给出的数组与要拆分的份数，按照某个方向进行拆分，axis的取值同上
ary1 = np.split(ary, 2, axis=0)
print(ary1)