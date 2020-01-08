from functools import reduce
n=int(input("n="))
a=[int(input("a="))for i in range(n)]
sum= reduce((lambda x,y: x+y),a)
print(sum)