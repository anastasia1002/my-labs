n = int(input("n="))
a = [
    int(input("a="))
    for i in range(n)
]

r = [a[i] for i in range(0, n, 2)] + [a[i] for i in range(1, n, 2)]

print(r)
