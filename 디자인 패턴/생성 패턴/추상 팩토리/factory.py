import chair
import table

class AbstractFactory:
    def createTable(origin) -> table.AbstractTable:
        pass
    def createChair(origin) -> chair.AbstractChair:
        pass

class KoreanFactory(AbstractFactory):
    origin = "korea"
    def createTable():
        return table.KoreanTable(KoreanFactory.origin)
    def createChair():
        return chair.KoreanChair(KoreanFactory.origin)
    
class ChineseFactory(AbstractFactory):
    origin = "chinese"
    def createTable(is_fake=True):
        return table.ChineseTable(ChineseFactory.origin, is_fake)
    def createChair(is_fake=True):
        return chair.ChineseChair(ChineseFactory.origin, is_fake)