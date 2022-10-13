from bs4 import BeautifulSoup

# Lecture des données HTML
f = open("recette.html", "r")
html_content = f.read()
f.close()
soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")  # , class_=""
paragraphe_description = soup.find("p", class_="description")
div_info = soup.find("div", class_="info")
img_info = div_info.find("img")
print("Titre de la page HTML:", titre_h1.text)
print("Paragraphe de description:", paragraphe_description.text)
print("le src de l'image est:", img_info["src"])

print()
