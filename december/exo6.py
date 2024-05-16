def nettoyer(ch: str) -> str:
    n = ""
    for i in ch.split(" "):
        if len(i) > 3:
            n += " " + i
    return n.strip()


print(nettoyer("bonjour les amies !"))
