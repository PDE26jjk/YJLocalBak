import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 利用等高线绘制方程
if __name__ == "__main__":
    # 根据间距生成序列
    x = np.arange(-10,10,1)
    y = np.arange(-10,10,1)
    # 根据个数生成序列
    x = np.linspace(-10, 10, 300)
    y = np.linspace(-10,10,30)
    x,y = np.meshgrid(x,y)
    z = y - np.power(x,2)
    z2 = y - np.power(x,3)
    # 等高线轮廓线
    plt.contour(x,y,z,0,colors=['blue'])
    plt.contour(x, y, z2, 0,colors=['blue'])
    print(x.shape,y.shape,z.shape)
    print(x,y,z)
    # 等高线
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # ax.scatter(x, y, z)


    plt.show()