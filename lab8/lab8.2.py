x_a=int(input("x_a="))
y_a=int(input("y_a="))
x_b=int(input("x_b="))
y_b=int(input("y_b="))
x_c=int(input("x_c="))
y_c=int(input("y_c="))

x_n=int(input("x_n="))
y_n=int(input("y_n="))
x_m=int(input("x_m="))
y_m=int(input("y_m="))
x_k=int(input("x_k="))
y_k=int(input("y_k="))

def triangle(x1,y1,x2,y2,x3,y3,a1,b1,a2,b2,a3,b3):
    if x1<a1 and y1<b1 and x2<a2 and y2<b2 and x3<a3 and y3<b3:
        return ("yes,these points belong to the triangle")
    else:
        return ("noo,it's false")
print(triangle(x_a,y_a,x_b,y_b,x_c,y_c,x_n,y_n,x_m,y_m,x_k,y_k))
