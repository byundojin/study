class HeapTree():
    tree = [None]

    def insert(data:int):
        pass

    def delete():
        pass

class MinHeapTree(HeapTree):
    def insert(data:int):
        tree = MinHeapTree.tree
        index = len(tree)
        tree.append(data)
        while tree[index] < tree[index//2]:
            p = tree[index]
            tree[index] = tree[index//2]
            tree[index//2] = p
            index //= 2
            if index == 1:
                break

    def delete():
        tree = MinHeapTree.tree
        if len(tree) == 1:
            return
        elif len(tree) == 2:
            tree.pop()
        else:
            tree[1] = tree.pop()
            index = 1
            child = []
            if len(tree) > index*2:
                child.append(tree[index*2])
            if len(tree) > index*2+1:
                child.append(tree[index*2+1])
            while 
            
