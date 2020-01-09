## Task1
__Дано натуральне число n і дійсне число x.Знайти cosx+cos**2...__
```py
import math
n = int(input("натуральне число"))
x = float(input("дійсне число"))
sum = 0
m = 1
i = math.cos(x)
while i <= math.cos(x) ** n:
    sum +=  math.cos(x) ** m
    m+=1
else:
    sum = math.cos(x) ** n
print(sum)
```
## Task2
__Дано два натуральних числа x і y. Знайти число, яке містить найбільшу кількість нулів.__
```py
x = input("x=")
y = input("y=")
x_zeros = 0
y_zeros = 0

for i in x:
    if i == "0":
        x_zeros += 1
for i in y:
    if i == "0":
        y_zeros += 1
if x_zeros > y_zeros:
    print(x)
else:
    print(y)
```
## Task3
__Перевірити справедливість рівності при заданій точності e:x=2(sinx-sin2x/2...)__
```py
import math
x = float(input("Введіть число:"))
eps = float(input("Epsilont:"))
sum = 0
k = 1
q = 1
while math.fabs(math.sin(k * x) / k) > eps:
    sum += q * math.sin(k * x) / k
    k += 1
    q *= -1
print (sum, x, eps)
```
## Task4
__Нехай x_0=-1,x_1=5.Знайти x_i=x_i-1(1+x_i-2) де і=2,3...__
```py 
n = int(input("n = "))
i = 2
x0 = -1
x1 = 5
while i <= n:
    xi = x0*(1+x1)
    x0 = xi
    i += 1


print("x(i) = {0}".format(xi))
```

