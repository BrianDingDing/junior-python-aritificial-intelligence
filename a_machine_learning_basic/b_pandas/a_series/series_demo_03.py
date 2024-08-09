"""
    Series属性
"""
import pandas as pd

data = pd.Series([100, 90, 80], index=['zs', 'ls', 'ww'])
print(data.values)  # [100  90  80], 返回一个ndarray一维数组
print(data.index)  # Index(['zs', 'ls', 'ww'], dtype='object'), object是字符串
print(data.ndim)  # 1
print(data.dtype)  # int64
print(data.shape)  # (3,)
