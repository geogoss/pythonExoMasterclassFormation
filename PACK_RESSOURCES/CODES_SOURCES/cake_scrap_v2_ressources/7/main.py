import requests
from bs4 import BeautifulSoup


def nettoyer_texte(t):
    return t.replace("\xa0", " ").replace("\n", "").strip()


def extraire_duree_recette(recipe_infos_p, class_name):
    span = recipe_infos_p.find("span", class_=class_name)
    duree = span.find("time").text if span else ""
    return nettoyer_texte(duree).replace("?", "")


def extraire_infos_recette(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    license_text = soup.find("footer", id="license").text
    license_valide = "cc0" in license_text.lower() or "domaine public" in license_text.lower()
    if not license_valide:
        print("La license n'est pas CC0 ou Domaine public")
        return None

    titre = nettoyer_texte(str(soup.find("h1").contents[0]))

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

    div_ingredients = soup.find("div", id="ingredients")
    ingredients_li = div_ingredients.find_all("li", class_="ingredient")
    ingredients = [nettoyer_texte(i.text) for i in ingredients_li if not i.find("i")]

    div_preparation = soup.find("div", id="preparation")
    items_preparation = div_preparation.find_all("p")
    if len(items_preparation) == 0:
        items_preparation = div_preparation.find_all("li")
    etapes = [nettoyer_texte(i.text) for i in items_preparation]

    recette = {"titre": titre,
               "infos": infos,
               "ingredients": ingredients,
               "etapes": etapes}

    print("Titre:", titre)
    print("Infos:", infos)
    print("Ingredients:", ingredients)
    print("Etapes:", etapes)
    print("Recette:", recette)

    return recette


extraire_infos_recette("https://www.cuisine-libre.org/gateau-au-chocolat-granuleux")
# extraire_infos_recette("https://www.cuisine-libre.org/gateau-aux-pommes-entieres?lang=fr")
# extraire_infos_recette("https://www.cuisine-libre.org/tartelettes-aux-myrtilles?lang=fr")
# extraire_infos_recette("https://www.cuisine-libre.org/gateau-irlandais-de-la-toussaint?lang=fr")
