"""
    ndarray数组的创建
    np.array(任何可被解释为Numpy数组的逻辑结构)
"""
import numpy as np

# 数组创建第一种
ary = np.array([1, 2, 3, 4, 5, 6])
print(ary)  # [1 2 3 4 5 6]
print(type(ary))  # <class 'numpy.ndarray'>

# 广播机制
# 数组与数值进行计算, 数组中的每个元素分别计算
print(ary * 2)  # [2  4  6  8 10 12]
print(ary == 3)  # [False False  True False False False]
# 数组与数组进行计算, 对应位置对应计算
print(ary * ary)  # [ 1  4  9 16 25 36]

# 数组创建第二种
print('---' * 30)
ary2 = np.arange(1, 10)
print(ary2)  # [1 2 3 4 5 6 7 8 9]
ary3 = np.arange(0.1, 1.1, 0.1)
print(ary3)

# 数组创建第三种
# np.zeros / np.ones(数组元素个数, dtype='类型'); dtype默认是float64
ary4 = np.zeros(shape=10)
print(ary4)

ary5 = np.ones(10)
print(ary5)

# shape(行, 列)
ary6 = np.zeros(shape=(10,))
print(ary6)

ary7 = np.zeros(shape=(2, 5))
print(ary7)

ary8 = np.zeros(shape=(3, 4, 2))
print(ary8)

# np.zeros_like
ary9 = np.zeros_like(ary3)
print(ary9)

# 生成-pi到pi的200个数(等差数列)
# 线性拆分 np.linspace(起始值, 终止值, 个数), 含头也含尾.
ary10 = np.linspace(-np.pi, np.pi, 200)
print(ary10)
