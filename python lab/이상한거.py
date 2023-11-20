# 이게 정상
a = (2, 3)
b = [a, 4]
print(b)
# [(2, 3), 4]

# ???????왓
a = (2, 3)
b = [*a, 4]
print(b)
# [2, 3, 4]

# 이것도 됨
a = [1,2,3]
b = [*a[1:],4]
print(b)
# [2, 3, 4]

a = [1,2,3]
print(a)
print(*a)
print(type(a))
# print(type(*a)) ? 타입 에러뜸

print((1,2,3))

a = [1,2,3]
def f(*a):
    print(a)
    print(*a[0])
f(a)
