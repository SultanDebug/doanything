import csv
import json
import time

import requests
import datetime

filename = "D:\projectpublicity.txt"
rows = []
with open(filename, "r", encoding='utf-8') as file_csv:  # 是不是忘记了如何打开文件？打开文件，并将结果文件对象存储在file_csv中
    for idx in range(1):
        rows.append(file_csv.readline())
querys = []
suc = 0
fail = 0
totle = 0
min_time = 0
max_time = 0

for row in rows:
    totle = totle + 1
    try:
        # host="http://192.168.200.91:8080"  #部署的服务器地址
        # login_url="/chun5/user/login"  #请求地址
        url = "http://wzalgo-gateway-v2-test-lan.qizhidao.com/bird-search-engine/bird/search/engine"  # 拼接地址

        # 参数
        body = json.loads(row)
        # 发送请求
        begin = time.time()
        r = requests.post(url=url, json=body)
        end = time.time()

        reduce = end - begin

        if min_time == 0:
            min_time = reduce
        if max_time == 0:
            max_time = reduce

        if min_time > reduce:
            min_time = reduce
        if max_time < reduce:
            max_time = reduce

        if reduce * 1000 > 200 :
            querys.append(row+"==>"+reduce)

        res = json.loads(r.content.decode('utf-8'))
        success = res.get('success')
        if success :
            suc = suc+1
        else:
            fail = fail +1
        req = json.loads(body.get('request'))
        query = req.get('query')
        print("查询",totle,"==>", query)
    except:
        print("异常",totle,"==>", row, "error")
        err = err + 1



print("接口总数：", totle,"成功：", suc,"失败：", fail, ",大于一秒的query：", querys, "最小花费：", (min_time * 1000), "最大花费：", (max_time * 1000))
