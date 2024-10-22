import random


class Car:
    def __init__(self, _a, __b, c):
        print("car para init")
        self._a = _a
        self.__b = __b
        self.c = c

    def name(self):
        print("car")

    @property
    def multi(self):
        return self.__b * self.c


class Byd(Car):
    def __init__(self, a, b, c, d: str = "hzq"):
        # self._a = _a
        # self._Car__b = __b
        super().__init__(a, b, c)
        self.__d = d
        print("Byd init 4")

    def name(self):
        print("BYD")

    def dd(self):
        print("__d=", self.__d)

    # *表示后面都是关键字参数，不能出现位置参数
    def tt(self, a, b, c, *, d=None, **kwargs):
        print(f'{a},{b},{c},{d},{kwargs}')


byd1 = Byd("byd", 3, 4)
print(byd1.multi)
byd1.name()
byd1.dd()

byd2 = Byd("asd", 5, 2, "asd")
print(byd2.multi)
byd2.name()
byd2.dd()
byd2.tt(1, 2, 3, d=4, f=5, g=6)

my_min = lambda a, b: min(a, b)

print(my_min(6, 2))

p1 = 1
p2 = "测试"
ss = f'打印p1：{p1},p2:{p2}'
print(ss)

x = range(10)

x1 = x[0::2]
xt1 = [f'CAT {i}' for i in x1]
x2 = x[1::2]
xt2 = [f'CAT {i}' for i in x2]

print(x, x1, x2, xt1, xt2)

index = range(1, 11)
n = [random.randint(1, 10) for i in index]
arr = [0 for i in range(index[len(index) - 1] - index[0] + 1)]
for i in n:
    arr[i - index[0]] += 1

for i in n:
    print('org=', i, end="/")
print()
for i in arr:
    print('sat=', i, end="/")
print()
x = 10//3
y = 10%3
z = 10/3
print(x)
print(y)
print(z)


for i in range(20):
    expr = [str(random.randint(1, 9)) for m in range(10)]
    s = ''.join(expr)

    print(s,end="/\n")

