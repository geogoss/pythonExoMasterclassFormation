

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







