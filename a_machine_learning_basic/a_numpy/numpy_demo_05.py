"""
    自定义复合类型
"""
import numpy as np
import warnings  # 警告

warnings.filterwarnings('ignore')

data = [
    ('zs', [90, 80, 85], 18),
    ('ls', [92, 81, 83], 19),
    ('ww', [95, 85, 95], 20)
]

# 第一种设置dtype类型
ary = np.array(data, dtype='U2,3int32,int32')
print(ary)
print(ary.shape)

# 求第三列平均值年龄, f=field
print(ary['f2'].mean())
# 求每一个人的平均分
print(ary['f1'].mean(axis=1))
# 求每科平均分
print(ary['f1'].mean(axis=0))

# 第二种设置dtype的方式
ary2 = np.array(data, dtype={'names': ['name', 'score', 'age'],
                             'formats': ['U2', '3int32', 'int32']})
print(ary2['age'])
