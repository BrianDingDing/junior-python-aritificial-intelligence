"""
    创建DataFrame
"""
import pandas as pd

df = pd.DataFrame([1, 2, 3, 4, 5])
print(df)  # shape: (5,1)

# 1. DataFrame基本创建
# 通常只设列名, 不设行级索引.
df1 = pd.DataFrame([['Tom', 18],
                    ['Jerry', 20],
                    ['Jack', 15],
                    ['Rose', 20]],
                   index=['s01', 's02', 's03', 's04'],
                   columns=['Name', 'Age'])
print(df1)

# 2. 通过字典创建, 列表中的元素必须相同.
data = {'Name': ['Tom', 'Jerry', 'Jack', 'Rose'],
        'Age': [18, 18, 20, 20]}
df2 = pd.DataFrame(data)
print(df2)

# 3. 使用series创建, 针对每一列长度不相等.
data1 = {'Name': pd.Series(['Tom', 'Jerry', 'Jack', 'Rose']),
         'Age': pd.Series([18, 20, 20])}
df3 = pd.DataFrame(data1)  # 在最后的一行Age位置补充NaN
print(df3)

# 4. 使用series创建, 指定index, 指定那个数值缺了.
data2 = {'Name': pd.Series(['Tom', 'Jerry', 'Jack', 'Rose'],
                           index=['a', 'b', 'c', 'd']),
         'Age': pd.Series([18, 20, 20],
                          index=['a', 'c', 'd'])}
df4 = pd.DataFrame(data2)
print(df4)
