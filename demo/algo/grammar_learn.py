import random

for v in "asd":
    print(v, end=" ")

print()
for v in [1, 2, 3, 4, 5]:
    print(v, end=" ")
print()

v = 1
while v <= 5:
    print(v, end=" ")
    v += 1

print()
arr = [1, 2, 3, 4, 5]

for v in arr[0:3:2]:
    print(v, end=" ")

for obj in enumerate(arr):
    print(obj[0], obj[1], sep="/")

print()
print("slen: ", len("asdadasd"))
print("len: ", len(arr))

arr.sort(reverse=True)
print(arr)

print(sorted(arr))

expr = [random.uniform(1, 10) for x in range(10)]
print(expr)

expr1 = [x for x in expr if x > 5]
print(expr1)

dic = {}
l1 = [1, 2, 3, "4"]
l2 = ["a", "b", "c", 1]
for i in range(len(l1)):
    dic.setdefault(l1[i], l2[i])

print(dic)

items = dic.items()
print(items)

years = [45, 89, 1998, 00, 75, 33, 1968, 37, 1958, 90]
for i in range(len(years)):
    y = years[i]
    print(isinstance(years[i], str))
    if y == 0:
        years[i] += 2000
    elif y < 100:
        years[i] += 1900

years.sort(reverse=False)
print(years)

"""
素数，筛选法
"""
pr = [x for x in range(2, 100)]
p = [1]
pre = 2
cnt = 0
while True:
    p.append(pr[0])
    for x in pr:
        cnt += 1
        if x % pre == 0:
            pr.remove(x)
    if len(pr) == 0:
        break
    pre = pr[0]
print(p)
print(p[:5])
pp = [x * 20 for x in p]
print(pp)
print(cnt)


class Man:
    age = 1
    sex = 1
    name = "hzq"
    __addr = "深圳"

    def __init__(self, age, sex):
        self.age = age
        self.__sex = sex

    def getage(self):
        return self.age

    def updateage(self, x=1):
        Man.age += (x * 2)
        self.age += x
        Man.name += "-sultan"


Man.age = 2
man = Man(18, 0)
man1 = Man(18, 0)
man.updateage(x=3)
print("实例：" + str(man.getage()))
print("类：" + str(Man.age))
print("类公共：" + str(man1.name))
print("类私有：" + man._Man__addr)
print("实例私有：" + str(man._Man__sex))


def func1(x=None):
    return x ** 2


print(func1(x=2))

import urllib3
pool = urllib3.PoolManager()
res = pool.request(method='get',url="https://www.baidu.com/")
print(res.data)

import matplotlib.pylab as lab

lab.show()