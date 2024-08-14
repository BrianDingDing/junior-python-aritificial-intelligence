"""
    波士顿房屋价格预测
"""

import pandas as pd
import numpy as np
import sklearn.datasets as sd  # 数据集和
import sklearn.model_selection as ms  # 模型选择
import sklearn.metrics as sm  # 评估模块
import sklearn.linear_model as lm  # 线性回归
import sklearn.pipeline as pl  # 数据管线
import sklearn.preprocessing as sp  # 数据预处理

# boston = sd.load_boston()
# print(boston.keys())
# print(boston.DESCR)  # 506样本, 13个x -> y
# print(boston.data.shape)  # x(506, 13)
# print(boston.target.shape)  # y(506,)

# x = boston.data
# y = boston.target

# sklearn更高版本获取boston数据的写法
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

x = data
y = target

# 划分训练集和测试集
# 数据一定不能有顺序, 一定要随机打乱.
train_x, \
    test_x, \
    train_y, \
    test_y = ms.train_test_split(x, y, test_size=0.2, random_state=7)


# 构建模型
# 线性回归, 岭回归，多项式回归
def get_model(name, model):
    print('--------------', name, '--------------')
    model.fit(train_x, train_y)
    pred_train_y = model.predict(train_x)
    pred_test_y = model.predict(test_x)
    train_r2 = sm.r2_score(train_y, pred_train_y)
    test_r2 = sm.r2_score(test_y, pred_test_y)
    print('训练集得分:', train_r2)
    print('测试集得分:', test_r2)


md = {'线性回归': lm.LinearRegression(),
      '岭回归': lm.Ridge(),
      '多项式回归': pl.make_pipeline(sp.PolynomialFeatures(2), lm.LinearRegression())}

for name, model in md.items():
    get_model(name, model)
