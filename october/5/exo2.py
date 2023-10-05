def func(x):
    return x**3-3*x**2+1

eps = float(input("Précision : "))

a = 2.0
b = 3.0
m = (b-a)/2

while abs(b-a) > eps:
    print(a,b,m)
    if m == 0:
        print("La solution exacte est :",m)
        break
    elif func(m) > 0:
        b = m
    else:
        a = m
    m = (b-a)/2 
print(m,"est environ égal à 0 à",eps,"près.")
