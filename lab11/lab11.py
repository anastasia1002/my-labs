import math
class TCircle:
    def __init__(self,r,x,y):
        self.r=r
        self.x=x
        self.y=y
    def S(self):
        return self.r * math.pi
    def R(self):
        return  self.x<= self.r and self.y<=self.r

    def __add__(self, other):
        return TCircle(other.r+self.r)
    def __sub__(self, other):
        return TCircle(self.r - other.r)
    def __mul__(self, other):
        return TCircle(other * self.r)
    def __str__(self):
        return str(self.r)

x =TCircle(2,5,4)
print("S=",x.S())
print("r_xy",x.R())
