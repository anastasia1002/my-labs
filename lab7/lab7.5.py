a = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(8)] for i in range(8)]
sum = 0
for i in range(8):
    for j in range(8):
        if a[i][j] < 0:
            sum += a[i][j]
print(sum)
