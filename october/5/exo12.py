n = int(input("Valeur de n : "))
if n < 3 :
    n = int(input("Valeur de n (impossible d'obtenir une somme sous 3) : "))
if n > 24 :
    n = int(input("Valeur de n (impossible d'obtenir une somme au dessus de 24) : "))

def triplet(v1,v2,v3):
    return f'({v1},{v2},{v3})'

def generateDice(max):
    arr = []
    n = 1
    while n <= max:
        arr.append(n)
        n+=1
    return arr

triples = []
d1 = generateDice(6)
d2 = generateDice(8)
d3 = generateDice(10)

n1 = 0
while n1 < len(d1):
    dn1 = d1[n1]
    n2 = 0
    if dn1 >= n: break
    while n2 < len(d2):
        dn2 = d2[n2]
        n3 = 0
        if dn1 + dn2 >= n : break
        while n3 < len(d3):
            dn3 = d3[n3]
            if dn1+dn2+dn3 == n : 
                triples.append(triplet(dn1,dn2,dn3))
                break
            n3 += 1
        n2 += 1
    n1 += 1
print(triples, len(triples))
