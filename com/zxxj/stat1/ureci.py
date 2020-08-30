import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm


def get_regre_coef(X, Y):
    S_xy = 0
    S_xx = 0
    S_yy = 0
    # 计算预报因子和预报对象的均值
    X_mean = np.mean(X)
    Y_mean = np.mean(Y)
    for i in range(len(X)):
        S_xy += (X[i] - X_mean) * (Y[i] - Y_mean)
        S_xx += pow(X[i] - X_mean, 2)
        S_yy += pow(Y[i] - Y_mean, 2)
    return S_xy / pow(S_xx * S_yy, 0.5)

def get_vari_contri(r):
    col = data.shape[1]
     #创建一个矩阵来存储方差贡献值
    v=np.ones((1,col-1))
    # print(v)
    for i in range(col-1):
        # v[0,i]=pow(r[i,col-1],2)/r[i,i]
        v[0, i] = pow(r[i, col - 1], 2) / r[i, i]
    return v

#选择因子是否进入方程，
#参数说明：r为增广矩阵，v为方差贡献值，k为方差贡献值最大的因子下标,p为当前进入方程的因子数
def select_factor(r,v,k,p):
    row=data.shape[0]#样本容量
    col=data.shape[1]-1#预报因子数
    #计算方差比
    f=(row-p-2)*v[0,k-1]/(r[col,col]-v[0,k-1])
    # print(calc_vari_contri(r))
    return f

#逐步回归分析与计算
#通过矩阵转换公式来计算各部分增广矩阵的元素值
def convert_matrix(r,k):
    col=data.shape[1]
    k=k-1#从第零行开始计数
    #第k行的元素单不属于k列的元素
    r1 = np.ones((col, col))  # np.ones参数为一个元组(tuple)
    for i in range(col):
        for j in range(col):
            if (i==k and j!=k):
                r1[i,j]=r[k,j]/r[k,k]
            elif (i!=k and j!=k):
                r1[i,j]=r[i,j]-r[i,k]*r[k,j]/r[k,k]
            elif (i!= k and j== k):
                r1[i,j] = -r[i,k]/r[k,k]
            else:
                r1[i,j] = 1/r[k,k]
    return r1

if __name__ == "__main__":
    ########读取################
    file = pd.read_csv('./NYCTB.CSV')
    df = pd.DataFrame(file)
    df = df.dropna(how='any')  # 表示去掉所有包含缺失值的行
    df = df[df["YEAR"] >= 1920]

    df["incidence_rate_w"] = (df["Notifications"] / df["Population"]) * 10000  # 计算发病率

    df["incidence_rate_w_g"] = df["incidence_rate_w"]- 4.857571380814787e+030 * np.exp(-0.0351025131638979 * df["YEAR"].values)

    ls = ["AP", "ATR_c","AAT_c","TM","HM","MIN_T","MAX_T","incidence_rate_w_g"]
    data = df.loc[:, ls].values.copy()
    # plt.plot(df["YEAR"],df["incidence_rate_w_g"])
    # plt.show()
    # x = df.loc[:,["AP","ATR"]].values.reshape(-1,2)
    # x = df.loc[:,["AP"]].values.reshape(-1,1)
    col=data.shape[1]
    # print(col)
    r=np.ones((col,col))
    # print(np.ones((col, col)))
    for i in range(col):
        for j in range(col):
            r[i, j] = get_regre_coef(data[:, i], data[:, j])
    print(r)
    ######画图##########
    f, (ax1) = plt.subplots(figsize=(6, 4), nrows=1)
    cmap = sns.cubehelix_palette(start=1.5, rot=3, gamma=0.8, as_cmap=True)

    # sns.heatmap(r, linewidths=0.05, ax=ax1, vmax=1, vmin=-1, cmap=cmap)
    # sns.heatmap(r, linewidths=0.05, ax=ax1, vmax=1, vmin=-1, annot=True,
    #             annot_kws={'size':9,'weight':'bold', 'color':'green'})

    sns.heatmap(r, linewidths=0.05, ax=ax1, annot=True,
                xticklabels=ls,yticklabels=ls,
                annot_kws={'size':9,'weight':'bold', 'color':'green'})
    plt.show()


    ######画图完##########


    v = get_vari_contri(r)
    print(v)

    f = select_factor(r, v, 3, 0)
    print(f)

    # 矩阵转换，计算第一步矩阵
    r = convert_matrix(r, 4)
    # print(r)
    # 计算第一步方差贡献值
    v = get_vari_contri(r)
    print(v)
    f = select_factor(r, v, 1, 1)
    print(f)












    # y = df["AAT"].values.reshape(-1,1)
    ###训练数据###
    # reg = LinearRegression()
    # reg.fit(x, y)
    # print("The linear model is: Y = {:.5} + {:.5}X".format(reg.intercept_[0], reg.coef_[0][0]))
    # plt.plot(x,y,"o")
    # predictions = reg.predict(x)
    # plt.plot(x, predictions, c='blue', linewidth=2)
    # plt.show()
    # X2 = sm.add_constant(x)
    # est = sm.OLS(y, X2)
    # est2 = est.fit()
