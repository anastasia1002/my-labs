n = int(input("n = "))
i = 2
x0 = -1
x1 = 5
while i <= n:
    xi = x0*(1+x1)
    x0 = xi
    i += 1


print("x(i) = {0}".format(xi))