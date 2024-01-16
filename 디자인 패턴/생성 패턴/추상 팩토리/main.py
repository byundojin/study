import factory
print("chair 동작")
print("==============")

print("korean")
print()
k_chair1 = factory.KoreanFactory.createChair()
print("chair 1 동작")
print("origin :", k_chair1.origin)
k_chair1.sit()
print()

k_chair2 = factory.KoreanFactory.createChair()
print("chair 2 동작")
print("origin :", k_chair2.origin)
k_chair2.sit()
print()

print("--------------------")
print("chinese")
print()

c_chair1 = factory.ChineseFactory.createChair()
print("chair 1 동작")
print("origin :", c_chair1.origin)
c_chair1.sit()
print()

c_chair2 = factory.ChineseFactory.createChair(is_fake=False)
print("chair 2 동작")
print("origin :", c_chair2.origin)
c_chair2.sit()
print()

print("================================================")
print()

print("table 동작")
print("==============")

print("korean")
print()

k_table1 = factory.KoreanFactory.createTable()
print("origin :", k_table1.origin)
k_table1.put()
print()

k_table2 = factory.KoreanFactory.createTable()
print("origin :", k_table2.origin)
k_table2.put()
print()

print("--------------------")
print("chinese")
print()

c_table1 = factory.ChineseFactory.createTable()
print("origin :", c_table1.origin)
c_table1.put()
print()

c_table2 = factory.ChineseFactory.createTable(is_fake=False)
print("origin :", c_table2.origin)
c_table2.put()