def corrDyslexie(s: str) -> str:
    return s.replace("ua", "au", -1)

def corrClavier(s: str) -> str:
    return s.replace("a", "$Q").replace("q", "a").replace("$Q", "q")

def valid(s: str) -> bool:
    for i in range(2,len(s)):
        if s[i-2:i-1] == s[i-1:i] and s[i-1:i] == s[i]:
            return False
    return True

def corrRepetition(s: str) -> str:
    while not valid(s):
        n = s[:2] 
        for i in range(2,len(s)):
            if not (s[i-2:i-1] == s[i-1:i] and s[i-1:i] == s[i]):
                n += s[i]
        s = n
    return s

print(corrDyslexie("tu es beua"))
print(corrClavier("aui est lq ?"))
print(corrRepetition("l'effffort est immmense"))

p = input("La phrase à corriger : ")
print(corrDyslexie(corrClavier(corrRepetition(p))))

