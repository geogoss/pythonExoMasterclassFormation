import random




# fonction pour générer une liste de nombre aléatoire
def newListe(n, min, max):
    liste = []
    for i in range(n):
        a = random.randint(min, max)
        liste.append(a)

    return liste


