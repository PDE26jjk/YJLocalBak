import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(0,2*np.pi+np.pi/4,10)
    y = np.sin(x)
    x_new = np.linspace(0,2*np.pi+np.pi/4,100)
    f_linear = interpolate.interp1d(x, y)
    tck = interpolate.splrep(x,y)
    y_bspline = interpolate.splev(x_new, tck)

    plt.xlabel(u'安倍/A')
    plt.ylabel(u'伏特/A')
    plt.plot(x,y,"o",label="原始数据")
    plt.plot(x_new, f_linear(x_new),label="线性差值")
    plt.plot(x_new, y_bspline,label="B-spline差值")
    plt.legend()
    plt.show()



