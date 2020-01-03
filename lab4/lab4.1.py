import math
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