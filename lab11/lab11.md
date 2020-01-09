## Task1
__Описати клас, який містять вказані поля і методи. Клас “круг” – TCircle. ПОЛЯ:1. для зберігання радіуса;2. для зберігання центра кола__
__МЕТОДИ : 1.конструктор без параметрів, конструктор з параметрами, конструктор копіювання; 2.введення/виведення даних; 3.визначення площі круга; 4.перевірка належності точки кругу; 5.перевантаження операторів + (додавання радіусів), – (віднімання радіусів), *(множення радіуса на число).__
```py 
import math
class TCircle:
    def __init__(self,r,x,y):
        self.r=r
        self.x=x
        self.y=y
    def S(self):
        return self.r**2 * math.pi
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
```
