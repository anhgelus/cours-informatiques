def startSpace(i: int) -> str:
    s = ""
    for j in range(i):
        s += " "
    return s

def gen(text: str, i: int, l: int) -> str:
    cross = startSpace(i)
    cross += text[i]
    for j in range(l-2*i-2):
        cross += " "
    cross += text[l-i-1]
    return cross

cross = ""

text = input("Texte à afficher sous forme d'un X : ")

l = len(text)
for i in range(l):
    v = l-2*i-2
    j = i
    if v == -1 and l%2==1:
        cross += startSpace(i) + text[i]
    else:
        if v < 0:
            j = l-i-1
        cross += gen(text, j, l)
    cross +="\n"

print(cross)

