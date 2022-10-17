

a = [1, 5, 6, 9, 11, 11, 12, 15]
b = [1, 5, 6, 6, 5, 7, 10]
c = [14, 14, 12, 11, 8, 6, 6, 6, 2, 1]
d = [1, 1, 1, 1, 1, 1]

# est-ce une série de données monotones -> qui croit ou décroit mais pas les deux

def monotone(x):
    positif = None
    negatif = None
    for i in x:
        if x[-1] - x[0] > 0:
            if positif == None or i >= positif:
                positif = i
            else:
                positif = None
                break
        else:
            if negatif == None or i <= negatif:
                negatif = i
            else:
                negatif = None
                break

            
    if positif == None and negatif == None:
        print("Ce n'est pas une série de données monotones")
    else:
        print("C'est une série de données monotones")
monotone(d)

# -----------------------------------------------------------------------------------------

# pour incrémentation que positive (changer le signe pour negative)
def is_monotone(x):
    for i in range(len(x)-1):
        if x[i] >  x[i+1]:
            return False
    return True

print(is_monotone(d))

# => encore mieux !!!!!!!!!

def monoPos(z):
    return z == sorted(z)
def monoNeg(z):
    return z == sorted(z, reverse=True)

print(monoPos(d))
print(monoNeg(d))


