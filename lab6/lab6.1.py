n = int(input("n=")
a = [
    int(input("a="))
    for i in range(n)
]
count = 0
for i in range(n - 2):
    a_1 = a[i]
a_2 = a[i + 1]
a_3 = a[i + 2]
if (a_1 + a_3) / 2 == a_2:
    count += 1
print(count)
