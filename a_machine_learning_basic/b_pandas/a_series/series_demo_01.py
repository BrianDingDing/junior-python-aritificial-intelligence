"""
    Series创建
"""

import pandas as pd
import numpy as np

# 1. 通过列表创建Series
s = pd.Series([100, 90, 80, 70])
print(s)  # 一维数据; 0,1,2,3是Series索引

# 创建Series, 创建自定义索引
s1 = pd.Series(['张三', '李四', '王五', '赵柳'],
               index=[100, 101, 102, 103])
print(s1)
print(s1[102])  # 取值

# 2. 通过字典创建Series
data = {'100': '张三', '101': '李四', '102': '王五'}
s2 = pd.Series(data)
print(s2)

# 3. 通过标量创建Series
# 创建10个元素，值都是5
s3 = pd.Series(5, index=np.arange(10))
print(s3)
