import random
# tri rapide : Quick sort
# arr = [8, 3, 7, 9, 1, 4]


# [8, 3, 7, 9, 1, 4] - p = 4
# [3, 1, 4, 8, 7, 9] - a = 2 : petits elements
# [3, 1]    [8, 7, 9]


# [3, 1] - p = 1
# [1, 3] - a = 0

# [8, 7, 9] p = 9
# [8, 7, 9] a = 2
# [8, 7]

# [7, 8]


# [1, 3] 4 [7, 8] 9

def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

def quicksort(l):
    qsort_loop(l, 0, len(l)-1)

def qsort_loop(l, imin, imax):
    if imax-imin == 1:
        if l[imin] > l[imax]:
            '''c = l[imin]
            l[imin] = l[imax]
            l[imax] = c'''
            l[imin], l[imax] = l[imax], l[imin]
        return
    if imax-imin == 0:
        return

    p = l[imax]
    a = 0
    for i in range(imin, imax):
        if l[i] <= p:
            l[a+imin], l[i] = l[i], l[a+imin]
            a += 1
    l[a+imin], l[imax] = p, l[a+imin]
    if a != 0:
        qsort_loop(l, imin, a+imin-1)
    if imax > a+imin+1 :
        qsort_loop(l, a+imin+1, imax)


# check_ordered(l)

def check_ordered(l):
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            return False
    return True


l = generate_random_list(10000, -1000, 1000)
print("UNSORTED:", l)
quicksort(l)
print("SORTED:  ", l)
if check_ordered(l):
    print("VERIFIED")
else:
    print("ALGORITHM FAILED")





