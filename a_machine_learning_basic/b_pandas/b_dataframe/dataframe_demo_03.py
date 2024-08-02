"""
    DataFrame增删改查: 列级
"""
import pandas as pd

data = {'one': pd.Series([1, 2, 3],
                         index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4],
                         index=['a', 'b', 'c', 'd']),
        'three': pd.Series([1, 3, 4],
                           index=['a', 'c', 'd'])}

df = pd.DataFrame(data)
print(df)

# 1. 列访问
# 访问一列数据, 返回一个Series, 列级索引没有位置索引.
print(df['one'])
# print(df[0])

# 列级索引不支持切片
# print(df['one':'two'])

# 访问多列数据, 使用掩码.
print(df[['one', 'two']])
print(df[df.columns[:-1]])

# 2. 列添加
# 如果添加数据为列表, 要跟原始数据的列的长度相同.
df['four'] = [1, 2, 3, 4]
# 如果添加数据为Series, 要指定index, 否则会默认分配行级索引为0,1,2. 返回数据全部为NaN.
df['five'] = pd.Series([1, 2, 3],
                       index=['a', 'b', 'c'])
print(df)

# 3. 列删除
# del和pop同时只能删除一列数据
del df['four']
df.pop('five')
print(df)

# 删除多列 drop
# axis指的是索引是行还是列, 轴向axis=1表示列级索引并且必须写, 默认按axis=0删除行的.
# 默认inplace=False, 不修改原数据
df.drop(['one', 'three'], axis=1, inplace=True)
print(df)
