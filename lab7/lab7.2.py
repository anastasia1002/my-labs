from math import cos


def formula(i, j, n):
    f = j * cos(i ** 2 + n)
    return f


z = int(input("к-ть рядків: "))
m = int(input("к-ть стовпців: "))
n = int(input("n: "))
a = [[formula(i, j, n) for i in range(z)] for j in range(m)]
for el in a:
    print(el)
