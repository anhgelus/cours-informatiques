from math import sqrt

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

class Unreal: # Ici je définis une classe pour gérer les nombres complexes (a+ib), ça complique beaucoup le script pour les néophytes mais j'avais la flemme de faire autrement
    real = .0
    imaginary = .0
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary
    def __str__(self):
        return str(self.real)+" i*"+str(self.imaginary)
    def conjugate(self):
        return Unreal(self.real,-self.imaginary)

delta = b**2-4*a*c
if delta == 0:
    print("Racine :",-b/(2*a))
elif delta > 0:
    print("Racine 1 :",(-b-sqrt(delta))/(2*a))
    print("Racine 2 :",(-b+sqrt(delta))/(2*a))
else:
    num = Unreal(-b/(2*a),((delta**2)**0.25)/(2*a))
    print("Racine 1 :",num.conjugate())
    print("Racine 2 :",num)
