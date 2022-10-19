import random



def quick_sort(liste):
    if len(liste) <= 1:
        return liste
    
    petit = []
    grand =[]
    pivot = liste.pop()
    for i in liste:
        if i > pivot:
            grand.append(i)
        else:
            petit.append(i)
    
    return quick_sort(petit) + [pivot] + quick_sort(grand)


def generate_liste(n, min, max):
    liste = []
    for i in range(n):
        nbr = random.randint(min, max)
        liste.append(nbr)
    return liste


def verificate(tri):
    for i in range(len(tri)-1) :
        if tri[i] > tri[i+1]:
            return False
    return True



liste = generate_liste(10, -100, 100)

print(liste)

print(verificate(liste))

# tri = quick_sort(liste)

print(quick_sort(liste))


print(verificate(quick_sort(liste)))
