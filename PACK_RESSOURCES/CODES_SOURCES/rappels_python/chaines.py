# RAPPELS PYTHON : Chaines de caractères

a = "Je m'appelle " + "Tota"
a = a.lower()   # upper : majuscules / lower : minuscules
print(a)
print(len(a))
print(a[-1])
print(a[-4:])

split_a = a.split(" ")
print(split_a)

noms = ["Jean", "Paul", "Marc"]
print("-".join(noms))
print(", ".join(split_a))

print("Je m'appelle " + "toto" + str(50))  # "Je m'appelle toto"
print("Je m'appelle", 50)
