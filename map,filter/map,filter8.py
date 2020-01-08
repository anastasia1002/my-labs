from functools import reduce
n=int(input("n="))
a=[int(input("a="))for i in range(n)]
positive_el=filter(lambda x: x//3,a)
sum=reduce((lambda x,sum: x+sum ),positive_el)
print(sum)
