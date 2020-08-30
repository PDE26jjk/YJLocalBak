import sys
sys.setrecursionlimit(1000000)

# 打印小数点
def div(a,b,num=100):
    """模拟笔算除法，没有四舍五入，递归实现

        @author: PDE

        @param a:被除数
        @type b:int
        @param b:除数
        @type b:int
        @param num:小数点后精度
        @type num:int
        """
    print((int)(a/b),end="")
    print(".",end="")
    d = a % b
    _div(d,b,num)
# 打印0
def _div10(a,b,num):
    if (a!=0) & (a<b) & (num>0):
        a *= 10
        print(0,end="")
        num -= 1
        return _div10(a,b,num)
    return _div(a,b,num)
# 打非0
def _div(a,b,num):
    if (a!=0) & (a<b) & (num>0):
        a *= 10
        return _div10(a,b,num)
    c = (int)(a / b)
    d = a % b
    if num>0:
        print(c,end='')
        num -= 1
        return _div(d,b,num)
    print()
    return


if __name__ == "__main__":
    a = 123456789/987654321
    div(0.1,1,355)
    div(123456789,987654321,355)
    print('%.200f'%a)

    # print(a)
