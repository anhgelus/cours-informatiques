a = int(input("valeur de a : "))

i = 1
val = 1

while val < a:
    k = 1
    v = 0
    while k <= i:
        v += 1/k
        k += 1
    val = v
    i += 1
print("plus petite valeur de n :",i)
