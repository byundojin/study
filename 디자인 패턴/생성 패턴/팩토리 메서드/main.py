import creator

print("------korean------")

k_creator = creator.KoreanTableCreator()

k_table1 = k_creator.createTable()
k_table1.check()

k_table2 = k_creator.review()

print("------chinese------")

c_creator = creator.ChineseTableCreator()

k_table1 = c_creator.createTable(is_fake=False)
k_table1.check()

k_table2 = c_creator.review()
