n = int(input("enter the number of vectors"))
x_list = [float(input("vector coordinates x")) for x in range(n)]
y_list = [float(input("vector coordinates y")) for y in range(n)]
perpendicular = list(map(lambda x, y: x * y, x_list, y_list))
# print("perpendicularnist vectoriv x and y ")
s = 0

for el in perpendicular:
    s += el

if s == 0:
    print("perpendicularnist vectoriv x and y")
else:
    print("not")
