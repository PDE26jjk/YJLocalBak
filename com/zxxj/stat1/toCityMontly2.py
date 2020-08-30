import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
# 转换成日平均数据
def get_day_data(file):
    df = pd.DataFrame(file)
    df["type"] = df["type"].astype('category')

    # print(df.groupby("type").mean())
    df2 = pd.DataFrame(df.groupby("type").mean())
    return df2

if __name__ == "__main__":

    read_path = 'I:/cache/城市_20152017/'
    save_path = 'I:/cache/城市_20152017_result/'
    os.chdir(read_path)
    csv_name_list = os.listdir()
    ll2 = []

    for i in range(len(csv_name_list)):
        print(read_path + csv_name_list[i])
        file = pd.read_csv(read_path + csv_name_list[i])
        ll2.append(get_day_data(file))

    result = pd.concat(ll2)
    result.to_csv(save_path+'day_data.csv',encoding="utf_8_sig")
    # print(df2)
    # print(df[df["type"] == "AQI"]["北京"].mean())

