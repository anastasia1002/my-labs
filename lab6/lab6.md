## Task1
__Дано одновимірний масив, який містить дійсних чисел. З’ясувати, скільки серед елементів цієї послідовності є пар з трьох елементів, які слідують підряд і утворюють арифметичну прогресію.__
```py
n = int(input("n=")
a = [
    int(input("a="))
    for i in range(n)
]
count = 0
for i in range(n - 2):
    a_1 = a[i]
a_2 = a[i + 1]
a_3 = a[i + 2]
if (a_1 + a_3) / 2 == a_2:
    count += 1
print(count)
```
## Task2
__Елементи масиву A=(ai)(i=1,2..n) задаються так :a1=-4, a2=3, ai=ai-1**2+2ai=2-i (i=3,4..n).Знайти середнє арифметичне всіх елементів масиву, які потрапляють у проміжок (b,c]__
```py
def get_ai(i):
    if i == 1:
        return -4
    if i == 2:
        return 3
    return get_ai(i - 1) ** 2 + 2 * get_ai(i - 2) - i


n = int(input("n="))
b = int(input("b="))
c = int(input("c="))
A = [get_ai(i + 1) for i in range(n)]
Af = [x for x in A if b < x <= c]
s = 0
for el in Af:
    s += el
f = s / len(Af)
print(f)
```
## Task3
__Дано два вектори x,y є R .З’ясувати, чи є вони перпендикулярними.__
```py
from functools import reduce
n = int(input("enter the number of vectors"))
x_list = [float(input("vector coordinates x")) for x in range(n)]
y_list = [float(input("vector coordinates y")) for y in range(n)]
perpendicular = reduce((lambda suma, x: suma + x), map(lambda x, y: x * y, x_list, y_list))
# print("perpendicularnist vectoriv x and y ")
s = 0


if perpendicular == 0:
    print("perpendicularnist vectoriv x and y")
else:
    print("not")
```
## Task4
__Перетворити масив таким чином, щоб спочатку розміщувались всі елементи, які мають непарні індекси, а потім з парними індексами.__
```py
n = int(input("n="))
a = [
    int(input("a="))
    for i in range(n)
]

r = [a[i] for i in range(0, n, 2)] + [a[i] for i in range(1, n, 2)]

print(r)
```

