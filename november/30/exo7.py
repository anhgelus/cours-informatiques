def compteVers(strophe: str):
    count = 1
    for i in strophe:
        if i == '\n':
            count += 1
    return count


hymne = """A la très chère, à la très belle
Qui remplit mon coeur de clarté,
A l'ange, à l'idole immortelle,
Salut en l'immortalité !"""

c = compteVers(hymne)

if c == 3:
    print("tercet")
elif c == 4:
    print("quatrain")
elif c == 5:
    print("quintil")
elif c == 6:
    print("sizain")
