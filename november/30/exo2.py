print("Saisissez le texte")
ch = input()
print("Saisissez un caractère")
x = input()

cpt = 0
sentence = 0
lastC = ""
for c in ch:
    lastC = c
    if c == x:
        cpt += 1
    elif c == " " and lastC == ".":
        sentence += 1
    
    if c == ch[len(ch)-1] and lastC != " ":
        sentence += 1
print(cpt, sentence)
