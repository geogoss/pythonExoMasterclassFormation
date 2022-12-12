from utils import newListe


# newListe(50, -50, 100)
# print(newListe(20, -10, 10))

laListe = newListe(15, 0, 20)

def removeDuplicate(l):
    sansDoublon = []
    for e in laListe:
        for i in sansDoublon:
            if i == e:
                break
        else:
            sansDoublon.append(e)
    return sansDoublon

print(removeDuplicate(laListe))




