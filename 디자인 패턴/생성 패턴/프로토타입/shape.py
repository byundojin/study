class Copyable():
    def copy(source):
        pass

class Shape(Copyable):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def copy(source):
        return Shape(source.x, source.y)
    
    def print(self):
        print(f"x : {self.x} | y : {self.y}")