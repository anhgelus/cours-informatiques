var1 = input("Nombre 1\n")
var2 = input("Nombre 2\n")

print("Avant échange","var1 =",var1,"; var2 =",var2)
var1, var2 = var2, var1
print("Après échange","var1 =",var1,"; var2 =",var2)
