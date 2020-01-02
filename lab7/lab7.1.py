n = int(input("n="))
m = int(input("m="))

matr = [[int(input("{0},{1}".format(i,j)))for j in range(m)]for i in range (n)]
dob = 1
for i in range(n):
    for j in range(m):
        if matr[i][j]>0 and matr[i][j] % 2 == 0:
            dob *= matr[i][j]
print(dob)

