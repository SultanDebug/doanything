import random

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.title("demo")
x = [random.uniform(1, 10) for x in range(10)]
# x.sort()
y = [random.uniform(1, 10) for x in range(10)]
# y.sort()
plt.plot(x, y)
plt.show()
