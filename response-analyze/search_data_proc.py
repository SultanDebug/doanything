import csv

filename = "D:\data.csv"
rows = []
with open(filename, "r", encoding='utf-8') as file_csv:  # 是不是忘记了如何打开文件？打开文件，并将结果文件对象存储在file_csv中
    reader = csv.reader(file_csv)  # 直接调读取 用csv.read()读取文件内容

    json_data = []
    # row = []
    for item in reader:  # 用for循环打印每一行
        rows.append(item[0].strip())

pos = 0
for row in rows:
    arr = row.split("||")
    query = arr[0].strip()
    proid = arr[1].strip()

    if len(query) >= 6:
        str1 = query[0:3] + query[5:len(query)]
        rows[pos] = str1
    print(rows[pos], "||", proid)
    pos = pos + 1
