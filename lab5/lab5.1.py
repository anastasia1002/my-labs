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