import pandas
from cake_scrap_lib import *

# titre / ingredients / url
# "beurre, 100g de sucre, " (join)

# pandas -> recettes.csv / xlsx
liste_recettes_sauvegardees = charger_fichier_json(JSON_FILENAME)
# [{"titre", "ingredients", "url"}]
recettes_a_exporter = []
for recette in liste_recettes_sauvegardees:
    ingredients = recette["recette"]["ingredients"]
    ingredients_str = ", ".join(ingredients)
    recettes_a_exporter.append({"titre": recette["titre"], "ingredients": ingredients_str, "url": recette["url"]})

recettes_a_exporter_dataframe = pandas.DataFrame(recettes_a_exporter)
# print(recettes_a_exporter_dataframe.loc[0])
recettes_a_exporter_dataframe.to_csv("recettes.csv")
recettes_a_exporter_dataframe.to_excel("recettes.xlsx")
