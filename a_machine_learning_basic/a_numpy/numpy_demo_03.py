"""
    测试numpy中的时间类型
"""
import numpy as np

data = np.array(['2021',
                 '2022-01-01',
                 '2023-01-01 08:08:08',
                 '1970-01-01',
                 '1970-01-02'])
print(data.dtype)  # 字符串 <U19

# 字符串 -> 日期, 精确到的部分: YMDhms
dates = data.astype('datetime64[D]')
print(dates)

# 日期 -> 数值, 换回距离1970-01-01的天数, 如果是时间日期精确到秒数, 则返回的是1970-01-01 00:00:00的秒数
res = dates.astype('int64')
print(res)
