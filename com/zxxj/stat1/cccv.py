import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import exp
if __name__ == "__main__":
    ########读取################
    file = pd.read_csv('./NYCTB.CSV')
    df = pd.DataFrame(file)
    df = df.dropna(how='any')  # 表示去掉所有包含缺失值的行
    # print(df.dtypes)
    # 开头5行
    ########查看################
    print(df.head(5))
    # 结尾5行
    print(df.tail(5))

    print(df.index) # RangeIndex(start=0, stop=151, step=1)
    print(df.columns) # Index(['YEAR', 'AP', 'AAT', 'Notifications', 'TB deaths', 'Population', 'TM', 'HM', 'ATR', 'AAT_c', 'ATR_c'],dtype='object')
    print(df.values) # 所有内容
    print(df.describe()["AP"])# 一般统计
    ########更改排序、筛选################
    print(df.T)
    print(df.sort_index(axis=1, ascending=True)) # 对轴排序
    print(df.sort_values(by="AP", ascending=False)) # 根据ap排序
    print(df.sort_values(by=["AP","AAT"], ascending=False))# 根据ap、aat排序
    print(df[(df["YEAR"]>=1950)&(df["YEAR"]<=1960)][["AP","AAT"]])# 筛选数据
    ########重组################
    print(df.groupby("TM").describe()["YEAR"])# 按列分组
    df["incidence_rate_w"]=(df["Notifications"]/df["Population"])*10000# 计算发病率
    ##################类型操作########################
    print(df.dtypes) # 查看每列类型
    print(df.apply(pd.to_numeric, errors='ignore').dtypes)# 自动适配类型
    # df["HM"]=df["HM"].astype(bool)# 传化为bool类型
    df["HM"]=df["HM"].astype("int64").astype('category')# 传化为category类型

    print(df.dtypes)
    print(df["HM"])
    # df['YEAR'] = pd.to_datetime(df['YEAR'],format="%Y") # 转换为时间序列
    # print(df["YEAR"])
    ######################画图#####################
    x = df["YEAR"]
    y = df["incidence_rate_w"]
    print(df["incidence_rate_w"])

    # plt.rcParams['axes.unicode_minus'] = False # 解决负号是一个矩形的问题
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.plot(x, y, "bo",ls="-", lw=2, label="TB发病率",)
    # plt.legend()
    plt.show()
    x = df["YEAR"].values
    y = 4.857571380814787e+030 * np.exp( -0.0351025131638979 * df["YEAR"].values )

    print(y)