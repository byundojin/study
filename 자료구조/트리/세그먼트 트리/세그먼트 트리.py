class Node:
    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f"Node:{self.data}"
    
class SegTree:
    def __init__(self) -> None:
        self.root:Node = None
        self.point:Node = None

