import csv
import threading
import new_search
import old_search

# class mythread(threading.Thread):
#     def __int__(self, name, paramType):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.paramType = paramType
#
#     def run(self):
#         if self.paramType == 1:
#             new_obj = new_search.new_search(rows)
#             totle = new_obj["totle"]
#             suc = new_obj["suc"]
#             fail = new_obj["fail"]
#             err = new_obj["err"]
#             totle_time = new_obj["totle_time"]
#             min_time = new_obj["min_time"]
#             max_time = new_obj["max_time"]
#
#             print("新接口总数：", totle, ",正确：", suc, ",失败：", fail, "异常：", err, "总花费：", (totle_time * 1000), "平均花费：",
#                   ((totle_time / totle) * 1000), "最小花费：", (min_time * 1000), "最大花费：", (max_time * 1000), )
#         else:
#             old_obj = old_search.old_search(rows)
#             old_totle = old_obj["totle"]
#             old_suc = old_obj["suc"]
#             old_fail = old_obj["fail"]
#             old_err = old_obj["err"]
#             old_totle_time = old_obj["totle_time"]
#             old_min_time = old_obj["min_time"]
#             old_max_time = old_obj["max_time"]
#
#             print("老接口总数：", old_totle, ",正确：", old_suc, ",失败：", old_fail, "异常：", old_err, "总花费：",
#                   (old_totle_time * 1000), "平均花费：",
#                   ((old_totle_time / old_totle) * 1000), "最小花费：", (old_min_time * 1000), "最大花费：",
#                   (old_max_time * 1000), )


filename = "D:\data.csv"
rows = []
with open(filename, "r", encoding='utf-8') as file_csv:  # 是不是忘记了如何打开文件？打开文件，并将结果文件对象存储在file_csv中
    reader = csv.reader(file_csv)  # 直接调读取 用csv.read()读取文件内容

    json_data = []
    # row = []
    for item in reader:  # 用for循环打印每一行
        rows.append(item[0].strip())

newdict = {}
olddict = {}


def search(type=None):
    if type == 1:
        new_obj = new_search.new_search(rows)
        newdict["totle"] = new_obj["totle"]
        newdict["suc"] = new_obj["suc"]
        newdict["fail"] = new_obj["fail"]
        newdict["err"] = new_obj["err"]
        newdict["totle_time"] = new_obj["totle_time"]
        newdict["min_time"] = new_obj["min_time"]
        newdict["max_time"] = new_obj["max_time"]
    else:
        old_obj = old_search.old_publicity_search(rows)
        olddict["totle"] = old_obj["totle"]
        olddict["suc"] = old_obj["suc"]
        olddict["fail"] = old_obj["fail"]
        olddict["err"] = old_obj["err"]
        olddict["totle_time"] = old_obj["totle_time"]
        olddict["min_time"] = old_obj["min_time"]
        olddict["max_time"] = old_obj["max_time"]


# thread1 = mythread("thread-1", 1)
# thread2 = mythread("thread-2", 2)

threads = []

# thread1 = threading.Thread(target=search, kwargs={'type': 1})
# thread1.start()
# threads.append(thread1)

thread2 = threading.Thread(target=search, kwargs={'type': 2})
thread2.start()
threads.append(thread2)

for threadtmp in threads:
    threadtmp.join()

# totle = newdict["totle"]
# suc = newdict["suc"]
# fail = newdict["fail"]
# err = newdict["err"]
# totle_time = newdict["totle_time"]
# min_time = newdict["min_time"]
# max_time = newdict["max_time"]
# print("新接口总数：", totle, ",正确：", suc, ",失败：", fail, ",异常：", err, ",总花费：", (totle_time * 1000), ",平均花费：",
#       ((totle_time / totle) * 1000), ",最小花费：", (min_time * 1000), ",最大花费：", (max_time * 1000), )

old_totle = olddict["totle"]
old_suc = olddict["suc"]
old_fail = olddict["fail"]
old_err = olddict["err"]
old_totle_time = olddict["totle_time"]
old_min_time = olddict["min_time"]
old_max_time = olddict["max_time"]

print("老接口总数：", old_totle, ",正确：", old_suc, ",失败：", old_fail, ",异常：", old_err, ",总花费：", (old_totle_time * 1000), ",平均花费：",
      ((old_totle_time / old_totle) * 1000), ",最小花费：", (old_min_time * 1000), ",最大花费：",
      (old_max_time * 1000), )