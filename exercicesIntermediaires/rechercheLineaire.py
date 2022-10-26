import random


def generate(n, min, max):
    liste = []
    for i in range(n):
        e = random.randint(min, max)
        liste.append(e)
    return liste

liste = generate(15, -10, 10)
print(liste)

def search(liste, f):
    for i in range(len(liste)):
        if liste[i] == f:
            return i
    return -1

print(search(liste, 5))



