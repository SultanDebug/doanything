import pandas as pd
import re

xlxs = pd.read_excel("")

pattern = re.compile('^[a-zA-Z0-9 _\-\"“+/.:]*$')

dic = []
i = 0
cnt = 0
while i < xlxs.values.shape[0]:
    val = xlxs.values[i][0]
    sval = str(val)
    # print(sval)
    word = not bool(pattern.match(sval))
    if 2 <= len(sval) < 20 \
            and sval.find("公司") == -1 \
            and sval.find("and") == -1 \
            and sval.find("or") == -1 \
            and sval.find("not") == -1 \
            and word:
        print(cnt, ":", sval)
        dic.append(sval)
        cnt += 1
        if cnt >= 2000:
            break
    i += 1

# print("======处理后结果========")
# j=0
# while j< len(dic) :
#     print(dic[j])
#     j+=1

df = pd.DataFrame(dic)
df.to_csv("process.csv", index=False, encoding="utf8", header=False)
