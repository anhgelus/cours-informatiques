import random


def permuteMot(s: str) -> str:
    a = s[0]
    z = s[len(s) - 1:len(s)]
    av = list(range(1, len(s) - 1))
    n = ""
    for _ in range(len(av)):
        r = random.randint(0, len(av) - 1)
        n += s[av[r]]
        av.pop(r)
    return a + n + z


def permute(s: str) -> str:
    words = s.split(" ")
    n = ""
    for w in words:
        n += permuteMot(w) + " "
    return n.strip()


p = input("Phrase à permuter : ")
print(permute(p))
