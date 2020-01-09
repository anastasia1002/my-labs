## Task1
__Визначити добуток додатних парних елементів матриці.__
```py
n = int(input("n="))
m = int(input("m="))

matr = [[int(input("{0},{1}".format(i,j)))for j in range(m)]for i in range (n)]
dob = 1
for i in range(n):
    for j in range(m):
        if matr[i][j]>0 and matr[i][j] % 2 == 0:
            dob *= matr[i][j]
print(dob)
```

## Task 2
__Побудувати прямокутну матрицю А, елементи якої задаються формулою:aij = jcos(i**2+n)Обчислити суму елементів матриці А, сума індексів яких непарна.__
```py
from math import cos


def formula(i, j, n):
    f = j * cos(i ** 2 + n)
    return f


z = int(input("кількість рядків: "))
m = int(input("кшлькість стовпців: "))
n = int(input("n: "))
a = [[formula(i, j, n) for i in range(z)] for j in range(m)]
for el in a:
    print(el)
```

## Task 3
__Дано матрицю A і число a є R . Знайти добуток числа на матрицю.__
```py
b = int(input("b="))
n = int(input())
m = int(input())
f = [[int(input("A[{0}][{1}]:".format(i, j))) for i in range(1, n + 1)] for j in range(1, m + 1)]
for i in range(n):
    for j in range(m):
        f[i][j] *= b
print(f)
```

## Task 4 
__Розмістити елементи парних стовпців у порядку спадання.__
```py
n = int(input("Кількість рядків та стовпців: "))
A = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(1, n + 1)] for i in range(1, n + 1)]
matrix = [[0] * n for i in range(n)]
for j in range(n):
    for i in range(n):
        matrix[j][i] = A[i][j]
for el in range(0,n,2):
    matrix[el].sort(reverse=True)
c = [[0] * n for i in range(n)]
for j in range(n):
    for i in range(n):
        A[j][i] = matrix[i][j]

for i in A:
    print(i)
```

## Task 5
__Дана цілочислова матриця 8x8. Знайти суму елементів в тих рядках, які містять хоча б один від’ємний елемент.__
```py
a = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(2)] for i in range(2)]

string = 0
for el in a:
    count = 0
    m = list(filter(lambda x: x < 0, el))
    if len(m) > 0:
        string += 1
        count = sum(el)
        print("Сума чисел стовпця № {0}: {1}".format(string, count))
        continue
    else:
        string += 1
        continue
```
## Task6
__Дана цілочислова матриця 88. Знайти такі k, що k-й рядок матриці співпадає з k-м стовбцем.__
```py
a = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(2)] for i in range(2)]
for i in range(2):
    for j in range(2):
        if i==j:
            print(a[i][j])
```