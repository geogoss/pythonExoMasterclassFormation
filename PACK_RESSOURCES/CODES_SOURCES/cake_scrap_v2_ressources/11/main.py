import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.cuisine-libre.org/"


def telecharger_et_sauvegarder_image(url):
    response = requests.get(url)
    filenmame = url.split("/")[-1]
    index_point_interrogation = filenmame.find("?")
    if index_point_interrogation != -1:
        filenmame = filenmame[:index_point_interrogation]
    if response.status_code == 200:
        with open(filenmame, 'wb') as f:
            f.write(response.content)


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

    '''print("Titre:", titre)
    print("Infos:", infos)
    print("Ingredients:", ingredients)
    print("Etapes:", etapes)
    print("Recette:", recette)'''

    return recette

def extraire_liste_recettes(url):
    # { "titre": "", "url": "", "url_image": "" }
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    div_recettes = soup.find("div", id="recettes")
    ul_recettes = div_recettes.find("ul", recursive=False)
    li_recettes = ul_recettes.find_all("li")

    liste_resultats = []
    for li in li_recettes:
        a = li.find("a")
        strong = a.find("strong")
        titre = nettoyer_texte(strong.text)
        url = BASE_URL + a["href"]
        img = a.find("img")
        url_image = BASE_URL + img["src"]

        recette = extraire_infos_recette(url)
        if recette:
            liste_resultats.append({"titre": titre, "url": url, "url_image": url_image, "recette": recette})

    return liste_resultats

# extraire_infos_recette("https://www.cuisine-libre.org/gateau-au-chocolat-granuleux")
# extraire_infos_recette("https://www.cuisine-libre.org/gateau-aux-pommes-entieres?lang=fr")
# extraire_infos_recette("https://www.cuisine-libre.org/tartelettes-aux-myrtilles?lang=fr")
# extraire_infos_recette("https://www.cuisine-libre.org/gateau-irlandais-de-la-toussaint?lang=fr")

liste_recettes = extraire_liste_recettes("https://www.cuisine-libre.org/boulangerie-et-patisserie?mots%5B%5D=83&lang=&max=10")
print(liste_recettes)
print(len(liste_recettes))

# données -> sérialise en JSON -> Texte
# texte -> désérialise le JSON -> données

liste_recettes_json = json.dumps(liste_recettes)
f = open("recette.json", "w")
f.write(liste_recettes_json)
f.close()

# for r in liste_recettes:
#    telecharger_et_sauvegarder_image(r["url_image"])

