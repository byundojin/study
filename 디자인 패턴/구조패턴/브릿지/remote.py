from tv import AbstractTV

class AbstractRetote():
    def __init__(self, tv) -> None:
        self.tv:AbstractTV = tv
    def volume_up(self):
        print("volume up")

class KoreanRetote(AbstractRetote):
    pass

class ChineseRemote(AbstractRetote):
    def volume_up(self):
        print("volume up")
        self.tv.turn_off()
