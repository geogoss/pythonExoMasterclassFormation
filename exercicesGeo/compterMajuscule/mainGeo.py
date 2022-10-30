
# Compter les majuscules 
#
# "Bonjour Toto"
# => 2
#
# Uppercase (majuscules)
# Lowercase (minuscules)



phrase = "Bonjour Toto et SACHA"

def compter(phrase):
    count = 0
    for c in phrase:
        if c.isupper():
            count += 1
    print(count)
    # ou faire
    # return count
    # si on veut l'exploiter

compter(phrase)

def compte(phrase):
    l = [1 for i in phrase if i.isupper()]
    return len(l)

print(compte(phrase))




