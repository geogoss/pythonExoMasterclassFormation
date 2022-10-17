
a = [1, 4, 7, 10]

def elements_manquant1(liste, min, max):
    b = []
    for i in range(min, max + 1):
        if i not in liste:
            b.append(i)
    return b


def elements_manquant2(liste, min, max):
    return [i for i in range(min, max + 1) if i not in liste]

print(elements_manquant2(a, 1, 10))








