"""
    基本的绘图
"""
import numpy as np
import matplotlib.pyplot as plt

# # 绘制简单直线
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([3, 6, 9, 12, 15])
#
# plt.plot(x, y)
# # 显示图片，阻塞方法
# plt.show()

# 绘制-pi, pi 正弦, 余弦的函数图像
xs = np.linspace(-np.pi, np.pi, 200)
sinx = np.sin(xs)
cosx = np.cos(xs) / 2

plt.plot(xs, sinx, linestyle='--', linewidth=3, color='dodgerblue', label=r'$y=sin(x)$')
plt.plot(xs, cosx, linestyle='-.', linewidth=6, color='orangered', label=r'$y=\frac{1}{2}cos(x)$')

# 设置坐标轴的范围: 第一象限
# plt.xlim(0, np.pi + 0.1)
# plt.ylim(0, 1 + 0.1)

# 设置坐标刻度
# r'$latex表达式$', 分数: \frac{分子}{分母}, pi: \pi
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\frac{\pi}{2}$', 0, r'$\frac{\pi}{2}$', r'$\pi$'],
           fontsize=14)

# 设置坐标轴
ax = plt.gca()
# 设置上轴和右轴透明
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 需要重新字体大小
plt.xticks(fontsize=14)
plt.yticks([-1, -0.5, 0.5, 1], fontsize=14)

# 图例
plt.legend()

# 特殊点
plt.scatter([np.pi/2, -np.pi/2], [1, -1],
            marker='*', s=200, edgecolors='red', facecolor='green', zorder=2)

plt.show()
