couleur = ["blanc", "jaune", "rouge", "bleu", "vert", "noir"]
print(couleur)
couleur[3] = "violet"
print(couleur, len(couleur))
couleur = [c[0].upper()+c[1:] for c in couleur]
print(couleur)
