import random

import matplotlib.pyplot as plt
import numpy as np

xxx = np.linspace(-1,1,100)

x= range(-10,11,1)

w1 = [random.randint(1,10) for i in x]

w2 = [random.randint(1,10) for i in x]

b1 = random.randint(1,10)
b2 = random.randint(1,10)

y1 = [w*xx+b1 for w,xx in zip(w1,x)]

y2 = [w*xx+b2 for w,xx in zip(w2,x)]

y3 = np.amax()

y2 = [5*i-1 for i in y1]

plt.plot(x,y,color='red')
plt.plot(x,y1,color='blue')
plt.plot(x,y2,color='black')
plt.show()