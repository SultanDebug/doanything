import json
import time
import requests

filename = "C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\testfile\com_name.txt"
rows = []
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        rows.append(line)

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

        # host="http://192.168.200.91:8080"  #部署的服务器地址
        # login_url="/chun5/user/login"  #请求地址
        url = "http://172.16.5.233:8888/shard/single/query?index=enterprise&query="+query

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

print("老接口总数：", totle, ",正确：", suc, ",失败：", fail, ",异常：", err, ",总花费：", (totle_time * 1000), ",平均花费：",
      ((totle_time / totle) * 1000), ",最小花费：", (min_time * 1000), ",最大花费：",
      (max_time * 1000), )