"""
    范围缩放
"""
import numpy as np

raw_sample = np.array([[3.0, -100.0, 2000.0],
                       [0.0, 400.0, 3000.0],
                       [1.0, -400.0, 2000.0]])

std_sample = raw_sample.__copy__()

for col in std_sample.T:
    col_min = col.min()
    col_max = col.max()
    col -= col_min
    col /= (col_max - col_min)

print(std_sample)

print('==' * 30)

# 基于sklearn提供的API实现范围缩放
import sklearn.preprocessing as sp  # 数据预处理

mms = sp.MinMaxScaler()

# mms.fit(raw_sample)
# res = mms.transform(raw_sample)
res = mms.fit_transform(raw_sample)
print(res)
