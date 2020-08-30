from sympy import *


# 解方程
if __name__ == "__main__":
    x = Symbol("x")

    # print(solve([6600*(exp(-0.1155*x)-exp(-0.1386*x))-400],[x]))#解不出来，卡死
    #看图找到所求解在5附近，在其左右找近似解
    print(nsolve(6600*(exp(-0.1155*x)-exp(-0.1386*x))-400,5))
    