import math
import random 
n = int(input("Nombre d'itérations : "))
while n <= 0:
    n = int(input("Nombre d'itérations (strictement positif) : "))

nu = 0
i = 0
while i < n:
    c1 = random.uniform(-1,1)
    c2 = random.uniform(-1,1)
    if math.sqrt(c1**2 + c2**2) < 1:
        nu += 1
    i+=1
print(4*nu/n)
