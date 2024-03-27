import random

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

"""
基础画图
"""
plt.rcParams['font.family'] = ['SimHei']
plt.figure(figsize=(10, 5), dpi=100)

x = range(30)
xt = [f"{i} Day" for i in x]
yd1 = [random.uniform(20, 30) for i in x]
yd2 = [random.uniform(10, 20) for i in x]

y = range(40)
yt = [f"{i} ℃" for i in y]

plt.xlabel("March", fontsize=15)
plt.ylabel("Temperature", fontsize=15)
plt.xticks(x[::5], xt[::5])
plt.yticks(y[::5], yt[::5])

plt.plot(x, yd1,'rh-', label="hign")
plt.plot(x, yd2,'g|-.', label="low")

# 添加图例 loc指定图例的位置
plt.legend(loc='best')

# 添加网格线 linestyle线型 alpha透明度
plt.grid(True, linestyle=':', alpha=0.7)

plt.show()
