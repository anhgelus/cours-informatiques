ch = print("Entrer un texte :")
i = 0
chNew = 0
while i <= len(ch):
    if (ch[i] == "?") and (ch[i] == "!") and (ch[i] == "."):
        chNew = chNew + \n
        i = i + 2
        nb = nb + 1
    else:
        chNew = ch[i]
print(chNew, 'nb', end = '')