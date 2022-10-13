import string


chaine = "Un chasseur sachant chasser sans son chien est un chasseur qui chasse bien"

def trouverLeMot(chaine):
    lePlusCourt = string.ascii_letters
    lePlusLong = ""
    lesDeux = []
    for i in chaine.split():
        if len(i) < len(lePlusCourt):
            lePlusCourt = i
        if len(i) > len(lePlusLong):
            lePlusLong = i
    lesDeux.extend([lePlusCourt, lePlusLong])
    return lesDeux

print(f"Le mot le plus court est : {trouverLeMot(chaine)[0]}") 
print(f"Le mot le plus long est : {trouverLeMot(chaine)[1]}") 





