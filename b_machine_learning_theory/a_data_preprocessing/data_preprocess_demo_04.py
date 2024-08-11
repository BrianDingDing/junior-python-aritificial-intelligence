"""
    二值化
"""
import numpy as np

raw_sample = np.array([[45.5, 60.0, 99.9],
                       [12.3, 23.4, 56.7],
                       [68.8, 98.8, 12.1]])

bin_sample = raw_sample.__copy__()

# 阈值为60, 设定为60
# 方法一
# bin_sample[bin_sample <= 60] = 0
# bin_sample[bin_sample > 60] = 1
# print(bin_sample)

# 方法二: np.where(条件, 条件成立的返回值, 条件不成立的返回值)
res = np.where(bin_sample > 60, 1.0, 0.0)
print(res)

print("==" * 30)

# 基于sklearn实现二值化
import sklearn.preprocessing as sp

bin = sp.Binarizer(threshold=60)
res = bin.transform(raw_sample)
print(res)
