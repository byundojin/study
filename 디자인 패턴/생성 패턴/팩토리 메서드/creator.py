import table
from abc import ABC, abstractmethod
class TableCreator(ABC):
    num = 0
    @abstractmethod
    def createTable(self) -> table.Table:
        pass

    def review(self):
        t = self.createTable()
        t.check()

class KoreanTableCreator(TableCreator):
    def createTable(self) -> table.KoreanTable:
        self.num += 1
        return table.KoreanTable(self.num)
    
class ChineseTableCreator(TableCreator):
    def createTable(self, is_fake=True) -> table.ChineseTable:
        self.num += 1
        return table.ChineseTable(self.num, is_fake)
    