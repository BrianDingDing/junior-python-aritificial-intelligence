"""
    独热编码
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([[1, 3, 2],
                        [7, 5, 4],
                        [1, 8, 6],
                        [7, 3, 9]])

# sparse_output: 稀疏矩阵: 保存不为0的位置
encoder = sp.OneHotEncoder(sparse_output=False, dtype='int32')
res = encoder.fit_transform(raw_samples)
print(res)

# 反向转换
inv_res = encoder.inverse_transform(res)
print(inv_res)
