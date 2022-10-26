import random

def generate(n, min, max):
    new = []
    for i in range(n):
        e = random.randint(min, max)
        new.append(e)
    return new


liste = [4, 8, 7, 2]


def bubble_sort(liste):
    inversion = True
    while inversion == True:
        inversion = False
        for i in range(len(liste)-1):
            n = liste[i]
            s = liste[i + 1]
            if n > s:
                liste[i] = s
                liste[i + 1] = n
                inversion = True


print(liste)
bubble_sort(liste)
print(liste)

# -----------------------------------------------------------------------------
# pour entrainement

liste2 = generate(15, -100, 100)

def triChewingum(liste):
    inversion = True
    while inversion:
        inversion = False
        for i in range(len(liste) - 1):
            n = liste[i]
            s = liste[i + 1]
            if liste[i] > liste[i + 1]:
                liste[i] = s
                liste[i + 1] = n
                inversion = True
    return liste

print(liste2)
print(triChewingum(liste2))





