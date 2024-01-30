import student

s1 = student.Student(2105, "변도진")
s2 = student.Student(4567, "김철중")

s1 = student.StudentProxy(s1)
s2 = student.StudentProxy(s2)

s1.self_introduce()
s2.self_introduce()