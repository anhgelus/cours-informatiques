def valid(s: str) -> bool:
    l = ""
    for c in s:
        if c == l:
            return False
        l = c
    return True


p = input("Phrase à clean : ")
l = ""
while not valid(p):
    n = ""
    for c in p:
        if c != l:
            n += c
        l = c
    p = n

print("Chaîne clean :", p)
