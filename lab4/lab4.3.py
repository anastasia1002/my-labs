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