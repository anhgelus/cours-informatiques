def compte(ch: str, c: str) -> int:
    cnt = 0
    for i in ch:
        if i == c:
            cnt += 1
    return cnt

def estAnagrame(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    for i in a:
        if compte(a,i) != compte(b,i):
            return False
    return True

a = input("Mot 1 ")
b = input("Mot 2 ")

print(estAnagrame(a,b))
