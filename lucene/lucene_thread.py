import lucene_search
import threading

filename = "C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\testfile\com_thread.txt"
rows = []
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        rows.append(line)

results = []


def search(rows=None):
    newdict = {}
    new_obj = lucene_search.search(rows)
    newdict["totle"] = new_obj["totle"]
    newdict["suc"] = new_obj["suc"]
    newdict["fail"] = new_obj["fail"]
    newdict["err"] = new_obj["err"]
    newdict["totle_time"] = new_obj["totle_time"]
    newdict["min_time"] = new_obj["min_time"]
    newdict["max_time"] = new_obj["max_time"]
    results.append(newdict)


threads = []

i = 0
while True:
    end = i + 1000
    if end >= len(rows):
        end = len(rows)
    tmps = rows[i:end]
    thread = threading.Thread(target=search, kwargs={'rows': tmps})
    thread.start()
    threads.append(thread)
    if end == len(rows):
        break
    i = end

for threadtmp in threads:
    threadtmp.join()

totle = 0
suc = 0
fail = 0
err = 0
totle_time = 0
min_time = 0
max_time = 0

for res in results:
    totle += res["totle"]
    suc += res["suc"]
    fail += res["fail"]
    err += res["err"]
    totle_time += res["totle_time"]
    min_time += res["min_time"]
    max_time += res["max_time"]

print("新接口总数：", totle, ",正确：", suc, ",失败：", fail, ",异常：", err, ",总花费：", (totle_time * 1000), ",平均花费：",
      ((totle_time / totle) * 1000), ",最小花费：", (min_time * 1000), ",最大花费：", (max_time * 1000), )
