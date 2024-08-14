"""
    多项式回归
"""

import pandas as pd
import sklearn.pipeline as pl  # 管线模块
import sklearn.preprocessing as sp  # 数据预处理模块
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

data = pd.read_csv('../../resources/c_machine_learning_regression/Salary_Data.csv')
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

model = pl.make_pipeline(sp.PolynomialFeatures(3), lm.LinearRegression())
model.fit(x, y)
pred_y = model.predict(x)

plt.scatter(x, y)
plt.plot(x, pred_y, color='orangered')
plt.show()
