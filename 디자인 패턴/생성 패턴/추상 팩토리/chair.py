class AbstractChair:
    def __init__(self) -> None:
        self.origin:str
    
    def sit(self):
        pass

class KoreanChair(AbstractChair):
    def __init__(self, origin) -> None:
        super().__init__()
        self.origin = origin

    def sit(self):
        print("sit")

class ChineseChair(AbstractChair):
    def __init__(self, origin, is_fake) -> None:
        super().__init__()
        self.origin = origin
        self.is_fake = is_fake

    def sit(self):
        if self.is_fake:
            print("shit")
        else:
            print("sit")