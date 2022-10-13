from utils import generate_random_list

'''l = generate_random_list(14, 0, 40)
l.sort()

print(l)'''

# 24
l = [1, 4, 6, 11, 12, 16, 20, 20, 22, 24, 25, 30, 33, 40]
# -> Index
# -> -1 : non trouvé

# [1, 4, 6, 7]

def binary_search(l, e, imin, imax):
    if imax-imin == 0:
        if l[imin] == e:
            return imin
        return -1
    if imax-imin == 1:
        if l[imin] == e:
            return imin
        if l[imax] == e:
            return imax
        return -1
    icenter = (imax+imin)//2
    if l[icenter] == e:
        return icenter
    if l[icenter] < e:
        return binary_search(l, e, icenter+1, imax)
    return binary_search(l, e, imin, icenter-1)

print(binary_search(l, 24, 0, len(l)-1))




