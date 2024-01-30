class StudentInterface():
    def self_introduce(self):
        pass

class Student(StudentInterface):
    def __init__(self, num, name) -> None:
        self.num = num
        self.name = name

    def self_introduce(self):
        print(self.num, "-", self.name)

class StudentProxy(StudentInterface):
    def __init__(self, student) -> None:
        self.student:Student = student

    def self_introduce(self):
        if (1 <= self.student.num // 1000 <= 3 and
            1 <= self.student.num % 1000 // 100 <= 4 and
            1 <= self.student.num % 100 <= 20):
            self.student.self_introduce()
        else:
            print("존재 할 수 없는 번호")