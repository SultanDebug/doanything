import matplotlib.pyplot as plt
import random
import numpy as np

plt.rcParams['font.family'] = ['SimHei']

pie_num = 5

xx = [(np.random.randint(1, 10), f'类别{i}') for i in range(pie_num)]

x = [i[0] for i in xx]

lab = [f'{i[1]}-{i[0]}' for i in xx]

expl = [0 for i in range(pie_num)]
ei = [1,3]
for i in ei:
    expl[i] = 0.1

plt.pie(x,
        labels=lab,
        autopct='%.1f%%',
        explode=expl
        )
plt.show()
