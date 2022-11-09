import pandas as pd

rows = []

with open("C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\pydata\\area_data.txt", 'r', encoding='utf-8') as file:
    for line in file:
        rows.append(line)

pros = []
citys = []
areas = []

for row in rows:
    arr = row.split(",")
    code = arr[0]
    name = arr[1]

    code1 = code[2:4]
    code2 = code[4:6]

    if code1 == '00':
        pros.append(name)
    elif code2 == '00':
        citys.append(name)
    else:
        areas.append(name)


prov_set = set()
for row in pros:
    query_length = len(row)
    if row and query_length >= 2:
        prov_set.add(row)
        for i in range(3, query_length):
            tmp_addr = row[:i]
            prov_set.add(tmp_addr)

city_set = set()
for row in citys:
    query_length = len(row)
    if row and query_length >= 2:
        city_set.add(row)
        for i in range(3, query_length):
            tmp_addr = row[:i]
            city_set.add(tmp_addr)


area_set = set()
for row in areas:
    query_length = len(row)
    if row and query_length >= 2:
        area_set.add(row)
        for i in range(3, query_length):
            tmp_addr = row[:i]
            area_set.add(tmp_addr)

df1 = pd.DataFrame(prov_set, columns=["prov"])

df1 = df1.sort_values(by="prov", ascending=True)

df1.to_csv('C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\pydata\\addr\\prov.csv', encoding="utf_8_sig", index=False, header=False)

df2 = pd.DataFrame(city_set, columns=["city"])

df2 = df2.sort_values(by="city", ascending=True)

df2.to_csv('C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\pydata\\addr\\city.csv', encoding="utf_8_sig", index=False, header=False)

df3 = pd.DataFrame(area_set, columns=["area"])

df3 = df3.sort_values(by="area", ascending=True)

df3.to_csv('C:\\Users\\zhenqiang.huang\\Desktop\\searchprocess\\pydata\\addr\\area.csv', encoding="utf_8_sig", index=False, header=False)

print('省：', len(pros), '市：', len(citys), '区：', len(areas))
