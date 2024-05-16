def fac_rec(n):
    global nbPassageFonction
    nbPassageFonction += 1
    print("n =", n)
    if n < 2:
        return 1
    return n * fac_rec(n - 1)


def fac_it(n):
    if n < 2:
        return 1
    for i in range(2, n + 1):
        n *= i
    return n


nbPassageFonction = 0
i = int(input("i="))
print("Résultat de " + str(i) + "! =", fac_rec(i))
print("Nbr de passage de la fonction :", nbPassageFonction)
print("Résultat de " + str(i) + "! =", fac_it(i), "(en itérative)")
