import pandas as pd

if __name__ == '__main__':

    city_file = "./data/city.csv"

    # 读取文件
    df_city = pd.read_csv(city_file, encoding='utf-8', header=0, sep='\u0001', names=["city"]).fillna("")

    df_city = df_city.drop_duplicates(["city"])
    # 保存接口返回结果
    result_set = set()

    # 遍历用户city
    for index, row in df_city.iterrows():
        query = row["city"]
        query_length = len(query)
        if query and query_length >= 2:
            result_set.add(query)
            for i in range(2, query_length):
                tmp_addr = query[:i]
                result_set.add(tmp_addr)

    df = pd.DataFrame(result_set, columns=["city"])

    df = df.sort_values(by="city", ascending=True)

    df.to_csv('./data/city_handle.csv', encoding="utf-8", index=False, header=False)
