import math
class TCircle:
    def __init__(self,r):
        self.r=r
    def S(self):
        return self.r * math.pi
    def C(self):
        return 2*math.pi*self.r
    def __add__(self, other):
        return TCircle(other.r+self.r)
    def __sub__(self, other):
        return TCircle(self.r - other.r)
    def __mul__(self, other):
        return TCircle(other * self.r)
    def __str__(self):
        return "circle: {0}".format(self.r)


class TCylinder(TCircle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h=h
    def V(self):
        return super().S()**2 * self.h
    def Sb(self):
        return super().S() * 2 * self.h
    def So(self):
        return 2 * math.pi * self.r **2
    def Sp(self):
        return self.Sb() + self.So()
    def __add__(self, other):
        return TCylinder(other.r + self.r , other.h + self.h)
    def __sub__(self, other):
        return TCylinder(self.r - other.r , self.h - other.h)
    def __mul__(self, other):
        return TCylinder(other * self.r , other * self.h)
    def __str__(self):
        return ("Cylinder:{0},{1}".format(self.r,self.h))



x1=TCircle(3)
print(x1)
print("S=" , x1.S())
print("C=" , x1.C())
x = TCylinder( 2, 3)
print(x)
print("V=",x.V())
print("Sb=",x.Sb())
print("So=", x.So())
print("Sp=", x.Sp( ))
