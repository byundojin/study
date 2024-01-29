import student

s1 = student.StudentFactory.create(2, 1, 5, "변도진")
s2 = student.StudentFactory.create(2, 1, 4, "김철중")
s3 = student.StudentFactory.create(2, 1, 9, "양승권")
s4 = student.StudentFactory.create(2, 1, 10, "오영기")

s1.self_introduce()
s2.self_introduce()
s3.self_introduce()
s4.self_introduce()