import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ########读取################
    file = pd.read_csv('./aqi.csv')
    df = pd.DataFrame(file)
    # 表示去掉所有包含缺失值的行
    # print(df.dtypes)
    # 开头5行
    ########查看################
    print(df.head(5))
    # 结尾5行
    print(df.tail(5))
    print(df.dtypes)
    df["日期"]=pd.to_datetime(df['日期'],format="%Y/%m/%d")
    print(df.head(5))
    df = df.sort_values(by=["城市","日期"], ascending=False)
    df["城市"] = df["城市"].astype('category')
    print(df.head(5))
    # df["Y"] = [i.year for i in df["日期"]]
    df.set_index("日期",inplace=True)
    print("--------------------")
    ll = list(df.groupby("城市"))  # 按列分组
    # df2 = pd.DataFrame({"1":[],"2":[],"3":[]})
    ll2 = []
    print("--------------------")

    for i in ll:
        # print(i[1].dtypes)
        df3 = pd.DataFrame(i[1].to_period("M")["AQI"].groupby("日期").mean())
        df3["城市"] = i[0]
        ll2.append(df3)
    #
    result = pd.concat(ll2)
    result.reset_index(inplace=True)
    result["日期"] = result["日期"].astype('category')

    result.to_excel('./AQI结果.xlsx')

    # df["m"] = [i.month for i in df["日期"]]
    # print(df.head(5))