"""
    测试numpy中的时间类型
"""
import numpy as np

data = np.array(['2021',
                 '2022-01-01',
                 '2023-01-01 08:08:08',
                 '1970-01-01',
                 '1970-01-02'])
print(data.dtype)  # 字符串 U19

# 字符串 -> 日期, 精确到的部分: YMDhms
dates = data.astype('datetime64[D]')
print(dates)

# 日期 -> 数值
res = dates.astype('int64')
print(res)
