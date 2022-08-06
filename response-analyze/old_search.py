import json
import time

import requests


def old_search(rows):
    old_policy_url = "http://wzalgo-gateway-v2-pre-lan.qizhidao.com/general-search/search"

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
            # publicity_library_project_all （获批名单）
            # merge_subsidy_document （项目简介）
            # 广东省：440000	深圳市：440300
            # 浙江省：330000	温州市：330300
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
            print("旧接口==>", flag, "/", arr[0], "/", arr[1])
        except:
            print("旧接口==>error==>", "error",row)
            old_err = old_err + 1

    obj = {}
    obj["totle"] = old_totle
    obj["suc"] = old_suc
    obj["fail"] = old_fail
    obj["err"] = old_err
    obj["totle_time"] = old_totle_time
    obj["min_time"] = old_min_time
    obj["max_time"] = old_max_time

    return obj



def old_publicity_search(rows):
    old_policy_url = "http://wzalgo-gateway-v2-pre-lan.qizhidao.com/general-search/search"

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
            # publicity_library_project_all （获批名单）
            # merge_subsidy_document （项目简介）
            # 广东省：440000	深圳市：440300
            # 浙江省：330000	温州市：330300
            # old_policy_request_template = {
            #     "conditions": {
            #         "policyType": "merge_subsidy_document"
            #     },
            #     "current": 1,
            #     "fromSite": "sub",
            #     "pageSize": 3,
            #     "platform": 0,
            #     "searchKey": query,
            #     "type": 7
            # }

            old_policy_request_template = {
                "conditions": {
                    "policyType": "publicity_library_project_all"
                },
                "current": 1,
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
                # if k > 3:
                #     break
                k = k + 1
                # 输出返回
                proid_doc = doc['projectName']
                if proid == proid_doc:
                    flag = True
                    break

            if flag:
                old_suc = old_suc + 1
            else:
                old_fail = old_fail + 1
            print("旧接口==>", flag, "/", arr[0], "/", arr[1])
        except:
            print("旧接口==>error==>", "error",row)
            old_err = old_err + 1

    obj = {}
    obj["totle"] = old_totle
    obj["suc"] = old_suc
    obj["fail"] = old_fail
    obj["err"] = old_err
    obj["totle_time"] = old_totle_time
    obj["min_time"] = old_min_time
    obj["max_time"] = old_max_time

    return obj
