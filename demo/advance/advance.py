import random

x = 0
y = 0

for i in range(100):
    a = 0
    b = 0
    expr = [random.uniform(1, 100) for m in range(100)]
    for j in expr:
        if j > 50:
            a += 1
        else:
            b += 1
    aa = a / (a + b)
    bb = b / (a + b)
    if aa > bb:
        x += 1
    else:
        y += 1
print("1：" + str(x / (x + y)) + ",0：" + str(y / (x + y)))
print(str(x) + "/" + str(y))
