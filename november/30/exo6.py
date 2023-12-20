ch = input("Entrer un texte : ")
i = 0
chNew = ""
nb = 0
while i <= len(ch):
    if (ch[i] == "?") or (ch[i] == "!") or (ch[i] == "."):
        chNew += ch[i]+"\n"
        i += 1 
        nb = nb + 1
    else:
        chNew += ch[i]
    i += 1
print(chNew, nb, sep='')
