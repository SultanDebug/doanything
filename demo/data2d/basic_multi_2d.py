"""
多坐标基础画图
"""

import random

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['SimHei']
x = range(30)
xt = [f'{i} th' for i in x]

y = range(40)
yt = [f'{i} ℃' for i in y]

yd1 = [random.uniform(10, 20) for i in x]
yd2 = [random.uniform(20, 30) for i in x]

fig, ax = plt.subplots(1, 2,sharex=True, figsize=[15, 8], dpi=100)

ax[0].set_xlabel("March", fontsize=15)
ax[0].set_ylabel("Temperature", fontsize=15)
ax[0].set_xticks(x[::5], xt[::5])
ax[0].set_yticks(y[::5], yt[::5])
ax[0].plot(x, yd1, 'rh-', label="low")

ax[1].set_xlabel("March1", fontsize=15)
ax[1].set_ylabel("Temperature1", fontsize=15)
ax[1].set_xticks(x[::5], xt[::5])
ax[1].set_yticks(y[::5], yt[::5])
ax[1].plot(x, yd2, 'g|-.', label="hign")

# 添加图例 loc指定图例的位置
ax[0].legend(loc='best')
ax[1].legend(loc='best')

# 添加网格线 linestyle线型 alpha透明度
ax[0].grid(True, linestyle=':', alpha=0.7)
ax[1].grid(True, linestyle=':', alpha=0.7)

plt.show()
