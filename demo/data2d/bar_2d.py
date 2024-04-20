import matplotlib.pyplot as plt
import random

plt.rcParams['font.family'] = ['SimHei']

width = 0.3

x = range(1, 11, 1)

x1 = x[0::2]
xt1 = [f'类别 {i}' for i in x1]
# yd1 = [random.randint(0, 100) for i in x1]
yd1 = [random.uniform(0, i) for i in x1]

x2 = [i + width for i in x1]
# yd2 = [random.randint(0,100) for i in x2]
yd2 = [random.uniform(0, i) for i in x2]

x3 = [i + width for i in x2]
# yd2 = [random.randint(0,100) for i in x2]
yd3 = [random.uniform(0, i) for i in x3]

y = range(10)

plt.yticks(y[::2])

plt.xlabel("X-轴")
plt.ylabel("Y-轴")

plt.title("柱状图")

plt.bar(x1, yd1, width, align='center', color='r', tick_label=xt1, label='数据 1')
plt.bar(x2, yd2, width, align='center', color='g', tick_label=xt1, label='数据 2')
plt.bar(x3, yd3, width, align='center', color='m', tick_label=xt1, label='数据 3')

# 添加图例 loc指定图例的位置
plt.legend(loc='best')

plt.grid(True, linestyle=':')
plt.show()
