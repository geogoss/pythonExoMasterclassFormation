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

table_info = soup.find("table", class_="info")
table_info_tr = table_info.find_all("tr")
table_info_headers = table_info_tr[0].find_all("th")
table_info_data = table_info_tr[1].find_all("td")
print()
print("Informations")
for i in range(len(table_info_headers)):
    print("  ", table_info_headers[i].text, ":", table_info_data[i].text)

liste_ingredients = soup.find("div", class_="ingredients").find_all("p")

print()
print("Ingrédients")
for ingredient in liste_ingredients:
    print("  ", ingredient.text)