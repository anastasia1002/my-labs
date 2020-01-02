a = [
    [5,2,0],
    [1,1,5],
    [7,2,0]
]
for i in range(3):
    m = []
    for j in range(3):
        m.append(a[j][i])
    print(sum(m))

