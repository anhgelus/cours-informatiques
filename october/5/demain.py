# -*- coding: utf-8 -*-

an = int(input('Annee courante : '))
mois = 0
jour = 0
while True:
    mois = int(input('Mois courant : '))
    if not (mois > 12 or mois < 1):
        break
    print("Mauvais mois. Il doit être compris entre 1 et 12.")

while True: 
    jour = int(input('Numéro du jour : '))
    if mois == 2:
        if ((an % 4 == 0)  and not(an % 100 == 0)) or (an % 400 == 0):
            if jour <= 29:
                break
            print("Mauvais jour. Il doit être compris entre 1 et 29.")
        else :
            if jour <= 28:
                break
            print("Mauvais jour. Il doit être compris entre 1 et 28.")
    elif mois <= 7 :
        if mois % 2 == 0 : 
            if jour <= 30:
                break
            print("Mauvais jour. Il doit être compris entre 1 et 30.")
        else : 
            if jour <= 31:
                break
            print("Mauvais jour. Il doit être compris entre 1 et 31.")
    else :
        if mois % 2 == 0 :
            if jour <= 31:
                break
            print("Mauvais jour. Il doit être compris entre 1 et 31.")
        else :
            if jour <= 30:
                break
            print("Mauvais jour. Il doit être compris entre 1 et 30.")

if mois == 2: 
    if ((an % 4 == 0)  and not(an % 100 == 0)) or (an % 400 == 0):
        nbJour = 29
    else :
        nbJour = 28
elif mois <= 7 :
    if mois % 2 == 0 : nbJour = 30
    else : nbJour = 31
else :
    if mois % 2 == 0 : nbJour = 31
    else : nbJour = 30
if jour < nbJour :
    demain = jour + 1
else : demain = 1
print('Demain, nous serons le', demain)
