# Trouver le mot le plus court et le plus long dans une phrase
# le premier par ordre alphabetique 

# ordre dans la phrase en premier
def get_min_and_max_words(sentense):
    words = sentense.split(" ")
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    # print(words)
    return min_word, max_word

# ordre alphabetique en premier
def get_min_and_max_words_sorted(sentense):
    words = sentense.split(" ")
    min_word, max_word = get_min_and_max_words(sentense)

    all_min_words = [w for w in words if len(w) == len(min_word)]
    all_max_words = [w for w in words if len(w) == len(max_word)]

    all_min_words.sort()
    all_max_words.sort()
    # ...
    return all_min_words[0], all_max_words[0]

def get_min_and_max_words_sorted2(sentense):
    words = sentense.split(" ")
    words.sort()
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    # print(words)
    return min_word, max_word

s = "Un aa sachant chasser sait chasser sans son chien"

min_word, max_word = get_min_and_max_words_sorted2(s)

print("Mot le plus petit:", min_word)
print("Mot le plus long:", max_word)

# split(" ")
# min max

# print(min(["aa", "aaaaaa", "zzz"], key=len))

