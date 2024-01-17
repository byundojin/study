import student

student1 = student.StudnetBuilder().set_name("도진").set_number(2105).set_major("back-end").build()
student1.self_introduce()

student2 = student.StudnetBuilder().set_name("승권").set_number(2109).set_major("game-dev").build()
student2.self_introduce()

student3 = student.StudnetBuilder().set_name("철중").set_number(2104).build()
student3.self_introduce()

student4 = student.StudnetBuilder().set_name("도현").set_number(2202).set_major("그림쟁이").build()
student4.self_introduce()