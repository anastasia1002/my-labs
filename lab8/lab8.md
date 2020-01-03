## Task1
__Дано дійсні числа x,y,z . Обчислити:u= max(x,z) + max(x+y,xy)/max**2(x+y,xy)__
```py
x=float(input("x="))
y=float(input("y="))
z=float(input("z="))
def get_max(x,z):
    if x>z:
        return x
    else:
        return y
sum=x+y
dob=x*y
def get_max(sum,dob):
    if sum>dob:
        return sum
    else:
        return dob
u=max(x,z)+max(x+y,x*y)/max(x+y,x*y)**2
print(u)
```
## Task2
__Два трикутники задано координатами вершин. Використовуючи підпрограму визначення належності точки внутрішності трикутника, з’ясувати, чи лежить один з трикутників у середині іншого.__
```py
x_a=int(input("x_a="))
y_a=int(input("y_a="))
x_b=int(input("x_b="))
y_b=int(input("y_b="))
x_c=int(input("x_c="))
y_c=int(input("y_c="))

x_n=int(input("x_n="))
y_n=int(input("y_n="))
x_m=int(input("x_m="))
y_m=int(input("y_m="))
x_k=int(input("x_k="))
y_k=int(input("y_k="))

def triangle(x1,y1,x2,y2,x3,y3,a1,b1,a2,b2,a3,b3):
    if x1<a1 and y1<b1 and x2<a2 and y2<b2 and x3<a3 and y3<b3:
        return ("yes,these points belong to the triangle")
    else:
        return ("noo,it's false")
print(triangle(x_a,y_a,x_b,y_b,x_c,y_c,x_n,y_n,x_m,y_m,x_k,y_k))
```
## Task3
__Нехай x0=0, x1=x2=9, xi=xi-1 +xi-2 +xi-3. Визначити xn__
```py
i = int(input("i="))


def recurs(i):
    if i == 0:
        return 0
    elif i == 1 or i == 2:
        return 9
    else:
        return recurs(i - 1) + recurs(i - 2) + recurs(i - 3) \

print("i({0})={1}".format(i, recurs(i)))
```
