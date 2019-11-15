def Reversed(a):
    a[:] = a[::-1]


a = list(range(50))
Reversed(a)
print(a)
