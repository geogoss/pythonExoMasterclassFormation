
#1) Recherche de mots communs :


sentence1 = "Bonjour tout va bien j'ai mes dix doigts mes deux main"
sentence2 = "Bonjour les yeux encore fatigués comme tous les matins"


def mots_communs(x, y):
    a = set(x.split())
    b = set(y.split())
    commun = a.intersection(b)
    return commun

print(mots_communs(sentence1, sentence2))

# 2) recherche des mots différents

sentence3 = "Généralement, on utilise un texte en faux latin (le texte ne veut rien dire, il a été modifié), le Lorem ipsum ou Lipsum. L'avantage caca du latin est que l'opérateur sait au premier coup d'œil que la page contenant ces lignes n'est pas valide et que l'attention du lecteur n'est pas dérangée par le contenu, lui permettant de demeurer concentré sur le seul aspect, graphique."

sentence4 = "Généralement, on utilise un texte en faux latin (le texte ne veut rien dire, il a été modifié), le Lorem ipsum ou Lipsum. L'avantage, pipi du latin est que l'opérateur sait au premier coup d'œil que la page contenant ces lignes n'est pas valide et que l'attention du lecteur n'est pas dérangée par le contenu, lui permettant de demeurer concentré sur le seul aspect, graphique."

def mots_différents(x, y):
    a = list(x)
    for i in a:
        if i == "," or i == "." or i == "(" or i == ")":
            a.remove(i)
    a = set("".join(a).split())
    
    b = list(y)
    for i in b:
        if i == "," or i == "." or i == "(" or i == ")":
            b.remove(i)
    b = set("".join(b).split())
    
    different = b.difference(a)
    different2 = a.difference(b)
    lesDeux = different.union(different2)
    return lesDeux

print(mots_différents(sentence3, sentence4))

# -> plus facile bcp mieux !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def plus_simple(x, y):
    s3 = set(x.lower().replace(",", "").replace(".", "").replace("(", "").replace(")", "").split())
    s4 = set(y.lower().replace(",", "").replace(".", "").replace("(", "").replace(")", "").split())

    dif = s3.difference(s4)
    dif2 = s4.difference(s3)
    difTot = dif.union(dif2)
    return difTot
print("yes c'est ici")
print(plus_simple(sentence3, sentence4))



# -----------------------------------------------------------------------------------------



#  mots commun 2eme façon
def mots_communs2(x, y):
    e = x.split()
    f = y.split()
    motsCommun = []
    for i in e:
        if i in f:
            motsCommun.append(i)
    return motsCommun

print(mots_communs2(sentence1, sentence2))


# mots différents 2eme façon
#  si il y a des virgules, des points ou des parenthèses -> ça vient foutre la merde

def mots_differents2(x, y):
    e = x.split()
    f = y.split()
    motsCommun = []
    for i in e:
        if i not in f:
            motsCommun.append(i)
    return motsCommun

print(mots_differents2(sentence3, sentence4))





