import requests
from bs4 import BeautifulSoup


def nettoyer_texte(t):
    return t.replace("\xa0", " ").strip()


def extraire_duree_recette(recipe_infos_p, class_name):
    span = recipe_infos_p.find("span", class_=class_name)
    duree = span.find("time").text if span else ""
    return nettoyer_texte(duree).replace("?", "")


def extraire_infos_recette(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titre = soup.find("h1").text

    recipe_infos_p = soup.find("p", id="recipe-infos")
    # "article-duree_preparation-1383"
    # duree_preparation = recipe_infos_p.find("time", class_=lambda x: x and x.startswith("article-duree_preparation-")).text
    duree_preparation = extraire_duree_recette(recipe_infos_p, "duree_preparation")
    duree_cuisson = extraire_duree_recette(recipe_infos_p, "duree_cuisson")
    duree_repos = extraire_duree_recette(recipe_infos_p, "duree_repos")
    methode_cuisson_a = recipe_infos_p.find("a")
    methode_cuisson = methode_cuisson_a.text if methode_cuisson_a else ""

    infos = {"duree_preparation": duree_preparation,
             "duree_cuisson": duree_cuisson,
             "duree_repos": duree_repos,
             "methode_cuisson": methode_cuisson}

    recette = {"titre": titre,
               "infos": infos,
               "ingredients": None,
               "etapes": None}

    print("Titre:", titre)
    print("Infos:", infos)

    return recette


# extraire_infos_recette("https://www.cuisine-libre.org/gateau-au-chocolat-granuleux")
# extraire_infos_recette("https://www.cuisine-libre.org/gateau-aux-pommes-entieres?lang=fr")
extraire_infos_recette("https://www.cuisine-libre.org/tartelettes-aux-myrtilles?lang=fr")
