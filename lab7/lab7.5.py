a = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(2)] for i in range(2)]
# sum = 0
string = 0
for el in a:
    count = 0
    m = list(filter(lambda x: x < 0, el))
    if len(m) > 0:
        string += 1
        count = sum(el)
        print("Сума чисел стовпця № {0}: {1}".format(string, count))
        continue
    else:
        string += 1
        continue
