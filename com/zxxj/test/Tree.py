class Node:
    def __init__(self,left,right,data):
        self.left = left
        self.right = right
        self.data = data
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
        self.len = 0

    def isBalanced(self,root):
        d1 = 0
        d2 = 0
        if root.left:
            d1 = self.layerDeep(root.left)
        if root.right:
            d2 = self.layerDeep(root.right)
        return d1 - d2

    def turnL(self,root):
        temp = root.right
        root.right = temp.left
        temp.left = root
        return temp

    def turnR(self,root):
        temp = root.left
        root.left = temp.right
        temp.right = root
        return temp

    def append(self, data):
        if not self.root:
            self.root = Node(None,None,data)
            self.len +=1
            return
        root = self.root
        while 1:
            if data > root.data:
                if not root.right:
                    root.right = Node(None,None,data)
                    self.len += 1
                    break
                root = root.right
            elif data < root.data:
                if not root.left:
                    root.left = Node(None,None,data)
                    self.len += 1
                    break
                root = root.left
            else:
                break
        if self.len%100 ==0:
            self.root = self.toBalanced(self.root)

    def delete(self,data):
        if not self.root:
            return -1
        root = self.root
        tem = root
        pre = Node(root,None,None)
        while 1:
            if data > root.data:
                if not root.right:
                    return -1
                pre = root
                root = root.right
            elif data < root.data:
                if not root.left:
                    return -1
                pre = root
                root = root.left
            else:
                break
        if root.left is None and root.right is None:
            if pre.left == root:
                pre.left = None
            else:
                pre.right = None
        elif root.left is not None and root.right is None:
            tem = root.left
            if pre.left == root:
                pre.left = root.left
            else:
                pre.right = root.left
        elif root.left is None and root.right is not None:
            tem = root.right
            if pre.left == root:
                pre.left = root.right

            else:
                pre.right = root.right

        elif root.left is not None and root.right is not None:

            if pre.left == root:
                tem = root.ritht
                while tem.right:
                    tem = tem.right
                tem.left = root.left
                tem.right = root.right
                pre.left = tem
            else:
                tem = root.left
                while tem.right:
                    tem = tem.right
                tem.left = root.left
                tem.right = root.right
                pre.right = tem
        if data == self.root.data:
            self.root = tem
        return 1

    def find(self,data):
        root = self.root
        while root :
            if data > root.data:
                root = root.right
            elif data < root.data:
                root = root.left
            else:
                return data
        return -1



    def toBalanced(self,root):
        if root.right:
            root.right = self.toBalanced(root.right)
        if root.left:
            root.left = self.toBalanced(root.left)
        a = self.isBalanced(root)
        temp = root
        if a > 1:
            if self.isBalanced(root.left) > 0:
                temp = self.turnR(root)
            else:
                root.left = self.turnL(root.left)
                temp = self.turnR(root)
        elif a < -1:
            if self.isBalanced(root.right) < 0:
                temp = self.turnL(root)
            else:
                root.right = self.turnR(root.right)
                temp = self.turnL(root)
        return temp

    def layerDeep(self,root):
        list = [root]
        depth = 0
        while list:
            templist = []
            for i in list:
                if i.left:
                    templist.append(i.left)
                if i.right:
                    templist.append(i.right)
            list = templist
            depth +=1
        return depth



    def printLayer(self,root):
        depth = self.layerDeep(root) -1
        list = [root]
        print('  ' * depth, end='')
        print(root)
        for i in range(depth):
            templist = []
            for i in list:
                if i == '#':
                    templist.append('#')
                    templist.append('#')
                    continue
                if i.left:
                    templist.append(i.left)
                else:
                    templist.append('#')
                if i.right:
                    templist.append(i.right)
                else:
                    templist.append('#')
            depth -=1
            list = templist
            print('  '*depth,end='')
            for i in templist:
                if i != '#':
                    print(i.data,end=' ')
                else:
                    print('#',end='')
                    pass
            print()

    def printAll(self,root):
        if root:
            self.printAll(root.left)
            print(root.data,end=',')
            self.printAll(root.right)


if __name__ == '__main__':
    tree = Tree()
    tree.append(1)
    tree.append(2)
    tree.append(3)
    tree.append(4)
    tree.append(5)









    print(tree.layerDeep(tree.root))

    tree.root = tree.toBalanced(tree.root)
    tree.printLayer(tree.root)
    print('共有' + str(tree.layerDeep(tree.root)) + '层')
    tree.printall(tree.root)



