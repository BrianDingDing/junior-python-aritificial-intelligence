import pandas as pd
import warnings  # 警告

warnings.filterwarnings('ignore')

data = {'one': pd.Series([1, 2, 3],
                         index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4],
                         index=['a', 'b', 'c', 'd']),
        'three': pd.Series([1, 3, 4],
                           index=['a', 'c', 'd'])}

df = pd.DataFrame(data)
print(df)

# 访问一行数据: loc(标签索引), iloc(位置索引), loc和iloc可以看成二维数组.
# 列级操作能索引, 不能切片. 行级能切片, 不能索引.
print(df.loc['a'])  # 返回一个Series
# 切片
print(df.loc['a':'c'])
# 掩码
print(df.loc[['a', 'c']])

print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[[0, 2, 3]])

# 取出非最后一列数据
print(df.iloc[:, :-1])
# 取出最后一列数据
print(df.iloc[:, -1])

print('==' * 30)

# 行的添加 df1._append(df2)
# 注意: df1和df2列名必须相同, 否则添加歪.
df1 = pd.DataFrame([['Bob', 18],
                    ['Alex', 20]],
                   columns=['Name', 'Age'])

df2 = pd.DataFrame([['ZS', 19],
                    ['LS', 27]],
                   columns=['Name', 'Age'])

df3 = df1._append(df2)
# 由于索引冲突, 因此手动指定index.
df3.index = [1, 2, 3, 4]
print(df3)

# 删除行数据
# df3.drop([2, 3], axis=0, inplace=True)
# print(df3)

# 修改: 很少使用
# 通过列找行, 找到Alex, 修改为Age为21.
df3['Age'][2] = 21
print(df3)

# 通过行找列, 修改不成功, 底层没有赋值.
df3.iloc[1]['Age'] = 22
print(df3)
