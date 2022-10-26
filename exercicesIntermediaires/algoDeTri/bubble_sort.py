


liste = [5, 9, 3, 7, 6, 15, 2]


def bubbleSort(liste):
    for i in range(len(liste) - 1, 0, -1):
        for j in range(i):
            n = liste[j]
            s = liste[j + 1]
            if n > s:
                liste[j] = s
                liste[j + 1] = n

           
print(liste)
bubbleSort(liste)
print(liste)


liste2 = [5, 9, 3, 7, 6, 15, 2]

def triAbulles(liste):
    for i in range(len(liste) - 1, 0, -1):
        for j in range(i):
            n = liste[j]
            s = liste[j + 1]
            if liste[j] > liste[j + 1]:
                liste[j + 1] = n
                liste[j] = s
    return liste


print(liste2)

print(triAbulles(liste2))

