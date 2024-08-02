"""
    ndarray对象的基本属性
"""
import numpy as np

ary = np.arange(1, 10)
# shape如果有几个数据就几维数据
print(ary.shape)  # (9,)

ary.shape = (3, 3)
print(ary)

ary.shape = (1, 3, 3)  # 1页3行3列
print(ary)

ary.shape = (9,)
print(ary)

print('---' * 30)

ary1 = np.array([1, 2, 3, 4, 5, 6], dtype='int32')
print(ary1)
print(ary1.dtype)

# 并没有修改元素类型, 而是暴力的修改了解析方式，即用float32解析int32
# ary1.dtype = 'float32'
# print(ary1)

# astype接口不会修改原始数据类型, 因此需要要对修改数据进行赋值.
ary2 = ary1.astype('float32')
print(ary2)
print(ary2.dtype)

ary2.shape = (2, 3)

print('size:', ary2.size)  # 6
# 对于二维数组, 相当于查看多少个一维数组.
print('length', len(ary2))  # 2
