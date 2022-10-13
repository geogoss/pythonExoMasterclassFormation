import random
# tri bulle (bubble sort)
# O(N^2)

#l = [4, 8, 7, 2]


# [4, 7, 2, 8] # 2
# [4, 2, 7, 8] # 1
# [2, 4, 7, 8] # 1
# [2, 4, 7, 8] # 0 => FIN

def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

def bubble_sort(l):
    nb_permut = 1
    while nb_permut != 0:
        nb_permut = 0
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                nb_permut += 1
                a = l[i]
                l[i] = l[i+1]
                l[i+1] = a
        # print(l, "#", nb_permut)

l = generate_random_list(10, 0, 10)
print("UNSORTED:", l)
bubble_sort(l)
print("SORTED:  ", l)



