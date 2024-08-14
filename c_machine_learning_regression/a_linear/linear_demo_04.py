import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as sm

# 数据准备
data = pd.read_csv('../../resources/c_machine_learning_regression/Salary_Data2.csv')

# 整理输入和输出
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 构建模型
model = lm.LinearRegression()
ridge = lm.Ridge(alpha=100)

# 训练模型
model.fit(x, y)
ridge.fit(x, y)

# 将x带入模型中, 得到预测值
pred_y = model.predict(x)
pred_ridge_y = ridge.predict(x)

# 可视化回归线
# plt.scatter(x, y)
# plt.plot(x, pred_y, color='orangered')
# plt.plot(x, pred_ridge_y, color='black')
# plt.show()

# 暴力挑选正则化系数的最优值
test_x = x.iloc[:30:4]
test_y = y[:30:4]

params = np.arange(91, 109, 1)

score = []
for param in params:
    model = lm.Ridge(alpha=param)
    model.fit(x, y)
    pred_test_y = model.predict(test_x)
    score.append(sm.r2_score(test_y, pred_test_y))

score = pd.Series(score, index=params)
print('best model: {}, 得分:{}'.format(score.idxmax(), score.max()))