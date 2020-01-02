b = int(input("b="))
n = int(input())
m = int(input())
f = [[int(input("A[{0}][{1}]:".format(i, j))) for i in range(1, n + 1)] for j in range(1, m + 1)]
for i in range(n):
    for j in range(m):
        f[i][j] *= b
print(f)
