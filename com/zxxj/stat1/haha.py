import random
import numpy as np
import pandas as pd
a = [random.randint(0, 100) for a in range(20)]
b = [random.randint(0, 100) for a in range(20)]


if __name__ == "__main__":
    ab = np.array([a, b])
    print(ab.T)
    # 协方差
    print(np.cov(ab))
    # 相关系数
    print(np.corrcoef(ab))

    # 使用 DataFrame 作为数据结构，为方便计算，我们会将 ab 矩阵转置
    dfab = pd.DataFrame(ab.T, columns=['A', 'B'])
    # A B 协方差
    print(dfab.A.cov(dfab.B))
    # A B 相关系数
    print(dfab.A.corr(dfab.B))
