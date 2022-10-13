# mots communs entre deux phrases

a = "bonjour je bonjour m'appelle toto"
b = "Bonjour, je suis titi"

# bonjour je
# split(" ")

#print("bonjour" in ["titi", "toto"])

def get_common_words(a, b):
    words_a = a.lower().replace(",", "").split(" ")
    words_b = b.lower().replace(",", "").split(" ")

    common_words = []

    for word in words_a:
        if word in words_b and not word in common_words:
            common_words.append(word)
    
    return common_words

def get_common_words2(a, b):
    words_a = set(a.lower().replace(",", "").split(" "))
    words_b = set(b.lower().replace(",", "").split(" "))

    #return list(words_a.intersection((words_b)))
    return list(words_a & words_b)


print(get_common_words2(a, b))
