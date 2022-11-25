import numpy as np
import pandas as pd
import json

xlxs = pd.read_excel("C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\pydata\\source.xlsx");
i = 0
while i < xlxs.values.shape[0]:
    j = 0
    while j < xlxs.values.shape[1]:
        val = xlxs.values[i][j]
        print("panda xlsx形式：", val)
        j += 1
    i += 1

txt = pd.read_table("C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\pydata\\source.txt")
print("panda table形式：", txt)

js = pd.read_json("C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\pydata\\json.txt")
print("panda json形式：", type(js.values))

with open("C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\pydata\\source.txt", 'r', encoding='UTF-8') as f:
    line = f.readline()
    while not line.isspace():
        print("open形式：", line)
        line = f.readline()
