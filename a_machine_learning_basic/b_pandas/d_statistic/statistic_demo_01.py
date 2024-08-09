"""
    基本的数学指标
"""

import pandas as pd
import numpy as np

data = pd.read_json('../../../resources/a_machine_learning_basic/ratings.json')

fracture = data.loc['Fracture']

# 1. 通过numpy求平均值
print(np.mean(fracture))
# 求每一列列的平均值
print(np.mean(data, axis=0))

# 2. 通过pandas求平均值
print(fracture.mean())
print(data.mean(axis=1))

# 3. 加权平均值
weights = [1, 10, 1, 1, 1, 10, 1]
print(np.average(fracture, weights=weights))

# 最值和最值索引
# 1. numpy方法
print('最高分为:{}, 谁打的:{}'.format(np.max(fracture), np.argmax(fracture)))
# 2. pandas方法
print('最高分为:{}, 谁打的:{}'.format(fracture.max(), fracture.idxmax()))

# 中位数
print('中位数:', np.median(fracture))

# 标准差
print('标准差:', fracture.std())
# ddof=1 -> 样本方差和总体方差
print('标准差:', np.std(fracture, ddof=1))
