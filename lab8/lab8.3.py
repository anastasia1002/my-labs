# xi=xi-1(1+xi-2)
i = int(input("i="))


def recurs(i):
    if i == 0:
        return 0
    elif i == 1 or i == 2:
        return 9
    else:
        return recurs(i - 1) + recurs(i - 2) + recurs(i - 3) \

print("i({0})={1}".format(i, recurs(i)))
