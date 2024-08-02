"""
    ndarray数组维度操作
    视图变维, 复制变维: 不会修改原始数据的维度.
    就地变维: 直接修改原始数据的维度.
"""
import numpy as np

# 1. 视图变维 (数据共享): reshape() 与 ravel(): 直接拉伸成一维数据.
ary = np.arange(1, 19)
bry = ary.reshape(2, 9)

bry[0][0] = 99
print(bry)  # 二维数组
print(ary)  # 还是一维数组, 原始数据维度不变

# 创建一个1,18 shape=(3,6)
ary2 = np.arange(1, 19).reshape(1, 3, 6)
print(ary2)

# ravel() 不管几维数据, 直接拉伸一维数据
ary3 = ary2.ravel()
print(ary3)

# 2. 复制变维 (数据独立): flatten(), 相当于ravel
print('---' * 30)
ary4 = np.arange(1, 9).reshape(2, 2, 2)
bry4 = ary4.flatten()

bry4[0] = 666
print(bry4)
print(ary4)

# 3. 就地变维: 直接改变原数组对象的维度, 不返回新数组.
# 对shape属性进行, 就是就地变维.
ary5 = np.arange(1, 9)
ary5.resize(2, 4)
print(ary5)
