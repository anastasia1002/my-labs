n=int(input("n="))
v_1 = [float(input("кординати вектора V1:")) for el in range(n)]
v_2 = [float(input("кординати вектора V2:")) for el in range(n)]
sum1 = map(lambda x, y: x + y, v_1, v_2)
if sum(sum1)==0:
    print("perpendicular")
else:
    print("False")
print(sum)

v_1 = [float(input("кординати вектора V1:")) for el in range(3)]
v_2 = [float(input("кординати вектора V2:")) for el in range(3)]
dob = (sum(list(map(lambda x, y: x * y, v_1, v_2)))
print(dob)
