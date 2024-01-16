class Table:
    def __init__(self, num) -> None:
        self.num = num

    def check(self):
        pass

class KoreanTable(Table):
    def __init__(self, num) -> None:
        super().__init__(num)

    def check(self):
        print("Table number :", self.num)

class ChineseTable(Table):
    def __init__(self, num, is_fake) -> None:
        super().__init__(num)
        self.is_fake = is_fake

    def check(self):
        print("Table number :", self.num)
        if self.is_fake:
            print("fuck chinese")
        else:
            print("oh lucky")