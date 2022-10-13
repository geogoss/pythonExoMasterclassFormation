from cake_scrap_lib import *

# 1 - Récupérer tous les ingrédients une liste
# 2 - Néttoyer les ingrédients -> isoler le nom
'''200 g d’amandes douces  => amandes douces
200 g de sucre en poudre => sucre en poudre
3 à 4 blancs d’œufs => blancs d’œufs
3 bonnes cuillerées de gelée de pommes ou d’abricots  => gelée de pommes ou d’abricots'''
# 3 - mes_ingredients = ["sucre", "beurre", "..."]
# 4 - Algorithme pour lister les recettes correspondantes à nos ingrédients

# parcourir toutes les recettes
# tous_les_ingredients = []

def filtrer_nom_ingredient(nom_ingredient):
    # " de "
    # " d'"
    # nombre + espace
    # strip / split / find(" de ") / [:] / isdigit()
    filtre_gauche = False

    index_de = nom_ingredient.find(" de ")
    if index_de != -1:
        nom_ingredient = nom_ingredient[index_de+4:]
        filtre_gauche = True

    if not filtre_gauche:
        index_d_apostrophe = nom_ingredient.find(" d'")
        if index_d_apostrophe == -1:
            index_d_apostrophe = nom_ingredient.find(" d’")
        if index_d_apostrophe != -1:
            nom_ingredient = nom_ingredient[index_d_apostrophe + 3:]
            filtre_gauche = True

    if not filtre_gauche:
        nom_split = nom_ingredient.split(" ")
        if nom_split[0].isdigit() and nom_split[1] == "ou" and nom_split[2].isdigit():
            nom_ingredient = " ".join(nom_split[3:])
            filtre_gauche = True

    if not filtre_gauche:
        nom_split = nom_ingredient.split(" ")
        if nom_split[0].isdigit() and nom_split[1] == "g":
            nom_ingredient = " ".join(nom_split[2:])
            filtre_gauche = True

    if not filtre_gauche:
        nom_split = nom_ingredient.split(" ")
        if nom_split[0].isdigit():
            nom_ingredient = " ".join(nom_split[1:])
            filtre_gauche = True

    if not filtre_gauche:
        if nom_ingredient.startswith("du "):
            nom_ingredient = nom_ingredient[3:]
            filtre_gauche = True

    if not filtre_gauche:
        if nom_ingredient.startswith("des "):
            nom_ingredient = nom_ingredient[4:]
            filtre_gauche = True

    # filtre à droite
    index_parenthese = nom_ingredient.find("(")
    if index_parenthese != -1:
        return nom_ingredient[:index_parenthese]

    index_tiret = nom_ingredient.find(" - ")
    if index_tiret != -1:
        return nom_ingredient[:index_tiret]

    index_crochet = nom_ingredient.find(" [")
    if index_crochet != -1:
        return nom_ingredient[:index_crochet]

    return nom_ingredient

liste_recettes_sauvegardees = charger_fichier_json(JSON_FILENAME)
if not liste_recettes_sauvegardees:
    print("Erreur : Aucune données")
    exit(0)

tous_les_ingredients = []
for recette in liste_recettes_sauvegardees:
    ingredients = recette["recette"]["ingredients"]
    tous_les_ingredients.extend(ingredients)

for ingredient in tous_les_ingredients:
    nom_filtre = filtrer_nom_ingredient(ingredient)
    #if "FILTRÉ" not in nom_filtre:
    print(nom_filtre)

