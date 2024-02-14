def a(func):
    def _a():
        print("a!!!")
    return _a

def a1(func):
    def _a():
        print("a!!!")
        func()
    return _a

def a2(func):
    def _a():
        print("a!!!")
        return func
    return _a()

@a2
def b():
    print("b!!!")

b()

