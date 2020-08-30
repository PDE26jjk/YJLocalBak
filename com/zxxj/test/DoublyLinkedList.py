import copy

class DoublyLinkedList:
    class ElemType:
        def __init__(self,data,next,prior):
            self.data = data
            self.next = next
            self.prior = prior

    def __init__(self):
        self.head = self.ElemType(None, None, None)
        self.last = self.head
        self.head.next = self.last
        self.head.prior = self.last
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def append(self,data):
        node = self.ElemType(data,self.head,self.last)
        self.last.next = node
        self.head.prior = self.last
        self.last = node
        self.size += 1

    def printAll(self):
        node = self.head.next
        print("[",end="")
        while node is not None:
            print(node.data,end="")
            if node.next != None :
                print(",",end="")
            node = node.next
        print("]")

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
        nnode = self.ElemType(data,onode.next,onode)
        onode.next.prior = nnode
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

if __name__ == '__main__':
    list  = DoublyLinkedList()
    list.append({"k1":1})
    list.append(2)
    list.delete(1)
    list.printAll()