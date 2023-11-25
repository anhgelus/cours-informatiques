import math

class Data:
    value = .0
    n = 0
    def __init__(self,v,n):
        self.value = v
        self.n = n
    def __str__(self):
        return f"[{self.n} {self.value}]"

def leibniz(n):
    """
    start = 0
    s = 0
    if lL.n <= n:
        s = lL.value
        start = lL.n+1
    for i in range(start,n+1):
        s+= ((-1)**i)/(2*i+1)
    s *= 4
    lL.n = n
    lL.value = s
    return s
    """
    for k in range(lL.n,n):
        lL.value += ((-1)**k)/(2*k+1)
    lL.n = n
    return 4*lL.value
    """
    s = 0
    for k in range(n+1):
        print(k,s)
        s += ((-1)**k)/(2*k+1)
    return 4*s
    """

def euler(n):
    for k in range(lE.n,n):
        lE.value+=1/(k**2)
    lE.n = n
    return math.sqrt(6*lE.value) 

def inWoon(n):
    if n == 0:
        return 1
    for i in range(lW.n,n):
        lW.value += inWoon(i)
    lW.n = n
    return math.sqrt(1+lW.value**2) 

def woon(n):
    return (2**(n+1))/inWoon(n)

def fracContinues(n):
    i = n
    l = 1
    while i != 0:
        l += 1/i + 1/l
        i -= 1
    return 2+2*l

def test(v,name):
    n = 1
    while math.floor(v(n)*(10**6)) != math.floor(math.pi*(10**6)):
        if n%1000 == 0:
            print(n/1000)
        n+=1
    print(f"{name}:",n)

lL = Data(0,0) 
lE = Data(0,1)
lW = Data(0,0)
lFC = Data(0,0)

#test(leibniz,"Leibniz")
#test(euler,"Euler")
test(woon,"Woon")
test(fracContinues,"Fractions Continues")
