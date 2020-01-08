## Task1
__суму векторів (тобто новий список, який складається з елементів, які є сумою відповідних елементів заданих списків)__
```py
n=int(input("n="))
v_1 = [float(input("кординати вектора V1:")) for x in range(n)]
v_2 = [float(input("кординати вектора V2:")) for y in range(n)]
sum = map(lambda x, y: x + y, v_1, v_2)
print(list(sum))
```

## Task2
__скалярний добуток векторів;__
```py
n=int(input("n="))
v_1 = [float(input('кординати вектора V1: ')) for x in range(n)]
v_2 = [float(input('кординати вектора V2: ')) for x in range(n)]
scalar_dob = sum(list(map(lambda x, y: x * y, v_1, v_2)))
print(scalar_dob)
```

## Task3
__з’ясувати, чи є вектори перпендикулярними (скалярний добуток дорівнює 0).__
```py
n=int(input("n="))
v_1 = [float(input("кординати вектора V1:")) for el in range(n)]
v_2 = [float(input("кординати вектора V2:")) for el in range(n)]
sum1 = map(lambda x, y: x + y, v_1, v_2)
if sum(sum1)==0:
    print("perpendicular")
else:
    print("False")
print(sum)

v_1 = [float(input("кординати вектора V1:")) for el in range(3)]
v_2 = [float(input("кординати вектора V2:")) for el in range(3)]
dob = (sum(list(map(lambda x, y: x * y, v_1, v_2)))
print(dob)
```

## Task4
__з’ясувати, чи є вектори рівними;__
```py
n=int(input("n="))
v_1 = [float(input('кординати вектора V1: ')) for x in range(n)]
v_2 = [float(input('кординати вектора V2: ')) for x in range(n)]
identical=map(lambda x,y : x==y,v_1,v_2)
#print(list(identical))
if v_1==v_2 :
    print("true")
else:
    print("false")
```

## Task5
__Дано масив (список) елементів цілого типу. Знайти суму елементів;__
```py
from functools import reduce
n=int(input("n="))
a=[int(input("a="))for i in range(n)]
sum= reduce((lambda x,y: x+y),a)
print(sum)
```

## Task6
__Дано масив (список) елементів цілого типу. Знайти добуток елементів;__
```py
from functools import reduce
n=int(input("n="))
a=[int(input("a="))for i in range(n)]
dob=reduce((lambda x,y: x*y),a)
print(dob)
```

## Task7
__Дано масив (список) елементів цілого типу. Знайти суму додатних;__
```py
from functools import reduce
n=int(input("n="))
a=[int(input("a="))for i in range(n)]
positive_el=filter(lambda x: x>0,a)
sum=reduce((lambda x,sum: x+sum ),positive_el)
print(sum)
```

## Task8
__Дано масив (список) елементів цілого типу. Знайти суму елементів з номерами кратними 3;__
```py
from functools import reduce
n=int(input("n="))
a=[int(input("a="))for i in range(n)]
positive_el=filter(lambda x: x//3,a)
sum=reduce((lambda x,sum: x+sum ),positive_el)
print(sum)
``` 