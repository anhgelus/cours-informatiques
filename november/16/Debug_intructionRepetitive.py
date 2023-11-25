n = 0
while n <= 0:
    n = int(input("n = ? "))
i = 0
b = True
c = 0
while i < n:
    p = 0
    if i != 0:
        p = c
    c = int(input())
    if i != 0 and (p > c or not b) :
        b = False
    i += 1
if b:
    print("Les", n, "valeurs","sont triées de façon croissante.")
else :
    print("Les", n, "valeurs","ne sont pas triées de façon croissante.")
