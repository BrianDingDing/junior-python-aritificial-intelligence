"""
    数组掩码操作
    布尔掩码：掩码数组mask中, 值为bool值
    索引掩码: 掩码数组mask中, 值为索引值
"""
import numpy as np

ary = np.arange(1, 101)

# 求100以内的偶数
mask = (ary % 2) == 0
print(ary[mask])

# 求100以内, 能同时被3和7整除数字
mask1 = (ary % 3 == 0) & (ary % 7 == 0)
print(ary[mask1])

data1 = ary[ary % 3 == 0]
print(data1[data1 % 7 == 0])

print('---' * 30)
data = np.array(['BYD', 'BMW', 'BENZ', 'XiaoPeng', 'Audi'])
mask = [0, 3, 1, 2, 4]
print(data[mask])

mask = [0, 0, 0, 1, 1, 1, 2]
print(data[mask])
