def loop123():
    yield 1
    yield 2
    yield 3

for i in loop123():
    print(i)