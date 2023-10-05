from math import sqrt

# Ce programme calcule les solutions
#  d'une équation du second degré
a = int(input("Donner le parametre a : "))
b = int(input("Donner le parametre b : "))
c = int(input("Donner le parametre c : "))
d = b*b - 4*a*c
print("la valeur de delta est", d)
# le cas ou il y a deux solutions reelles
if (d > 0):
    print("Il y a deux racines reelles distinctes : x1 =", 
    -b + sqrt(d)/2*a," et x2 = ",  -b - sqrt(d)/2*a)
# le cas ou une seule solution reelle
elif (d == 0):
    print("Il y a une unique racine reelle : x=", -b/2*a)
# le cas ou aucune solution reelle
else:
    print("Il y a deux racines complexes distinctes : z1 =", 
    -b/2*a,"+", sqrt(-d),"i", " et z2 = ",
    -b/2*a, "-", sqrt(-d),"i")
