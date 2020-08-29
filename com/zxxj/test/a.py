class DoublyLinkedListWithoutHead:
    '''元素类'''

    class ElemType:
        def __init__(self, data, next, prior):
            self.data = data
            self.next = next
            self.prior = prior
            # 查了之后发现python有重载运算符的办法，这就好办了嘛

        '''定义加法'''

        def __add__(self, other):
            node = self
            for i in range(other):
                node = self.next
            return node

        '''定义减法'''

        def __sub__(self, other):
            node = self
            for i in range(other):
                node = self.prior
            return node

    def __init__(self):
        self.size = 0
        self.first = self.ElemType(None, None, None)  # 定义首元素
        self.first.next = self.first
        self.first.prior = self.first

    '''追加数据'''

    def append(self, data):
        self.insert(self.size, data)

    '''插入数据'''

    def insert(self, index, data):
        if index > self.size or index < 0:
            print("index error")
            return

        if index == 0 and self.size == 0:
            self.first.data = data
        else:
            p = self.first
            '''当前下标所指元素,对算法优化了下'''
            if index < self.size / 2:
                p += index
            else:
                p -= self.size - index
            node = self.ElemType(data, p, p.prior)
            p.prior.next = node
            p.prior = node
        self.size += 1

    '''删除数据'''

    def delete(self, index):
        if index > self.size or index < 0:
            print("index error")
            return
        if self.size == 0:
            print("size = 0")
            return

        p = self.first
        if index == 0:
            self.first.data = None
            self.first = p.next
        '''当前下标所指元素,对算法优化了下'''
        if index < self.size / 2:
            p += index
        else:
            p -= self.size - index
        p.next.prior = p.prior
        p.prior.next = p.next

        self.size -= 1

    def printAllNodes(self):
        node = self.first
        print("[", end="")
        for i in range(self.size):
            print(node.data, end="")
            if node.next != self.first and node.next is not None:
                print(",", end="")
            node = node.next
        print("]")

    def delX(self, x):
        p = self.first
        while True:
            if p.data == x:
                if p == self.first:
                    self.delete(0)
                    p += 1
                else:
                    p.prior.next = p.next
                    p.next.prior = p.prior
                    self.size -= 1;
            p += 1
            if p == self.first and p.data != x:
                return

    def __contains__(self, item):
        node = self.first
        for i in range(self.size):
            if node.data == item:
                return True
            node = node.next

    def __iter__(self):
        return self.it(self.first, self.size)

    class it:
        def __init__(self, first, size):
            self.i = 1
            self.size = size
            self.p = first

        def __next__(self):
            try:
                if self.i > self.size:
                    raise StopIteration
                return self.p.data
            finally:
                self.p += 1
                self.i += 1


list = DoublyLinkedListWithoutHead()

list.append(22)
list.append(2)
list.append(3)
list.append(22)
list.append(5235)

# list.printAllNodes()


for i in list:
    if i % 2 == 1:
        list.delX(i)
list.printAllNodes()