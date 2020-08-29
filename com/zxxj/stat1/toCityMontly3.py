import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


if __name__ == "__main__":

    file = pd.read_csv("I:/cache/城市_20152017_result/day_data.csv")
    df = pd.DataFrame(file)
    df["type"] = df["type"].astype('category')
    df["date"]=pd.to_datetime(df['date'],format="%Y%m%d")

    df.drop("hour", axis=1, inplace=True)
    df.set_index("date", inplace=True)
    ll = df.groupby("type")
    ll2 = []
    for i in ll:
        df2 = i[1].to_period("M").groupby("date").mean()
        df2["type"] = i[0]
        ll2.append(df2)

    result = pd.concat(ll2)
    result.reset_index(inplace=True)
    result.set_index(["date","type"], inplace=True)
    result.reset_index(inplace=True)
    result["date"] = result["date"].astype('category')
    result.rename(columns={'date':'month'}, inplace = True)

    result.set_index(["month","type"], inplace=True)
    result = result.stack()
    result = result.reset_index()
    result.rename(columns={'level_2': '城市',0:"值"}, inplace=True)
    print(result)

    # print(result.head(5))
    result.to_excel("I:/cache/城市_20152017_result/month_data_格式2.xlsx",encoding="utf_8_sig")

    # print(df2)
    # print(df[df["type"] == "AQI"]["北京"].mean())

