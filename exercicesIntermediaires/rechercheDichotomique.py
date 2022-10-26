import random


def generate(n, min, max):
    liste = []
    for i in range(n):
        e = random.randint(min, max)
        liste.append(e)
    return liste

# print(generate(20, 0, 100))

liste = [7, 82, 57, 82, 94, 32, 57, 25, 25, 52, 23, 40, 46, 1, 34, 67, 83, 74, 34, 31]
# binary_search fonctionne sur une liste triée

liste.sort()
print(liste)

def binary_search(liste, f, imin, imax):
    if imax - imin == 0:
        if liste[imin] == f:
            return imin
        return -1
    if imax - imin == 1:
        if liste[imin] == f:
            return imin
        if liste[imax] == f:
            return imax
        return -1

    icenter = (imin + imax)//2
    if liste[icenter] == f:
        return icenter
    if liste[icenter] > f:
        return binary_search(liste, f, 0, icenter-1)
    return binary_search(liste, f, icenter+1, imax)

print(binary_search(liste, 40, 0, len(liste)-1))








