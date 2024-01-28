class SenderrInterface():
    def send(self):
        pass

class Sender(SenderrInterface):
    def __init__(self, name) -> None:
        self.name = name

    def send(self):
        print("전송자 :", self.name)

class SenderDecorator(SenderrInterface):
    def __init__(self, sender) -> None:
        self.sender:Sender = sender

    def send(self):
        self.send()

class DiscordSenderDecorator(SenderDecorator):
    def __init__(self, sender) -> None:
        self.sender:Sender = sender

    def send(self):
        self.sender.send()
        print("discord에 전송")

class EmailSenderDecorator(SenderDecorator):
    def __init__(self, sender) -> None:
        self.sender:Sender = sender

    def send(self):
        self.sender.send()
        print("Email에 전송")

    