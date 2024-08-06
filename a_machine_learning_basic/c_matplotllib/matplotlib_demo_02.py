"""
    高级绘图
"""
import numpy as np
import matplotlib.pyplot as plt

# # 窗口属性
# # 设定窗口
# plt.figure('AAA', facecolor='lightgrey')
#
# xs = np.linspace(-np.pi, np.pi, 200)
# sinx = np.sin(xs)
# plt.plot(xs, sinx)
#
# plt.title('Sin(x)', fontsize='28')
# plt.xlabel('X', fontsize='18')
# plt.ylabel('Y', fontsize='18')
# plt.grid(linestyle=':')
# plt.tight_layout()
#
# plt.show()

# # 子图(矩阵式布局: 每副子图大小相同)
#
# plt.figure('Subplot', facecolor='lightgrey')
# # # 三行三列的第五副子图
# # plt.subplot(3, 3, 5)
# # plt.text(0.5, 0.5, '5', fontsize=28, ha='center', va='center')
#
# for i in range(1, 10):
#     plt.subplot(3, 3, i)
#     plt.text(0.5, 0.5, i, fontsize=28, ha='center', va='center')
#     plt.xticks([])
#     plt.yticks([])
#
# plt.tight_layout()
# plt.show()

# 子图(网格式布局)

plt.figure('GS', facecolor='lightgrey')

# 拆分出3行3列的网格对象
gs = plt.GridSpec(3, 3)
plt.subplot(gs[0, :2])
plt.text(0.5, 0.5, 'python_base', fontsize=28, ha='center', va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[:2, -1])
plt.text(0.5, 0.5, 'socket', fontsize=28, ha='center', va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[-1, -2:])
plt.text(0.5, 0.5, 'python_web', fontsize=28, ha='center', va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[-2:, 0])
plt.text(0.5, 0.5, 'AI', fontsize=28, ha='center', va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[1, 1])
plt.text(0.5, 0.5, '2302', fontsize=28, ha='center', va='center')
plt.xticks([])
plt.yticks([])

plt.show()
