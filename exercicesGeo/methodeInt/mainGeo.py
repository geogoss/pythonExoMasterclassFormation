

chaine = "-234"

# nombre = int(chaine)
# nombre += 5
# print(chaine, nombre)

def transformation(chaine):
    
    chaine_convertir = chaine
    is_negative = False
    if chaine[0] == "-":
        is_negative = True
        chaine_convertir = chaine[1::]


    f = 1
    nombre = 0
    for i in range(len(chaine_convertir)-1, -1, -1):
        n = ord(chaine_convertir[i]) - ord("0")
        if n > 9 or n < 0:
            raise ValueError("Cet élément ne peut pas être converti en nombre")
        nombre += n*f
        f *= 10
    if is_negative == True:
        return -nombre    
    return nombre

a = transformation(chaine)
print(a + 6)
    



