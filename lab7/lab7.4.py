n = int(input("Кількість рядків та стовпців: "))
A = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(1, n + 1)] for i in range(1, n + 1)]
matrix = [[0] * n for i in range(n)]
for j in range(n):
    for i in range(n):
        matrix[j][i] = A[i][j]
for el in range(0,n,2):
    matrix[el].sort(reverse=True)
c = [[0] * n for i in range(n)]
for j in range(n):
    for i in range(n):
        A[j][i] = matrix[i][j]

for i in A:
    print(i)

