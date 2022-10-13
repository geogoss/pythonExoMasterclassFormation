# Trouver les éléments manquants
#
# Entre 1 et 10 (inclus)

a = [3, 8, 2, 4, 7]

def get_missing_numbers1(l, min, max):
    missing = []
    for i in range(min, max+1):
        if i not in l:
            missing.append(i)
    return missing


def get_missing_numbers2(l, min, max):
    return [i for i in range(min, max+1) if i not in l]



print(get_missing_numbers2(a, 1, 10))
