# Inverser une chaine (Reverse)
#
# "Bonjour toto"
# "otot ruojnoB"
#
# Boucle
# Slice

def reverse_string1(str):
    r = ""
    for c in str:
        r = c + r
    return r

def reverse_string2(str):
    return s[::-1]


s = "Bonjour toto"
# print(reverse_string1(s))

print(reverse_string2(s))
