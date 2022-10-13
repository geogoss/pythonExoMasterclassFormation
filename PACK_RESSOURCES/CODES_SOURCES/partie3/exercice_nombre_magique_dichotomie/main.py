import random

MIN = 1
MAX = 100
nb_magique = random.randint(MIN, MAX)
#nb_magique = 10


def deviner_nombre(n):
    if n > nb_magique:
        print("Le nombre magique est plus petit")
        return -1
    elif n < nb_magique:
        print("Le nombre magique est plus grand")
        return 1
    else:
        print("Bravo, vous avez trouvé le nombre magique")
        return 0


'''def demander_nombre_utilisateur():
    n_str = input("Rentrez le nombre magique: ")
    n = int(n_str)
    return n'''

min = MIN
max = MAX
def demander_nombre_ai(r, last_n):
    global min, max
    if r == 0:
        return last_n

    if r == 1:
        min = last_n + 1

    if r == -1:
        max = last_n - 1

    if min == max:
        return min

    if max - min == 1:
        if min == last_n:
            return max
        else:
            return min

    return (min+max)//2

print("Le nombre magique est:", nb_magique)
print()

n = 5
print("Je teste avec :", n)
r = deviner_nombre(n)
print()

while(r != 0):
    # n = demander_nombre_utilisateur()
    n = demander_nombre_ai(r, n)
    print("Je teste avec :", n)
    r = deviner_nombre(n)
    print()
    if r == 0:
        break

