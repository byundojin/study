class Studnet():
    def __init__(self, name, number, major) -> None:
        self.name = name
        self.number = number
        self.major = major

    def self_introduce(self):
        print("------------")
        print("이름 :", self.name)
        print("번호 :", self.number)
        print("전공 :", self.major)
        print("------------")

class StudnetBuilder():
    name:str
    number:int
    major:str|None = None

    def set_name(self, name:str):
        self.name = name
        return self
    
    def set_number(self, number:int):
        self.number = number
        return self
    
    def set_major(self, major:str):
        if major in ["game-dev", "back-end"]:
            self.major = major
            return self
        else:
            raise "major is invaild"

    def build(self) -> Studnet:
        return Studnet(self.name, self.number, self.major)