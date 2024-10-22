import random

import matplotlib.pyplot as plt
import numpy
import numpy as np
from typing import List


def relu(*args) -> List[float]:

    z = [x for x in args]

    rs = []

    zz = np.array(z)
    tz = zz.T
    for item in tz:
        m = max(item)
        if m > 0:
            rs.append(m)
        else:
            rs.append(0)

    return rs


t1 = [-1, 2, 5]
t2 = [-2, 3, 6]
t3 = [-3, 4, 7]

r = relu(t1, t2,t3)
print(r)

# x = range(-10, 11)

xx = np.linspace(-100, 100, 100)
x = [random.random() * 10 * (np.sign(i)) for i in xx]
x.sort()

y1 = [i - 1 for i in x]
y2 = [-i for i in x]

# yy = [y1, y2]
# y3 = np.amax(yy, axis=0)
y3 = relu(y1, y2)

plt.scatter(x, y1, s=20, c='r', marker='+', label="cat1")
plt.scatter(x, y2, s=20, c='b', marker='v', label="cat1")
plt.plot(x, y3, color='black')
plt.show()
