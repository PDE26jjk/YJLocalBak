import copy

class OneWayLinkedList:
    class ElemType:
        def __init__(self,data,next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = self.ElemType(None, None)
        self.last = self.head
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def append(self,data):
        node = self.ElemType(data,None)
        self.last.next = node
        self.last = node
        self.size += 1

    def printAll(self):
        node = self.head.next

        while node is not None:
            print(node.data,end=",")
            node = node.next


    def getNode(self,index=0):
        if index == -1:
            return self.head
        if index >= self.size or index < 0:
            return None
        node = self.head
        for i in range(index + 1):
            node = node.next
        return node

    def index(self,index=0):
        return self.getNode(index).data

    def insert(self,data,index):
        onode = self.getNode(index)
        nnode = self.ElemType(data,onode.next)
        onode.next = nnode
        self.size += 1

    def insertLinkedList(self, list,index=0,listIn1 : int = 0,listIn2 : int = 0):
        onode = self.getNode(index)
        pnode = onode.next
        listNode = list.getNode(listIn1)
        for i in range(listIn2-listIn1):
            newNode = copy.deepcopy(listNode)
            onode.next = newNode
            listNode = listNode.next
            onode = newNode
        onode.next = pnode
        self.size += listIn2-listIn1


    def delete(self,index):
        pnode = self.getNode(index-1)
        dnode = pnode.next
        pnode.next = dnode.next
        dnode.next = None
        self.size -= 1

    def select(self,data):
        node = self.head
        index = -1
        while node is not None and node.data != data :
            node = node.next
            index += 1
        if node is not None:
            return index
        return -1

    def getInd(self, node):
        inode = self.head
        index = -1
        while inode != node:
            inode = inode.next
            index += 1
        return index

    def swapI(self, index1 = -1, index2 = -1):
        if index1 == index2:
            return
        pn1 = self.getNode(index1 - 1)
        pn2 = self.getNode(index2 - 1)
        n1 = pn1.next
        n2 = pn2.next
        pn1.next = n2
        pn2.next = n1
        n1.next, n2.next = n2.next, n1.next


    def swapN(self, n1, n2):
        index1 = self.getInd(n1)
        index2 = self.getInd(n2)
        self.swapI(index1,index2)


    def sort(self):
        for j in range(self.size-1):
            node = self.head
            while node.next.next != None :
                if node.next.data > node.next.next.data:
                    n2 = node.next
                    n3 = node.next.next
                    n2.next = n3.next
                    n3.next = n2
                    node.next = n3
                node=node.next
class SinglyLinkedListWithoutHead:
    '''元素类'''
    class ElemType:
        def __init__(self, data, next):
            self.data = data
            self.next = next
    def __init__(self):
        self.size = 0
        self.first = self.ElemType(None,None) #定义首元素
        self.first.next = self.first
    '''插入数据'''
    def insert(self,index,data):
        if index > self.size or index < 0:
            print("index error")
            return
        if index == 0 and self.size == 0:
            self.first.data = data
        else:
            p = self.first
            '''前一个元素'''
            for i in range(index-1):
                p = p.next
            p.next = self.ElemType(data, p.next)
        self.size += 1
    '''删除数据'''
    def delete(self,index):
        if index > self.size or index < 0:
            print("index error")
            return
        if self.size == 0:
            print("size = 0")
            return
        if index == 0:
            p = self.first
            for i in range(self.size - 1):
                p = p.next
            self.first = self.first.next
            p.next = self.first
        else:
            p = self.first
            '''前一个元素'''
            for i in range(index-1):
                p = p.next
            p.next = p.next.next
        self.size -= 1
    '''追加数据'''
    def append(self,data):
        self.insert(self.size,data)

    def printAll(self):
        node = self.first
        print("[",end="")
        for i in range(self.size):
            print(node.data,end="")
            if node.next != self.first and node.next is not None:
                print(",",end="")
            node = node.next
        print("]")

if __name__ == '__main__':
    list  = OneWayLinkedList()
    list.append({"k1":1})
    list.append(2)
    list.delete(1)
    list.printAll()