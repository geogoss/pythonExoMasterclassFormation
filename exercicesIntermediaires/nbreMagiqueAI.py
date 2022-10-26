import random


MIN = 0
MAX = 100

nbre_magique = random.randint(MIN, MAX)

# fonction qui compare le nombre n (testé) au nombre magique
def tester_le_nbreMagique(n):
    if n > nbre_magique:
        print(f"Le nombre magique est plus PETIT que : {n}")
        return -1
    elif n < nbre_magique:
        print(f"Le nombre magique est plus GRAND que : {n}")
        return 1
    print(f"Bravo, le nombre n :{n} est bien le nombre magique")
    return 0



min = MIN
max = MAX
# fonction qui permet à l'AI d'avoir de donner un nouveau nombre à tester en fonction
# de la réponse de la fonction du dessus
def demander_AI(r, last_nbre):
    global min, max

    if r == 0:
        return last_nbre

    if r == 1:
        min = last_nbre + 1

    if r == -1:
        max = last_nbre - 1
    
    if min == max:
        return min
    
    if max - min == 1:
        if min == last_nbre:
            return max
        return min

    return (min + max)//2




# ---------------------------------------------------------------------------------------

# lancement du script:
print(f"Le nombre magique est : {nbre_magique}")

n = 5
print("Je teste avec :", n)
r = tester_le_nbreMagique(n)
print()

while(r != 0):
    n = demander_AI(r, n)
    print("Je teste avec :", n)
    r = tester_le_nbreMagique(n)
    print()






