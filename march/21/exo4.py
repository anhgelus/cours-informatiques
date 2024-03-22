noms = ["Florian", "Léa", "Erwan", "Leila", "Ines", "Alain", "Hadi"]
notes = [2, 12, 7, 11, 20, 0, 12]
easy = [(noms[i], notes[i]) for i in range(len(noms))]  # je combine juste les deux listes en une seule avec des sous-listes
moyennes = sum(notes)/len(notes)
nice = []
i = 0
l = 0
for d in range(len(easy)):
    n = easy[d][1]
    if n > moyennes:
        nice.append(n)
        if n > l:
            i = d
            l = n
print(f"Il y a {len(nice)} étudiant qui a plus de {moyennes}. L'étudiant avec la meilleure note est {noms[i]}")
yes = []
no = []
for d in easy:
    if d[1] >= 10:
        yes.append(d[0])
    else:
        no.append(d[0])
print(f"Les élèves admis sont {yes}. Les recalés sont {no}.")
