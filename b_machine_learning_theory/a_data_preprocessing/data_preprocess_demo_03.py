"""
    归一化
"""
import numpy as np

raw_sample = np.array([[10.0, 20.0, 5.0],
                       [8.0, 10.0, 1.0]])

nor_sample = raw_sample.__copy__()

for row in nor_sample:
    row /= abs(row).sum()

print(nor_sample)

print('==' * 30)

# 基于sklearn提供的API实现归一化
import sklearn.preprocessing as sp

res = sp.normalize(raw_sample, norm='l1')
print(res)
