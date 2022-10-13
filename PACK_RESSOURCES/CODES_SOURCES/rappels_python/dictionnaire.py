# RAPPELS PYTHON : Dictionnaire

# clef -> valeur

'''p = { "nom": "Jean", "a": 20 }

age = p.get("age")
if age:
    print("Age de la personne : " + str(age))
else:
    print("L'age n'est pas spécifié")'''

repertoire = {"Jean Dupont": {"age": 20, "tel": "0610191818"},
              "Marie Dupont": {"age": 30, "tel": "066565656"},
              "Eric Dupuis": {"age": 35, "tel": "0748484848"}
}


personne_recherchee = "Eric Dupuis"
infos = repertoire[personne_recherchee]
# print(infos)

for clef in repertoire:
    print(clef)
    print(repertoire[clef])
    