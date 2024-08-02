"""
    访问索引数据
"""
import pandas as pd
import warnings  # 警告

warnings.filterwarnings('ignore')

# 使用索引检索元素
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# 可以通过索引, 切片, 掩码
# Series中有两套索引(位置索引, 标签索引(自己设置))

# 1. 位置索引
print(s[2])
# 位置切片, 切出来还是series
print(s[:2])
# 掩码
mask = [0, 2, 3]
print(s[mask])

# 2. 标签索引
print(s['d'])
print(s['a':'d'])  # 终止位置也包含的
mask1 = ['d', 'e']
print(s[mask1])

# Series没有反向索引
s = pd.Series([100, 90, 80])
# print(s[-1])

# 但是写了索引的s1[-1]相当于s1[ww]
s1 = pd.Series([100, 90, 80], index=['zs', 'ls', 'ww'])
print(s1[-1])
