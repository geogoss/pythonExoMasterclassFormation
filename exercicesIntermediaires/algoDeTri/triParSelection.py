import random


# liste = [5, 8, 10, 2, 1]
# liste.sort()
# print(liste)

# générer une liste aéatoire

def generer(n, min, max):
    liste = []
    for i in range(n + 1):
        e = random.randint(min, max)
        liste.append(e)

    return liste
liste = generer(15, 0, 1000)
print(liste)


def triSelection(liste):
    for cursor in range(len(liste) - 1):
        min = liste[cursor]
        index_min = cursor
        for i in range(cursor + 1, len(liste)):
            if liste[i] < min:
                min = liste[i]
                index_min = i
        liste[index_min] = liste[cursor]
        liste[cursor] = min

triSelection(liste)
print(liste)


# je recommence pour entrainement

#  v
# [5, 8, 3, 9, 6, 1]

#     v
# [1, 8, 3, 9, 6, 5]

#        v
# [1, 3, 8, 9, 6, 5]

#           v
# [1, 3, 5, 9, 6, 8]

#              v
# [1, 3, 5, 6, 9, 8]

#                 v
# [1, 3, 5, 6, 8, 9]

def selection(liste):
    for curseur in range(0, len(liste) - 1):
        # curseur = 0
        min = liste[curseur]
        index_min = curseur
        for i in range(curseur + 1, len(liste)):
            if liste[i] < min:
                min = liste[i]
                index_min = i
        liste[index_min] = liste[curseur]
        liste[curseur] = min

liste2 = generer(10, 0, 20)
print(liste2)
selection(liste2)
print(liste2)


