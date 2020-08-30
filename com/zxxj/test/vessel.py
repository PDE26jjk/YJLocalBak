from Tree import *
from HashTable import HashTable
from LinkedList import OneWayLinkedList as LinkedList
class Vessel:
    LinkedList = 0
    HashTable = 1
    Tree = 2
    List = 3
    def __init__(self,type=0):
        self.type = type
        if type == Vessel.LinkedList:
            self.v = LinkedList()
        elif type == Vessel.HashTable:
            self.v = HashTable()
        elif type == Vessel.Tree:
            self.v = Tree()
        elif type == Vessel.List:
            self.v = []
        else:
            return None
    def append(self,data):
        return self.v.append(data)

    def delete(self,data):
        if self.type == Vessel.LinkedList:
            return self.v.delete(self.v.select(data))
        if self.type == Vessel.List:
            return self.v.remove(data)

        return self.v.delete(data)
    def find(self,data):
        if self.type == Vessel.LinkedList:
            return self.v.select(data)
        if self.type == Vessel.List:
            if data in self.v:
                return 1
            return -1
        return self.v.find(data)

    def printAll(self):
        if self.type == Vessel.Tree:
            return self.v.printAll(self.v.root)
        if self.type == Vessel.List:
            for i in self.v:
                print(i,end=',')
            return
        return self.v.printAll()





if __name__ == '__main__':

    import random
    import time

    times = 100
    tem1 = 0
    tem2 = 0
    for j in range(times):
        # 随机插入10000条数据,并计时
        start = time.perf_counter()
        ves = Vessel(type=Vessel.Tree)
        for i in range(10000):
            ves.append(random.randint(-10000, 10000))
        tem1 += (time.perf_counter() - start)
        start = time.perf_counter()
        # 随机查找10000条数据,并计时
        for i in range(10000):
            ves.find(random.randint(-10000, 10000))
        tem2 += (time.perf_counter() - start)

    print('插入时间：'+str(tem1/times))
    print('查找时间：'+str(tem2/times))


