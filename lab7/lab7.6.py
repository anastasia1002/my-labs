a = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(2)] for i in range(2)]
for i in range(2):
    for j in range(2):
        if i==j:
            print(a[i][j])