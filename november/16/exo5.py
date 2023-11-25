def diviseurs(a):
    list = []
    for i in range (1,int(a/2)+1):
        if a % i == 0:
            list.append(i)
    print(list)
    return list

def pgcdParDiviseurs(a,b):
    if a < b:
        raise ValueError('a est plus petit que b')
    dA = diviseurs(a)
    dA.reverse()
    dB = diviseurs(b)
    dB.reverse()
    i,j = 0,0
    v = dA[i]
    u = dB[j]
    while u != v:
        print(u,v)
        if u > v:
            i+=1
        if v > u :
            j+=1
        v = dA[i]
        u = dA[j]
    print("Le plus grand diviseur commun de",a,"et",b,"est :",v,"\n(version diviseurs)")

def pgcdParDifferences(a,b):
    if a < b:
        raise ValueError('a est plus petit que b')
    i = a
    j = b
    while i-j != 0:
        i,j = j,i-j
    print("Le plus grand diviseur commun de",a,"et",b,"est :",i,"\n(version différences)")

def pgcdParEuclide(a,b):
    i = a
    j = b
    while i%j != 0:
        i,j = j,i%j
    print("Le plus grand diviseur commun de",a,"et",b,"est :",j,"\n(version euclide)")

pgcdParDiviseurs(63,42)
pgcdParDifferences(63,42)
pgcdParEuclide(561,357)

