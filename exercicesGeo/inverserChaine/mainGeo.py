
chaine = "Bonjour Toto"

# façon avec boucle

stock = ""
for i in chaine:
    stock = i + stock
print(stock) 

# façon avec reversed()
print("".join(reversed(chaine)))


# façon avec une liste et la methode reverse()
liste =[]
for i in chaine:
    liste.append(i)
liste.reverse()
print("".join(liste))


# méthode du slice

print(chaine[::-1])

