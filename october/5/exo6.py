n = int(input("nombre : "))

i = 1 
s = 0
while i < n:
    if n % i == 0:
        s += i
    i += 1
if s == 1:
    print(n,"est premier")
else:
    print("somme des diviseurs stricts :",s)
