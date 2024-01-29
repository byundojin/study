class StudentFlywate():
    def __init__(self, grade, _class) -> None:
        self.grade = grade
        self._class = _class

class Student():
    def __init__(self, number, name, fw_student) -> None:
        self.fw_student:StudentFlywate = fw_student
        self.number = number
        self.name = name
    
    def self_introduce(self):
        print(f"{self.fw_student.grade}{self.fw_student._class}{str(self.number).zfill(2)}-{self.name}")

class StudentFactory:
    Flywate:dict[str, Student] = {}

    def create(grade, _class, number, name):
        fw_key = f"{grade}_{_class}"
        if fw_key in StudentFactory.Flywate:
            fw = StudentFactory.Flywate[fw_key]
        else:
            fw = StudentFlywate(grade, _class)
            StudentFactory.Flywate[fw_key] = fw
        student = Student(number, name, fw)
        return student
        