import string


def obtenirPos(ch: str, alpha: str) -> int:
    """
    Donne la position de la lettre ch en utilisant la base alpha
    """
    return alpha.find(ch) + 1


def obtenirLettre(p: int, alpha: str) -> str:
    """
    Récupère une lettre ch depuis sa position dans la base alpha
    """
    return alpha[p - 1]


def retireSpecial(ch: str) -> str:
    """
    Retire tous les caractères spéciaux de la chaîne de caractère ch
    """
    return ch.replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a").replace("î", "i").replace("ù",
                                                                                                                "u")


def nombre(i: int) -> str:
    """
    Retourne le chiffre chiffré
    """
    return string.punctuation[i]


def obtenirNombre(p: str) -> int:
    """
    Donne le nombre lié à la ponctuation p
    """
    return string.punctuation.find(p)


def chiffrer(msg: str, k: int, alpha: str) -> str:
    """
    Chiffre le message msg en code César d'indice k en base alpha
    """
    msg = retireSpecial(msg)
    msg = msg.replace("'", " ")
    for p in string.punctuation:
        msg = msg.replace(p, "")
    # on enlève les doubles espaces
    msg = msg.replace("  ", " ")
    nMsg = ""
    for ch in msg:
        if ch == " ":
            nMsg += " "
        else:
            if ch not in alpha:
                nMsg += nombre(int(ch))
            else:
                nMsg += obtenirLettre((obtenirPos(ch, alpha) + k) % 26, alpha)
    return nMsg


def dechiffrer(msg: str, k: int, alpha: str) -> str:
    """
    Déchiffre le message msg en code César d'indice k en base alpha
    """
    nMsg = ""
    for ch in msg:
        if ch == " ":
            nMsg += " "
        else:
            if ch in string.punctuation:
                nMsg += str(obtenirNombre(ch))
            else:
                nMsg += obtenirLettre((obtenirPos(ch, alpha) - k) % 26, alpha)
    return nMsg


def enumk(msg: str, alpha: str) -> None:
    """
    Bruteforce le message msg en base alpha
    """
    for k in range(1, 26):
        print(f"Entier utilisé : {k}")
        print(dechiffrer(msg, k, alpha))


def freqMax(msg: str, alpha: str) -> str:
    """
    Donne quelle lettre est la plus fréquente dans le message msg
    La base alpha sert juste à la base de lettre.
    """
    # on enregistre les derniers scores 
    chMax = 0
    last = ""
    # on parcourt toutes les lettres que l'on peut compter
    for ch in alpha:
        c = msg.count(ch)
        # si la lettre en cours est plus utilisée que celle sauvegardée, on remplace celle qui est sauvegardée par la lettre en cours
        if c > chMax:
            chMax = c
            last = ch
    # on renvoie la lettre la plus utilisée
    return last


def smartBruteforce(msg: str, alpha: str) -> None:
    """
    Bruteforce intelligement en base alpha le message msg en supposant que la lettre la plus fréquente est le 'e'
    """
    fMax = freqMax(msg, alpha)
    print(f"La lettre la plus utilisée est {fMax}.")
    pos = obtenirPos(fMax, alpha)
    posE = obtenirPos("e", alpha)
    k = (pos - posE) % 26
    print(f"Si on suppose que {fMax} est 'e', alors l'entier vaut {k} et la chaîne déchiffrée est donc :\n")
    print(dechiffrer(msg, k, alpha))


alpha = 'abcdefghijklmnopqrstuvwxyz'

# on affiche un petit header pour que ce soit plus jolie
print("#####################")
print("   Code de César")
print(" Par William Hergès")
print("#####################")
# on affiche une petite séparation pour que ce soit plus jolie
print("\n------------------------------------------\n")

valid = False
c = 0
while not valid:
    c = int(input("Chiffrer (1), déchiffrer (2) ou bruteforce (3) le message :\n-> "))
    valid = c > 0 and c < 4

# on affiche une petite séparation pour que ce soit plus jolie
print("\n------------------------------------------\n")

msg = input("Message (attention, les majuscules vont être transformées en minuscule) :\n-> ")
# on met juste le message en minuscule au cas où
msg = msg.lower()

valid = c == 3
k = 0
while not valid:
    k = int(input("Entier à utiliser (entre 1 et 25) :\n-> "))
    valid = k > 0 and k < 26

# on affiche une petite séparation pour que ce soit plus jolie
print("\n------------------------------------------\n")

if c == 1:
    print("Chaîne chiffrée :")
    print(chiffrer(msg, k, alpha))
elif c == 2:
    print("Chaîne chiffrée :")
    print(dechiffrer(msg, k, alpha))
elif c == 3:
    print("Bruteforce :")
    enumk(msg, alpha)
    print("\nBruteforce intelligent :")
    smartBruteforce(msg, alpha)

# on affiche une petite séparation pour que ce soit plus jolie
print("\n==========================================")
print("                Question 8")
print("==========================================\n")

print('Le mot chiffré est "partage". La valeur de k est 8.')

# on affiche une petite séparation pour que ce soit plus jolie
print("\n==========================================")
print("              Message secret")
print("==========================================\n")

messageSecret = 'xw u j ynrwc bxrpwndbnvnwc bda unb canrin yxacnb m dw rvvndkun mjwb un ")n jaaxwmrbbnvnwc mn yjarb  dw pajwm % wxra rwenabn j uj kjbn nujaprn nw mnbbxdb caxrb unccanb  luc un lxvvrbbjran jmjvbknap unb yqxcxpajyqrn nc qnbrcn  brvyun pajoorcr xd vnwjln  j u jdcan kxdc mn uj eruun sxbb u jwlrnw vjarw kancxw mnenwd larnda mn wxdenuunb nbc ynayungn mnydrb caxrb bnvjrwnb dwn vjrw purbbn j uj wdrc m rwlxvyanqnwbrkunb vrbbrenb mjwb bj kxrcn j vnbbjpnb dw jvdbnda  dw lrwpun  bxw jwlncan vdavdan j bxw xanruun  ojrb pjoon j cxr sxbb ru w h j yjb zdn md knjd mjwb uj cncn mn u qxvvn'
smartBruteforce(messageSecret, alpha)
"""
Réponse à la question 8:
    Le mot chiffré est "partage". La valeur de k est 8.
"""
