# 使用scipy库
from scipy import optimize
from scipy.optimize import linprog
from scipy.optimize import minimize
import numpy as np
import math
from pprint import pprint
# 使用pulp库
import pulp
import sys

sys.setrecursionlimit(1000000)

def transporstation_problem(costs, x_max, y_max):
    row = len(costs)
    col = len(costs[0])
    prob = pulp.LpProblem('Transportation_Problem',sense=pulp.LpMaximize)
    var = [[pulp.LpVariable(f'x{i}{j}',lowBound=0, cat=pulp.LpInteger)
            for j in range(col)]for i in range(row)]
    # 递归方式使数组摊平
    flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
    prob += pulp.lpDot(flatten(var),costs.flatten())
    for i in range(row):
        prob += (pulp.lpSum(var[i]) <= x_max[i])
    for j in range(col):
        prob += (pulp.lpSum([var[i][j] for i in range(row)]) <= y_max[j])
    prob.solve()
    return {'objective':pulp.value(prob.objective),
            'var':[[pulp.value(var[i][j]) for j in range(col)]for i in range(row)]}

def integerPro(c,A,b,Aeq,beq,t=1.0E-10):
    res = linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq)
    # 出界或运算出错就返回一个大值，将其排除
    if(type(res.x) is float or not res.success):
        bestX = [sys.maxsize] * len(c)
    else:
        bestX = res.x
    bestVal = sum([x*y for x,y in zip(c, bestX)])
    print(bestX, bestVal)
    if all(((x-math.floor(x))<t or (math.ceil(x)-x) < t) for x in bestX):
        return (bestVal, bestX)
    else:
        ind = [i for i,x in enumerate(bestX) if (x-math.floor(x))>t and (math.ceil(x)-x)>t][0]
        newCon1 = [0] * len(A[0])
        newCon2 = [0] * len(A[0])
        newCon1[ind] = -1
        newCon2[ind] = 1
        newA1 = A.copy()
        newA2 = A.copy()
        newA1.append(newCon1)
        newA2.append(newCon2)
        newB1 = b.copy()
        newB2 = b.copy()
        newB1.append(-math.ceil(bestX[ind]))
        newB2.append(math.floor(bestX[ind]))
        r2 = integerPro(c,newA2,newB2,Aeq,beq)
        r1 = integerPro(c,newA1,newB1,Aeq,beq)

        if r1[0] < r2[0]:
            return r1
        else:
            return r2

if __name__ == "__main__":
    #使用scipy库
    c = np.array([2,3,-5])
    A = np.array([[-2,5,-1],[1,3,1]])
    B = np.array([-10,12])
    Aeq = np.array([[1,1,1]])
    Beq = np.array([7])

    res = optimize.linprog(-c,A,B,Aeq,Beq)
    print(res)
    print("-------")

    #使用pulp库

    z = [2,3,1]
    a = [[1,4,2],[3,2,0]]
    b = [8,6]
    # 确定是最大化问题
    m = pulp.LpProblem(sense=pulp.LpMinimize)
    # 三个变量
    x = [pulp.LpVariable(f'x{i}',lowBound=0) for i in [1,2,3]]
    m += pulp.lpDot(z, x)

    for i in range(len(a)):
        m += (pulp.lpDot(a[i], x) >= b[i])

    m.solve()
    print(f'优化结果：{pulp.value(m.objective)}')
    print(f'参数取值:{[pulp.value(var) for var in x]}')

    costs = np.array([[500,550,630,1000,800,700],
                      [800,700,600,950,900,930],
                      [1000,960,840,650,600,700],
                      [1200,1040,980,860,880,780]])
    max_plant = [76,88,96,40]
    max_cultivation = [42,56,44,39,60,59]
    res = transporstation_problem(costs,max_plant,max_cultivation)
    print(f'最大值为{res["objective"]}')
    print('各变量取值为')
    print(res['var'])

    c = [3,4,1]
    A = [[-1,-6,-2],[-2,0,0]]
    b = [-5,-3]
    Aeq = [[0,0,0]]
    beq = [0]
    print(integerPro(c,A,b,Aeq,beq))

    # 非线性规划
    def fun(args):
        a,b,c,d = args
        v= lambda x : (a + x[0]/b+x[1] - c* x[0] + d*x[2])
        return v
    def con(args):
        x1min,x1max,x2min,x2max,x3min,x3max = args
        cons = ({'type':'ineq','fun':lambda x:x[0] - x1min},\
                {'type':'ineq','fun':lambda x:-x[0] + x1max},\
                {'type':'ineq','fun':lambda x:x[1] - x2min},\
                {'type':'ineq','fun':lambda x:-x[1] + x2max},\
                {'type':'ineq','fun':lambda x:x[2] - x3min},\
                {'type':'ineq','fun':lambda x:-x[2] + x3max},)
        return cons

    args = (2,1,3,4)
    args1 = (0.1,0.9,0.1,0.9,0.1,0.9)
    cons = con(args1)
    x0 = np.asarray((0.5,0.5,0.5))
    res = minimize(fun(args),x0,method='SLSQP',constraints=cons)
    print(res.fun)
    print(res.success)
    print(res.x)