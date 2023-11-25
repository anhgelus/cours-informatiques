import random

def aleatoireAvecRepetitions(n):
    i = 0
    c = 0
    while i != n -1:
        r = random.randint(0,1)
        c += 1
        if r == 1:
            i += 1
    return random.randint(0,1)

n = -1
while n <= 0:
    n = int(input("n ? "))
print("Nombre de 1 :",n*1000)
m = 0
for i in range(1001):
    m+=aleatoireAvecRepetitions(n)
print("Valeur moyenne : ", m/1000)

