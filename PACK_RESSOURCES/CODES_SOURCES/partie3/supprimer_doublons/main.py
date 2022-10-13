# Supprimer les doublons (remove duplicates)
#
# 1 - Comparaison linéaire (n^2)
# 2 - Tri + comparaison successive (n.Log(n))
# 3 - Dictionnaire (hash map) (n)
#
# exists
# set

from utils import generate_random_list


l = generate_random_list(400000, 0, 10000)
# print(l)

# l = [6, 5, 9, 4, 1, 7, 6, 2, 5, 1, 7, 4, 2, 10, 1, 10, 9, 1, 6, 1]

def element_in_collection(e, c):
    for a in c:
        if a == e:
            return True
    return False

# 1 - Comparaison linéaire (n^2)
def remove_duplicates_linear(l):
    u = []
    for e in l:
        if not element_in_collection(e, u):
            u.append(e)
    return u


# 2 - Tri + comparaison successive (n.Log(n))
def remove_duplicates_sort(l):
    l.sort()
    u=[]
    u.append(l[0])
    for i in range(1, len(l)):
        if l[i-1] != l[i]:
            u.append(l[i])
    return u

def remove_duplicates_hash_map(l):
    # clef -> valeur
    # d[6] = 1
    # d.get(6) -> None
    d = {}
    for e in l:
        v = d.get(e)
        if v:
            v += 1
            d[e] = v
        else:
            d[e] = 1

    r = []
    for key in d:
        r.append(key)
    
    '''for key, value in d.items():
        print(key, "->", "x"+str(value))'''
    return r

print(remove_duplicates_hash_map(l))

