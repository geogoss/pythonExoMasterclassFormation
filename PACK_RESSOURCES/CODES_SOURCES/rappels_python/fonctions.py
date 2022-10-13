# RAPPELS : Les fonctions

b = 10

# Fonction récursive
def demander_nom():
    nom = input("Quel est votre nom: ")
    if nom == "":
        print("ERREUR : Le nom ne doit pas être vide")
        return demander_nom()
    return nom

def afficher_nom(nom = ""):
    global b
    b = 15
    a = 5
    if nom == "":
        print("Le nom est vide")
        return
    print("Je m'appelle")
    print(nom)
    print(b)

nom_personne = demander_nom()

afficher_nom(nom_personne)

print(b)

