# RAPPELS PYTHON : Les listes

# Tuples, Dictionnaires, sets
# Tableaux, Arrays, Vecteurs
# collections

# nom = "Toto"
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

ages = [20, 25, 15]
nb_noms = len(noms)

# Operations
# noms[0], noms[-1] = noms[-1], noms[0]

# tous_les_noms = ", ".join(noms)

# Completions de listes
'''len_noms = []
for nom in noms:
    len_noms.append(len(nom))'''

len_noms = [len(nom) if len(nom) > 3 else 0 for nom in noms]

print(len_noms)


