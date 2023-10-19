n = int(input("Valeur de n : "))
while n <= 0:
    n = int(input("Valeur de n (non négative ou nulle) : "))

s0 = 0 # somme impaire
s1 = 0 # somme pair
i = 0

while i < n:
    t  = int(input("Valeur : "))
    while t <= 0:
        t  = int(input("Valeur (non négative ou nulle) : "))
    if t % 2 == 0:
        s1 += t
    else:
        s0 += t
    i+=1

if s1 == s0:
    print("la somme des nombres pairs est égale à la somme des nombres impairs.")
else:
    print("la somme des nombres pairs n'est pas égale à la somme des nombres impairs.")

