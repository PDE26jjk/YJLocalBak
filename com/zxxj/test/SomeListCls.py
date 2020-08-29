
class SomeList:
    def __init__(self):
        "初始化顺序表函数"
        self.SeqList = []
    def __init__(self,list=[]):
        "初始化顺序表函数"
        self.SeqList = list
    def DestorySequenceList(self):
        "销毁顺序表函数"
        del self.SeqList[:]
        print("顺序表已成功销毁！")

    def GetLength(self):
        "获取顺序表长度函数"
        length = len(self.SeqList)
        print("顺序表 SL 中元素的个数为", length, "个")

    def FindElement(self):
        "查找表中某一元素函数"
        key = int(input('请输入想要查找的元素值：'))
        if key in self.SeqList:
            ipos = self.SeqList.index(key)
            print("查找成功！值为%d的元素，位于当前顺序表的第%d个位置。" % (self.SeqList[ipos],ipos + 1 ))
        else:
            print("查找失败！当前顺序表中不存在值为", key, "的元素")

    def InsertElement(self):
        "定位插入元素函数"
        iPos = int(input('请输入待插入元素的位置：'))
        Element = int(input('请输入待插入的元素值：'))
        self.SeqList.insert(iPos, Element)
        print("成功插入元素", Element)

    def DeleteElement(self):
        "删除列表元素函数"
        dElement = int(input('请输入需要删除元素的值：'))
        if dElement in self.SeqList:
            dPos = self.SeqList.index(dElement)
            del self.SeqList[dPos]
            print("成功删除元素", dElement)
        else:
            print("表中不存在该元素")

    def TraverseElement(self):
        "遍历顺序表函数"
        SeqListLen = len(self.SeqList)
        print("------------------遍历顺序表中元素------------------")
        for i in range(0, SeqListLen):
            print("第", i + 1, "个元素的值为", self.SeqList[i])
