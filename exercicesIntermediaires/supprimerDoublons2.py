from utils import newListe



maListe = [9, 7, 4, 5, 14, 10, 6, 14, 2, 2, 20, 11, 0, 16, 15, 12, 17, 18, 13, 11]


def removeDuplicate_sort(l):
    l.sort()
    print(l)
    liste = []
    liste.append(l[0])
    for i in range(1, len(l)):
        if l[i-1] != l[i]:
            liste.append(l[i])
    return liste

print(removeDuplicate_sort(maListe))

