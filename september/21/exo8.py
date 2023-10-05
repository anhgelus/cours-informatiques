from math import sqrt, acos

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
d = int(input("d : "))
e = int(input("e : "))
f = int(input("f : "))

# Ce n'est pas fini : ça ne différencie pas les cas où les droites sont strictement parallèles ou condondues
class Vector:
    x = .0
    y = .0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def scalar(self, vector):
        return self.x*vector.y + self.y*vector.x

    def angle(self, vector):
        # AB + CD + cos() = scalar
        # cos = scalar - AB - CD
        acos(self.scalar(vector) - self.norme() - vector.norme())

    def norme(self):
        return sqrt(self.x**2+self.y**2)

vec1 = Vector(a,b)
vec2 = Vector(d,e)

angle = vec1.angle(vec2)

if angle != 0:
    """
    ax+by=c
    dx+ey=f
    
    x=(c-by)/a
    d(c-by)/a+ey=f
    y=(af-dc)/(-db+ae)
    """
    y = (a*f-d*c)/(-d*b+a*e)
    x = (c-b*y)/a
    print("x :",x)
    print("y :",y)
else:
    c = e/f
