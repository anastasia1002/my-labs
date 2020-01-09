with open("text.txt") as file:
    a=[]
    for el in file:
        a.append(float(el))
    res = []
    for i in a:
        if i > 0:
            res.append(i)
            m = min(res)

    print(m)
