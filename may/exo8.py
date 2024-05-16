import time


def FibIt(n):
    if n < 2:
        return 1
    last = 1
    last_second = 1
    for _ in range(2, n + 1):
        last, last_second = last + last_second, last
    return last


def FibRec(n, i=None):
    if i is None:
        i = {1: 1, 0: 1}
    if n < 2:
        return 1
    if n - 2 not in i:
        i[n - 2] = FibRec(n - 2, i)
    if n - 1 not in i:
        i[n - 1] = FibRec(n - 1, i)
    return i[n - 1] + i[n - 2]


p = time.time()
print(FibIt(35))
print(f"Temps passé pour FibIt(35) : {time.time() - p} secondes")
p = time.time()
print(FibRec(35))
print(f"Temps passé pour FibRec(35) : {time.time() - p} secondes")
p = time.time()
print(FibIt(70))
print(f"Temps passé pour FibIt(70) : {time.time() - p} secondes")
p = time.time()
print(FibRec(70))
print(f"Temps passé pour FibRec(70) : {time.time() - p} secondes")
