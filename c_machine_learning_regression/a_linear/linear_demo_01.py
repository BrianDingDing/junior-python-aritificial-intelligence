"""
    基于梯度下降实现线性回归
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
y = np.array([5.0, 5.5, 6.0, 6.8, 7.1])

# 模型的初始参数
w1 = 1  # 权重, 初始值一般为0-1随机数, 不能为0
w0 = 1  # 偏置, 初始值一般0或者1
learning_rate = 0.01  # 学习率
epoch = 500  # 轮数

w1s, w0s, losses, epochs = [], [], [], []

for i in range(epoch):
    # 模型参数更新之前, 打印参数变化和损失值变化情况
    loss = ((w1 * x + w0 - y) ** 2).sum() / 2
    print('轮数:{:3},w1:{:.8f},w0:{:.8f},loss:{:.8f}'.format(i, w1, w0, loss))

    w1s.append(w1)
    w0s.append(w0)
    losses.append(loss)
    epochs.append(i)

    # w0和w1偏导数
    d0 = (w0 + w1 * x - y).sum()
    d1 = (x * (w0 + w1 * x - y)).sum()

    # 更新模型参数
    w0 = w0 - learning_rate * d0
    w1 = w1 - learning_rate * d1

pred_y = w1 * x + w0

# 回归线可视化
# plt.plot(x, pred_y, color='orangered')
# plt.scatter(x, y)
# plt.show()

# 模型参数和损失函数可视化
plt.subplot(3, 1, 1)
plt.plot(epochs, w1s, color='dodgerblue', label='w1')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(epochs, w0s, color='dodgerblue', label='w0')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(epochs, losses, color='orangered', label='loss')
plt.legend()

plt.tight_layout()
plt.show()
