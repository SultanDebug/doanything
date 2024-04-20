import matplotlib.pyplot as plt
import random

plt.rcParams['font.family'] = ['SimHei']

rge = 2
nums = [random.randint(1, 10) for i in range(100)]
maxn = max(nums)
minn = min(nums)
cats = range(minn, maxn + rge, rge)

# cat_names = [f"cat {i}" for i in cats]
plt.xticks(cats)
# range未生效
plt.hist(nums, cats, range=(3, 7),stacked=True,histtype='barstacked',color='y')
plt.show()
