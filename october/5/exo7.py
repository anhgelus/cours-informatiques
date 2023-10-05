u = int(input("nombre : "))

n = 1
while n <= u:
    i = 1 
    s = 0
    while i < n:
        if n % i == 0:
            s += i
        i += 1
    if n == s :
        print(n,"est parfait")
    n+=1
