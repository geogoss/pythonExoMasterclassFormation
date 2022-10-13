# Supprimer les doublons

a = ["Jean", "Marie", "Claire", "Emilie", "Claire", "Jean", "Marc"]
# set

uniques = list(set(a))
print(uniques)

print(uniques[0])

for nom in uniques:
    print("Bonjour", nom)

