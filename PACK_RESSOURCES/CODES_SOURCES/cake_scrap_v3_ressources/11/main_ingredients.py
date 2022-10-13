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

'''tous_les_ingredients = []
for recette in liste_recettes_sauvegardees:
    ingredients = recette["recette"]["ingredients"]
    tous_les_ingredients.extend(ingredients)

tous_les_ingredients_filtres = [filtrer_nom_ingredient(i).lower().strip() for i in tous_les_ingredients]
ingredients_uniques = list(set(tous_les_ingredients_filtres))
ingredients_uniques.sort()

for ingredient in ingredients_uniques:
    print(ingredient)'''

liste_recettes_sauvegardees = trier_recettes_par_liste_ingredients(liste_recettes_sauvegardees, MES_INGREDIENTS)

for i in range(len(liste_recettes_sauvegardees)):
    recette = liste_recettes_sauvegardees[i]
    print(i+1, "-", recette["titre"], "-", recette["url"])
    print("  Ingrédients que l'on possède:", recette["ingredients_correspondants"])
    print("  Ingrédients que l'on a pas:", recette["ingredients_manquants"])
    print("  Score ingrédients:", recette["score_correspondance_ingredients"])
    print()
