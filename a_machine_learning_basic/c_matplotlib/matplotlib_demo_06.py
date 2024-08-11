"""
    直方图
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(175, 5, 1000)

plt.hist(x, bins=50)

plt.show()
