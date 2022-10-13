from cake_scrap_lib import *

# 1 - Gateau au chocolat (nb_ingredients : 5) - url
def afficher_liste_recettes(recettes):
    for i in range(len(recettes)):
        recette = recettes[i]
        ingredients = recette["recette"]["ingredients"]
        print(i+1, "-", recette["titre"], "(nb_ingredients :", str(len(ingredients))+")", "-", recette["url"])

liste_recettes_sauvegardees = charger_fichier_json(JSON_FILENAME)
if not liste_recettes_sauvegardees:
    print("Erreur : Aucune données")
    exit(0)


print("Nombre de recettes:", len(liste_recettes_sauvegardees))
afficher_liste_recettes(liste_recettes_sauvegardees)


