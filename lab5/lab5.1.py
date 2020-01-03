import math
n = int(input("натуральне число"))
x = float(input("дійсне число"))
sum = 0
i = math.cos(x)
while i <= math.cos(x) ** n:
    sum = i + math.cos(x)
else:
    sum = math.cos(x) ** n
print(sum)