def get_ai(i):
    if i == 1:
        return -4
    if i == 2:
        return 3
    return get_ai(i - 1) ** 2 + 2 * get_ai(i - 2) - i


n = int(input("n="))
b = int(input("b="))
c = int(input("c="))
A = [get_ai(i + 1) for i in range(n)]
Af = [x for x in A if b < x <= c]
s = 0
for el in Af:
    s += el
f = s / len(Af)
print(f)
