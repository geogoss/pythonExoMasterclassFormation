# Compter les majuscules 
#
# "Bonjour Toto"
# => 2
#
# Uppercase (majuscules)
# Lowercase (minuscules)


def count_upper_characters1(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    return count

def count_upper_characters2(s):
    l = [1 for c in s if c.isupper()]
    return len(l)

s = "Bonjour toto"

# isupper
# islower

print(count_upper_characters2(s))

# print(count_upper_characters1(s))

