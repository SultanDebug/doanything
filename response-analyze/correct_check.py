import csv
import json
import time

import requests
import datetime

filename = "D:\correct_word_freq.txt"
rows = []
with open(filename, "r", encoding='utf-8') as file_csv:  # 是不是忘记了如何打开文件？打开文件，并将结果文件对象存储在file_csv中
    for idx in range(50000):
        cont = file_csv.readline()
        if len(cont) == 0:
            break
        rows.append(cont)


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
        url = "http://wzalgo-gateway-v2-pre-lan.qizhidao.com/bird-search-engine/bird/search/engine"  # 拼接地址

        # 参数
        # 政策搜索索引名称
        #     项目简介 projectinfo
        #     公示文件 projectpublicity
        #     获批名单 publicitylibrary
        #     申报通知,产业通知，政策资讯 relatematerial

        arr = row.split(",")

        collect = arr[0].strip()
        query = arr[1].strip()

        cotype = ''
        if collect == 'project_info':
            cotype = 'projectinfo'
        elif collect == 'publicity_library':
            cotype = 'publicitylibrary'
        elif collect == 'relate_material':
            cotype = 'relatematerial'
        else:
            cotype = 'projectpublicity'
        body = {
            "collectionName": cotype,
            "request": "{\"offset\":1,\"size\":10,\"query\":\"" + query + "\",\"conditions\":\"{\\\"material_type_id\\\":1}\"}"
        }
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

        res = json.loads(r.content.decode('utf-8'))
        docs = res.get('docs')
        if len(docs) > 0:
            suc = suc+1
        else:
            fail = fail +1

        print("查询",totle,"==>", query,"==>",len(docs) > 0)
    except:
        print("异常",totle,"==>", row, "==>error")
        err = err + 1

print("接口总数：", totle,"成功：", suc,"失败：", fail, "最小花费：", (min_time * 1000), "最大花费：", (max_time * 1000))
