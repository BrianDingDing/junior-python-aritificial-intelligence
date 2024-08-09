"""
   json文件读取与写入
"""
import pandas as pd

# read_json
# 其中键是列级索引, 对应下面写to_json的columns格式.
data = pd.read_json('../../../resources/a_machine_learning_basic/ratings.json')
# print(data)

# to_json

print("==" * 30)

data = {'Name': ['Tom', 'Jerry', 'Jack', 'Rose'],
        'Age': [18, 19, 20, 20]}

df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'])
print(df)

# [{"Name":"Tom","Age":18}, ...]
print(df.to_json(orient='records'))
# {"s1":{"Name":"Tom","Age":18}, ...]
print(df.to_json(orient='index'))
# {"Name":{"s1":"Tom","s2":"Jerry","s3":"Jack","s4":"Rose"}, ...}
print(df.to_json(orient='columns'))
# [["Tom",18], ...]
print(df.to_json(orient='values'))
