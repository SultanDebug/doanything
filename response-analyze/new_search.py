import json
import time

import requests


def new_search(rows):
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

            # host="http://192.168.200.91:8080"  #部署的服务器地址
            # login_url="/chun5/user/login"  #请求地址
            url = "http://wzalgo-gateway-v2-test-lan.qizhidao.com/bird-search-engine/bird/search/engine"  # 拼接地址

            # 参数
            # 政策搜索索引名称
            #     项目简介 projectinfo
            #     公示文件 projectpublicity
            #     获批名单 publicitylibrary
            #     申报通知,产业通知，政策资讯 relatematerial
            body = {
                "collectionName": "publicitylibrary",
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
                # if k > 3:
                #     break
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
            print("新接口==>", flag, "/", arr[0], "/", arr[1])
        except:
            print("新接口==>error==>", row)
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
