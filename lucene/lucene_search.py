import json
import time

import requests


def search(rows):
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

            proid = arr[0].strip()
            query = arr[1].strip()

            # host=""  #部署的服务器地址
            # login_url=""  #请求地址
            url = "" + query

            # 发送请求
            begin = time.time()
            r = requests.get(url=url)
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

            res = json.loads(r.text)
            docs = res.get('data').get('data')
            flag = False
            k = 0
            for doc in docs:
                # if k > 3:
                #     break
                k = k + 1
                # 输出返回
                proid_doc = doc['company_id']
                if proid == proid_doc:
                    flag = True
                    break

            if flag:
                suc = suc + 1
            else:
                fail = fail + 1
            print("新接口==>", totle, "==>", flag, "/", arr[0], "/", arr[1])
        except:
            print("新接口==>", totle, "==>error==>", row)
            err = err + 1

    obj = {}
    obj["totle"] = totle
    obj["suc"] = suc
    obj["fail"] = fail
    obj["err"] = err
    obj["totle_time"] = totle_time
    obj["min_time"] = min_time
    obj["max_time"] = max_time

    return obj
