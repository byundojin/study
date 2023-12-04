from functools import reduce

a = reduce(lambda x, y: x + y, [1, 2, 3, 4])

a = reduce(lambda x, y: x + y, [1, 1, 1], 10)

print(a)

global