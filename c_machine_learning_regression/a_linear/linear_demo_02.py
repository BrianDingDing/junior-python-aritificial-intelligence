"""
    利用sklearn提供的API实现线性回归
"""
import sklearn.linear_model as lm  # 线性模型
import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
data = pd.read_csv("../../resources/c_machine_learning_regression/Salary_Data.csv")

# 整理输入(二维)和输出(一维)
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 构建模型
model = lm.LinearRegression()

# 训练
model.fit(x, y)
print('权重:{},偏置:{}'.format(model.coef_, model.intercept_))

# 执行预测
pred_y = model.predict(x)

plt.plot(x, pred_y, color='orangered')
plt.scatter(x, y)
plt.show()
