import sklearn.linear_model as lm  # 线性模型
import pandas as pd
import sklearn.metrics as sm  # 评估模块
import pickle

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

# 找到一组数据, 进行模型评估
# 在全部数据中, 抽取一部分数据，进行测试，假设他们没参加过训练
test_x = x.iloc[::4]
test_y = y[::4]  # 真实值

# 将test_x带入到模型中, 得到预测值.
pred_test_y = model.predict(test_x)  # 预测值

print("MAE:", sm.mean_absolute_error(test_y, pred_test_y))
print("MSE:", sm.mean_squared_error(test_y, pred_test_y))
print("Medain:", sm.median_absolute_error(test_y, pred_test_y))
print("R2:", sm.r2_score(test_y, pred_test_y))

# 保存模型
with open('./model.pickle', 'wb') as w:
    pickle.dump(model, w)
print("模型保存成功")

# 加载模型
with open('./model.pickle', 'rb') as f:
    new_model = pickle.load(f)

res = new_model.predict([[1.1], [2.2]])
print(res)
