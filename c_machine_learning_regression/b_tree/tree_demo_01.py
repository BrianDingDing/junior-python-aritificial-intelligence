"""
    波士顿房屋价格预测
"""

import sklearn.datasets as sd  # 数据集和
import sklearn.model_selection as ms  # 模型选择
import sklearn.metrics as sm  # 评估模块
import sklearn.tree as st
import matplotlib.pyplot as plt
import pandas as pd

boston = sd.fetch_openml(name='boston', version=1, as_frame=True)
x = boston.data
y = boston.target

# 划分训练集和测试集
train_x, \
test_x, \
train_y, \
test_y = ms.train_test_split(x, y, test_size=0.2, random_state=7)

# 单颗决策树, 属于弱模型
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
pred_train_y = model.predict(train_x)
pred_test_y = model.predict(test_x)
print('训练集得分:', sm.r2_score(train_y, pred_train_y))
print('测试集得分:', sm.r2_score(test_y, pred_test_y))

# 单颗决策树可视化
# plt.figure(figsize=(15, 9))
# st.plot_tree(model, feature_names=boston.feature_names, filled=True)
# plt.savefig('tree.png')
# plt.show()

# 特征属性强度
fi = model.feature_importances_
s = pd.Series(fi, index=boston.feature_names)
print(s)

s.sort_values(ascending=True).plot.barh()
plt.show()
