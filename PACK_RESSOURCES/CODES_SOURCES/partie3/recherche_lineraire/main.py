
from utils import generate_random_list


#l = [1, 6, 3, 7, 9, 4, 6, 7, 10, 2, 1, 7, 11]
l = generate_random_list(10, 0, 10)
print(l)
# linear_search(l, e)
# -> index de la première occurence
# -> -1 : si non trouvé.

def linear_search(l, e):
    for i in range(len(l)):
        if l[i] == e:
            return i
    return -1

print(linear_search(l, 5))

# O(N)