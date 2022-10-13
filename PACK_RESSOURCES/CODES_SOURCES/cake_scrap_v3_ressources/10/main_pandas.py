import pandas

'''data = {
    "noms": ["Jean", "Paul", "Emilie"],
    "ages": [30, 20, 25]
}

noms_et_ages = pandas.DataFrame(data)
noms_et_ages.to_csv("noms_et_ages.csv")
noms_et_ages.to_excel("noms_et_ages.xlsx")

print(noms_et_ages)'''

recettes = pandas.read_json("recette.json")
print(recettes.info())

