def Produit(a, b, total=0):
    if b == 0:
        return total
    return Produit(a, b - 1, total + a)


print(Produit(2, 3))
print(Produit(8, 9))
