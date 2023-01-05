import csv
import json
import time

import requests
import datetime

filename = "D:\data.csv"
rows = []
with open(filename, "r", encoding='utf-8') as file_csv:  # 是不是忘记了如何打开文件？打开文件，并将结果文件对象存储在file_csv中
    reader = csv.reader(file_csv)  # 直接调读取 用csv.read()读取文件内容

    json_data = []
    # row = []
    for item in reader:  # 用for循环打印每一行
        rows.append(item[0].strip())

totle = 0
suc = 0
fail = 0
err = 0
totle_time = 0
min_time = 0
max_time = 0
for row in rows:
    totle = totle + 1
    try:
        arr = row.split("||")

        query = arr[0].strip()
        proid = arr[1].strip()

        # host=""  #部署的服务器地址
        # login_url=""  #请求地址
        url = ""  # 拼接地址

        # 参数
        body = {
            "collectionName": "projectinfo",
            "request": "{\"offset\":1,\"size\":3,\"query\":\"" + query + "\",\"conditions\":\"{}\"}"
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
        totle_time = totle_time + reduce

        res = json.loads(r.content.decode('utf-8'))
        docs = res.get('docs')
        flag = False
        k = 0
        for doc in docs:
            if k > 3:
                break
            k = k + 1
            # 输出返回
            proid_doc = doc['project_id']
            if proid == proid_doc:
                flag = True
                break

        if flag:
            suc = suc + 1
        else:
            fail = fail + 1
        print("新接口==>", arr[0], "/", arr[1], "/", flag)
    except:
        print("新接口==>", row, "error")
        err = err + 1



old_policy_url = ""

old_totle = 0
old_suc = 0
old_fail = 0
old_err = 0
old_totle_time = 0
old_min_time = 0
old_max_time = 0
for row in rows:
    old_totle = old_totle + 1
    try:
        arr = row.split("||")

        query = arr[0].strip()
        proid = arr[1].strip()

        # 参数
        old_policy_request_template = {
            "conditions": {
                "policyType": "merge_subsidy_document"
            },
            "current": 1,
            "fromSite": "sub",
            "pageSize": 3,
            "platform": 0,
            "searchKey": query,
            "type": 7
        }
        # 发送请求
        begin = time.time()
        r = requests.post(url=old_policy_url, json=old_policy_request_template)
        end = time.time()

        reduce = end - begin

        if old_min_time == 0:
            old_min_time = reduce
        if old_max_time == 0:
            old_max_time = reduce

        if old_min_time > reduce:
            old_min_time = reduce
        if old_max_time < reduce:
            old_max_time = reduce
        old_totle_time = old_totle_time + reduce

        res = json.loads(r.content.decode('utf-8'))
        data = res["data"]
        docs = data["records"]
        flag = False
        k = 0
        for doc in docs:
            if k > 3:
                break
            k = k + 1
            # 输出返回
            proid_doc = doc['project_id']
            if proid == proid_doc:
                flag = True
                break

        if flag:
            old_suc = old_suc + 1
        else:
            old_fail = old_fail + 1
        print("旧接口==>", arr[0], "/", arr[1], "/", flag)
    except:
        print("旧接口==>", row, "error")
        old_err = old_err + 1

print("新接口总数：", totle, ",正确：", suc, ",失败：", fail, "异常：", err, "总花费：", (totle_time * 1000), "平均花费：",
      ((totle_time / totle) * 1000), "最小花费：", (min_time * 1000), "最大花费：", (max_time * 1000), )
print("老接口总数：", old_totle, ",正确：", old_suc, ",失败：", old_fail, "异常：", old_err, "总花费：", (old_totle_time * 1000), "平均花费：",
      ((old_totle_time / old_totle) * 1000), "最小花费：", (old_min_time * 1000), "最大花费：", (old_max_time * 1000), )
