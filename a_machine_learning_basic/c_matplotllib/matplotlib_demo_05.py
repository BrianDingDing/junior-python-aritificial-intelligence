"""
    柱状图
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 13)
apples = np.random.normal(60, 20, 12).astype("int32")
oranges = np.random.normal(60, 20, 12).astype("int32")

plt.bar(x - 0.2, apples, width=0.4)
plt.bar(x + 0.2, oranges, width=0.4)

# for i in range(0, 12):
#     plt.text(x[i], apples[i], apples[i],
#              ha='center', va='bottom')

plt.show()
