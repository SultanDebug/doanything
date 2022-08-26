import json
import time

import requests
import threading

filename = "D:\projectpublicity.txt"
rows = []
with open(filename, "r", encoding='utf-8') as file_csv:  # 是不是忘记了如何打开文件？打开文件，并将结果文件对象存储在file_csv中
    for idx in range(800):
        cont = file_csv.readline()
        if len(cont) == 0:
            break
        rows.append(cont)


def run(type):
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

            req = json.loads(body.get('request'))
            query = req.get('query')

            if reduce * 1000 > 200:
                # querys.append(row + "==>" + reduce)
                querys.append("{}==>{}".format(query, reduce))

            res = json.loads(r.content.decode('utf-8'))
            success = res.get('success')
            if success:
                suc = suc + 1
            else:
                fail = fail + 1

            # print("查询==>", query)
        except:
            print("新接口==>", row, "error")
            err = err + 1

    print("类型：", type, "接口总数：", totle, "成功：", suc, "失败：", fail, ",超时：", querys, "最小花费：", (min_time * 1000),
          "最大花费：",
          (max_time * 1000))


threads = []

for i in range(10):
    thread1 = threading.Thread(target=run, kwargs={'type': i})
    thread1.start()
    threads.append(thread1)

for threadtmp in threads:
    threadtmp.join()
