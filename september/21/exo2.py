a = int(input("Valeur de a : "))
b = int(input("Valeur de b : "))
c = int(input("Valeur de c : "))

if a == b+c:
    print("oui")
elif b == a+c:
    print("oui")
elif c == a+b:
    print("oui")
else:
    print("non")
