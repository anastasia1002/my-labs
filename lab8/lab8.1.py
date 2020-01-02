x=float(input("x="))
y=float(input("y="))
z=float(input("z="))
print(max(x,y,z))
print(max(x+y,x*y))
print(max(x+y,x*y))
u=max(x,z)+max(x+y,x*y)/max(x+y,x*y)**2
print(u)