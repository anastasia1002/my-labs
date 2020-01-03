## Task1
__Обчислити площу та периметр прямокутника, довжини сторін якого задаються.__
```py
x1=int(input("x1="))
x2=int(input("x2="))
x3=int(input("x3="))
y1=int(input("y1="))
y2=int(input("y2="))
y3=int(input("y3="))
print(x1, x2,x3, y1, y2, y3)
a=((x3-x2)**2+(y3-y2)**2)**1/2
b=((x2-x1)**2+(y2-y1)**2)**1/2
c=((x3-x1)**2+(y3-y1)**2)**1/2
print(a,b,c)
P=a+b+c
print(P)
p=a+b+c//2
S=1/2*(p*(p-a)*(p-b)*(p-c))
print(S)
```

## Task2
__Дано три дійсних числа: a,b,c__

__Знайти min (a,b)+(min(b,c))**2__
```py
a=float(input("Ведіть a:"))
b=float(input("Ведіть b:"))
c=float(input("Ведіть c:"))
print (min( a,b) )
print (min(b,c) )
s=min( a,b)+min(b,c)**2
print(s)
```

## Task3
__Трикутник задається координатами своїх вершин на площині:A(x1,y1),B(x2,y2),C(x3,y3). Знайти периметр трикутника.__
```py
import math
x1 = float(input("x1="))
x2 = float(input("x2="))
y1 = float(input("y1="))
y2 = float(input("y2="))
z1 = float(input("z1="))
z2 = float(input("z2="))
a = math.sqrt((y1-x1)**2+(y2-x2)**2)
b = math.sqrt((z1 - y1)**2+(z2-y2)**2)
c = math.sqrt((z1-x1)**2+(z2-x2)**2)
p=a+b+c
print(p)
```

## Task4
__y=1,якщо 2x**2-x-3=0__
__y=2, якщо 2x**2-x-3>0__
__y=0, якщо 2x**2-x-3<0__
```py
x=float(input("ведіть x: "))
def fun(x):
    a = 2*x ** 2 - x - 3
    if a==0:
        return 1
    elif a<0:
        return 2
    else :
        return 0
print (fun(x))
```