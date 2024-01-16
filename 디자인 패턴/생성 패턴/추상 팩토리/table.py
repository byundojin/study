class AbstractTable:
    def __init__(self) -> None:
        self.origin:str
    
    def put(self):
        pass

class KoreanTable(AbstractTable):
    def __init__(self, origin) -> None:
        super().__init__()
        self.origin = origin

    def put(self):
        print("put")

class ChineseTable(AbstractTable):
    def __init__(self, origin, is_fake) -> None:
        super().__init__()
        self.origin = origin
        self.is_fake = is_fake

    def put(self):
        if self.is_fake:
            print("poo")
        else:
            print("put")