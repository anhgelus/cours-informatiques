from math import sqrt

def serie(n):
    u = 0
    i = 0
    while i != n:
        #        print(u)
        u = sqrt(3*u+4)
        i += 1
#    print(u)
    return u

eps = float(input("écart : "))

n = 0
while serie(n) < 4 - eps:
    n+=1
print("valeur de n :",n)

