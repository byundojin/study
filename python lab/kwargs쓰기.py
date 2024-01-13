def f(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)

f(key=123,adf=123,dafdd=123)