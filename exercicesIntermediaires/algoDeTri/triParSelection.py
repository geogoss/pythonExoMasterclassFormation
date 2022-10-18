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



