n=int(input("n="))
v_1 = [float(input("кординати вектора V1:")) for x in range(n)]
v_2 = [float(input("кординати вектора V2:")) for y in range(n)]
sum = map(lambda x, y: x + y, v_1, v_2)
print(list(sum))
