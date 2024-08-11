"""
    标签编码
"""
import numpy as np
import pandas as pd
import sklearn.preprocessing as sp

# data = np.array(['bmw', 'benz', 'bmw', 'audi', 'bmw', 'BYD', 'Yadi'])
#
# encoder = sp.LabelEncoder()
# # 按照字符串的ASCII进行比较, a=97; A=65.
# res = encoder.fit_transform(data)
# print(res)

data = np.array([['男', '及格'],
                 ['女', '及格'],
                 ['男', '不及格']])

ret = []
for col in data.T:
    encoder = sp.LabelEncoder()
    res = encoder.fit_transform(col)
    ret.append(res)

ret = np.array(ret)
print(ret.T)

# 将car.txt中的数据, 使用标签编码将字符串转成数值.

data = pd.read_csv('../../resources/b_machine_learning_theory/car.txt')
# print(data.head(5))
# print(data.dtypes)

encoders = {}
car_data = pd.DataFrame()

# col: 是列名
for col in data:
    encoder = sp.LabelEncoder()
    # 保存每列的编码器.
    encoders[col] = encoder
    res = encoder.fit_transform(data[col])
    car_data[col] = res

# print(car_data)

# 解码
inv_data = pd.DataFrame()
for col in car_data:
    encoder = encoders[col]
    res = encoder.inverse_transform(car_data[col])
    inv_data[col] = res

print(inv_data)
