import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def y2_(x):
    return 6600*(np.exp(-0.1155*x)-np.exp(-0.1386*x))
# 画方程线
if __name__ == "__main__":
    # 根据个数生成序列
    x = np.linspace(0, 25, 300)
    y1 = 1100*np.exp(-0.1386*x)
    y2 = y2_(x)
    print(y2_(2))
    plt.figure(figsize=(5, 3), dpi=80)
    plt.xlim([0,25])
    plt.ylim([0,1200])


    plt.plot(x,y1,color="blue")
    plt.plot(x,y2,color="red")
    plt.legend(["x(t)", "y(t)"])

    plt.show()