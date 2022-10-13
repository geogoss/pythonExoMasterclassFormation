import requests
from bs4 import BeautifulSoup


def extraire_infos_recette(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titre = soup.find("h1").text

    print("Titre:", titre)

    recette = {"titre": titre}

    return recette


extraire_infos_recette("https://www.cuisine-libre.org/gateau-au-miel-de-litha")
