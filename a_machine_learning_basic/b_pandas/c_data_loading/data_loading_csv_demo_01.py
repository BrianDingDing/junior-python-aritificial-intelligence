"""
    csv读取与写入
"""
import pandas as pd

"""
| 方法参数             | 参数解释                                          |
| ------------------ | -------------------------------------------------|
| filepath_or_buffer | 文件路径                                           |
| sep                | 列之间的分隔符. read_csv()默认为为','                 |
| header             | 默认将首行设为列名. header=None时应手动给出列名.        |
| names              | header=None时设置此字段使用列表初始化列名.             |
| index_col          | 将某一列作为行级索引. 若使用列表, 则设置复合索引.         |
| usecols            | 选择读取文件中的某些列。设置为为相应列的索引列表。         |
| skiprows           | 跳过行。可选择跳过前n行或给出跳过的行索引列表。           |
| encoding           | 编码。                                            |
"""
data = pd.read_csv('../../../resources/a_machine_learning_basic/aapl.csv',
                   sep=',',
                   header=None,
                   names=['name', 'date', '_', 'open', 'high', 'low', 'close', '__'],
                   index_col='date',
                   usecols=['date', 'open', 'high', 'low', 'close'])

print(data.head(5))

"""
| 方法参数             | 参数解释                                          |
| ------------------ | -------------------------------------------------|
| filepath_or_buffer | 文件路径                                          |
| sep                | 列之间的分隔符. 默认为','                            |
| na_rep             | 写入文件时dataFrame中缺失值的内容. 默认空字符串.        |
| columns            | 定义需要写入文件的列.                                |
| header             | 是否需要写入表头. 默认为True.                        |
| index              | 会否需要写入行索引. 默认为True.                       |
| encoding           | 编码.                                             |
"""

data.to_csv("../../../resources/a_machine_learning_basic/new_data.csv")

"""
    读取excel
"""
# pip install xlrd==1.2.0
data1 = pd.read_excel('../../../resources/a_machine_learning_basic/CustomerSurvival.xlsx')
print(data1.head(5))
