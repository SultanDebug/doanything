import json
import time
import sys
import pandas as pd

import requests

filename = ""
rows = []
with open(filename, "r", encoding='utf-8') as file:  # 是不是忘记了如何打开文件？打开文件，并将结果文件对象存储在file_csv中
    line = file.readline()
    cnt=0
    while line:
        rows.append(line)
        line = file.readline()
        cnt +=1
        if cnt%2==0:
            print(f"加载: [{cnt}]", end='\r')
    print(f"加载: [{cnt}]")

result_set = list()
cnt=0
for row in rows:
    try:
        # host=""  #部署的服务器地址
        # login_url=""  #请求地址
        url = ""  # 拼接地址
        row = row.replace('\n', '')
        query = ''
        # 参数
        body = json.loads(query)
        body["query"] = row
        # 发送请求
        begin = time.time()
        r = requests.post(url=url, json=body)
        end = time.time()

        reduce = end - begin

        res = json.loads(r.content.decode('utf-8'))

        extend = res["extend"]
        del extend["searchFields"]
        query_bright = extend["brightQuery"]
        del extend["brightQuery"]

        buids = list()

        for item in res["docs"]:
            buids.append(item["eid"])

        req = ''
        req_obj = json.loads(req)

        req_obj['busIds'] = buids
        req_obj['extend'] = extend
        req_obj['query'] = query_bright

        req_str = json.dumps(req_obj,ensure_ascii=False)
        result_set.append(req_str+'\n')

        cnt += 1
        per = (cnt*100) / len(rows)
        end= '\r'
        if cnt==len(rows):
            end='\n'
        print(f"搜索请求: [{per}%]", end=end)


    except json.JSONDecodeError as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"异常类型：{exc_type}，{exc_value}，{exc_traceback}")
reslen = len(result_set)
print(f'最终请求数{reslen}')


filename = ""
with open(filename, mode='w', encoding='utf-8') as file:
    file.writelines(result_set)
