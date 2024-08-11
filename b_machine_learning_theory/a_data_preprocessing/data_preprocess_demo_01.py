"""
    均值移除
"""
import numpy as np

raw_sample = np.array([[3.0, -100.0, 2000.0],
                       [0.0, 400.0, 3000.0],
                       [1.0, -400.0, 2000.0]])

std_sample = raw_sample.__copy__()

for col in std_sample.T:
    col_mean = col.mean()
    col_std = col.std()
    # 用每个数据减去当前列的平均值, 得到离差.
    col -= col_mean
    # 用每个数据的离差 / 原始数据的对应列的标准差.
    col /= col_std

print(std_sample)
print(std_sample.mean(axis=0))
print(std_sample.std(axis=0))

print('==' * 30)

# 基于sklearn提供的API实现均值移除
import sklearn.preprocessing as sp  # 数据预处理

res = sp.scale(raw_sample)
print(res)
print(res.mean(axis=0))
print(res.std(axis=0))
