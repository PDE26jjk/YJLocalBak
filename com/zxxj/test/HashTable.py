import math

def hash(data):
    a = abs(data) + 12345
    a = a ** 2
    return int(str(a)[2:8])

class HashTable:
    def __init__(self,hash=hash):
        self.table = [None]*5669
        self.hash = hash
        self.len = len(self.table)
        self.usedLen = 0

    def getIndex(self,data):
        hashCode = abs(self.hash(data))
        return (hashCode % self.len)-1

    def append(self, data):
        index = self.getIndex(data)
        slot = self.table[index]
        if slot:
            if data in slot:
                return
            else:
                slot.append(data)
        else:
            self.table[index] = [data]
            self.usedLen +=1

    def find(self,data):
        index = self.getIndex(data)
        slot = self.table[index]
        if slot:
            if data in slot:
                return index
            else:
                return -1
        return -1


    def delete(self,data):
        index = self.getIndex(data)
        slot = self.table[index]
        if slot:
            for i in slot:
                if i == data:
                    slot.remove(i)
                    return index
            else:
                return -1
        return None
    def printAll(self):
        for i,slot in enumerate(self.table):
            if slot:
                for j in slot:
                    print(j,end=',')


if __name__ == '__main__':

    ht = HashTable(hash)


    import random
    import time

    ht.printAll()

