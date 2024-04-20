import matplotlib.pyplot as plt
import random

plt.rcParams['font.family'] = ['SimHei']
x = range(20)

y = range(50)
yd1 = [random.randint(0, 50) for i in x]
yd2 = [random.randint(0, 50) for i in x]


plt.xticks(x[::2])
plt.yticks(y[::5])

plt.xlabel("X-label")
plt.ylabel("Y-label")

plt.title("Test Title")

plt.scatter(x,yd1,s=20,c='r',marker='+',label="cat1")
plt.scatter(x,yd2,s=40,c='b',marker='v',label="cat2")

# 添加图例 loc指定图例的位置
plt.legend(loc='best')

plt.grid(True,linestyle=':')
plt.show()
