import numpy as np


def f(x):
    return 2 ** x


xx = np.linspace(-2, 4, 5, 7)

arg_min = np.argmin(f(xx))

print(arg_min)
print(xx[arg_min])
print(f(xx[arg_min]))
