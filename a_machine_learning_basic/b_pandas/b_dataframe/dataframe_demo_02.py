"""
    panda基本属性
"""
import pandas as pd

data = {'Name': pd.Series(['Tom', 'Jerry', 'Jack', 'Rose'],
                          index=['a', 'b', 'c', 'd']),
        'Age': pd.Series([18, 20, 20],
                         index=['a', 'c', 'd'])}
df = pd.DataFrame(data)

# 返回行/列标签(index)列表
print(df.axes)  # [Index(['a', 'b', 'c', 'd'], dtype='object'), Index(['Name', 'Age'], dtype='object')]
# 返回行标签
print(df.index)  # Index(['a', 'b', 'c', 'd'], dtype='object')
# 返回列标签
print(df.columns)  # Index(['Name', 'Age'], dtype='object')
# 返回数据, 二维数组
print(df.values)
# 返回纬度，一定是二维
print(df.ndim)  # 2
print(df.shape)  # (4,2)
# 返回数据中的元素数
print(df.size)  # 8
# 返回每列数据类型, 返回的对象是Series类型.
# object指的是字符串.
# 如果某列数据存在nan, 类型则变为浮点型.
print(df.dtypes)
# 判断系列为空
print(df.empty)
# 返回前n行
print(df.head(2))
# 返回最后n行
print(df.tail(2))
