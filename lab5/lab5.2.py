x = str(input("x="))
y = str(input("y="))
x_zeros = 0
y_zeros = 0
x_zeros += x.count("0")
y_zeros += y.count("0")
if x_zeros > y_zeros:
    print(x)
else:
    print(y)