with open("text1.txt") as file:
    a = []
    for line in file:
        if "A" in line:
            a.append(line)
    for index in range(-1, -len(a) - 1, -1):
        print(a[index])

    print(a)
