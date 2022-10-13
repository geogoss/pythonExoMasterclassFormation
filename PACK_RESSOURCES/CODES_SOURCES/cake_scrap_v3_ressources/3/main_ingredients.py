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

liste_recettes_sauvegardees = charger_fichier_json(JSON_FILENAME)
if not liste_recettes_sauvegardees:
    print("Erreur : Aucune données")
    exit(0)

tous_les_ingredients = []
for recette in liste_recettes_sauvegardees:
    ingredients = recette["recette"]["ingredients"]
    tous_les_ingredients.extend(ingredients)

for ingredient in tous_les_ingredients:
    print(ingredient)

