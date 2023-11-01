class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.if_find = False

    def __repr__(self) -> str:
        return f"Node:{self.data}"
    
class Tree():
    def __init__(self) -> None:
        self.nodes:list[Node] = [None]

    def add_node(self, node):
        if type(node) != Node:
            node = Node(node)
        self.nodes.append(node)

    def get_node(self, data):
        self.if_find = False
        result = self._dfs_get_node(data)
        return result

    def _dfs_get_node(self, data, index = 1):
        if self.if_find:
            return None
        if len(self.nodes) > index:
            print(self.nodes[index])
            if self.nodes[index].data == data:
                self.if_find = True
                return self.nodes[index], index
        else:
            return None
        result1 = self._dfs_get_node(data, index * 2)
        result2 = self._dfs_get_node(data, index * 2 + 1)
        if result1:
            return result1
        return result2
    
tree = Tree()

for i in range(1, 8):
    tree.add_node(Node(i))

print(tree.get_node(5))



            
