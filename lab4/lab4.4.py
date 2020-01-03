x=float(input("ведіть x: "))
def fun(x):
    a = 2*x ** 2 - x - 3
    if a==0:
        return 1
    elif a<0:
        return 2
    else :
        return 0
print (fun(x))