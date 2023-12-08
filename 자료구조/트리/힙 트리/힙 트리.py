class HeapTree():
    def __init__(self) -> None:
        self.tree = [None]

    def compare(self, index1, index2=None) -> bool:
        pass
        
    def rotate(self, index1, index2=None):
        tree = self.tree
        if index2:
            p = tree[index2]
            tree[index2] = tree[index1]
        else:
            p = tree[index1//2]
            tree[index1//2] = tree[index1]
        tree[index1] = p


    def insert(self, data:int):
        tree = self.tree
        index = len(tree)
        tree.append(data)
        if index == 1:
            return
        
        while index > 1:
            if self.compare(index):
                self.rotate(index)
                index //= 2
            else:
                break 

    def delete(self):
        tree = self.tree
        if len(tree) == 1:
            return "tree is empty"
        data = tree[1]
        tree[1] = tree[-1]
        tree.pop()
        if len(tree) == 1:
            return data
        index = 1 
        while index * 2 < len(tree):
            if index * 2 + 1 < len(tree):
                child_index = index*2 if self.compare(index*2, index*2+1) else index*2+1
                if self.compare(child_index, index):
                    self.rotate(index, child_index)
                else:
                    break
                index *= 2
            else:
                if self.compare(index * 2, index):
                    self.rotate(index, index * 2)
                break
        return data

class MinHeapTree(HeapTree):
    def __init__(self) -> None:
        super().__init__()
        
    def compare(self, index1, index2=None) -> bool:
        tree = self.tree
        if index2:
            if tree[index2] > tree[index1]:
                return True
        else:
            if tree[index1//2] > tree[index1]:
                return True
        return False
    
class MaxHeapTree(HeapTree):
    def __init__(self) -> None:
        super().__init__()
        
    def compare(self, index1, index2=None) -> bool:
        tree = self.tree
        if index2:
            if tree[index2] < tree[index1]:
                return True
        else:
            if tree[index1//2] < tree[index1]:
                return True
        return False



min_tree = MinHeapTree()

for i in range(5, 0, -1):
    min_tree.insert(i)
    print(min_tree.tree)

min_tree.delete()
print(min_tree.tree)

max_tree = MaxHeapTree()

for i in range(5):
    max_tree.insert(i)
    print(max_tree.tree)

max_tree.delete()
print(max_tree.tree)



