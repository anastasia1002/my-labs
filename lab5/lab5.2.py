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