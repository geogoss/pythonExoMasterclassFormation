import os
import json

JSON_FILENAME = "recette.json"

MES_INGREDIENTS = ["beurre", "beurre doux", "beurre doux mou", "beurre fondu", "chocolat noir", "citron",
                   "confiture d’abricots", "crème fraîche", "eau tiède", "farine", "farine blanche",
                   "farine de blé", "farine tout usage", "gingembre", "gros œuf", "huile",
                   "huile neutre", "lait", "lait tiède", "lait végétal", "miel", "pomme de terre",
                   "sel", "sel fin", "sucre", "sucre en grains", "sucre en poudre", "sucre fin",
                   "tasse de sucre", "tasse d’huile d’olive tiède", "tasse farine", "œuf",
                   "œuf battu", "œuf entier", "œufs", "œufs entiers", "œufs séparés", "beurre ramolli",
                   "chocolat à pâtisserie noir"]

def charger_fichier_json(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        json_data = f.read()
        f.close()
        return json.loads(json_data)
    return None


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


def trier_recettes_par_liste_ingredients(liste_recettes, liste_ingredients):
    # liste_recettes_sauvegardees
    #   "noms_ingredients" = []
    for recette in liste_recettes:
        ingredients = recette["recette"]["ingredients"]
        noms_ingredients = [filtrer_nom_ingredient(i).lower().strip() for i in ingredients]
        recette["noms_ingredients"] = noms_ingredients
        recette["ingredients_correspondants"] = [i for i in noms_ingredients if i in liste_ingredients]
        recette["ingredients_manquants"] = [i for i in noms_ingredients if i not in liste_ingredients]
        recette["score_correspondance_ingredients"] = len(recette["ingredients_correspondants"])-4*(len(recette["ingredients_manquants"]))
        if len(recette["ingredients_correspondants"]) == 0:
            recette["score_correspondance_ingredients"] -= 100
        if len(recette["ingredients_manquants"]) == 0:
            recette["score_correspondance_ingredients"] += 100

    liste_recettes.sort(key=lambda x: x["score_correspondance_ingredients"], reverse=True)
    return liste_recettes

