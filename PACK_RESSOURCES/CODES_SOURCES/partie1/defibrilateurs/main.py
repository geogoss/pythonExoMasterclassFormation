
import math

'''class Defibrilateur:
    def __init__(self, infos)
        self.id = 1
        ...

    def calculer_distance(lon, lat)'''

def get_defibrilateur(infos):
    infos_split = infos.split(";")

    d = {}

    d["id"] = infos_split[0]
    d["nom"] = infos_split[1]
    d["adresse"] = infos_split[2]
    d["tel"] = infos_split[3]

    lon_str = infos_split[4].replace(",", ".")
    lat_str = infos_split[5].replace(",", ".")

    d["lon"] = float(lon_str)
    d["lat"] = float(lat_str)

    return d

# en entrée : valeurs float en degrés

defibrilateurs = []


def get_distance(lonA, latA, lonB, latB):
    r_lonA = math.radians(lonA)
    r_lonB = math.radians(lonB)
    r_latA = math.radians(latA)
    r_latB = math.radians(latB)

    x = (r_lonB-r_lonA)*math.cos((r_latA+r_latB)/2)
    y = r_latB-r_latA

    d = (math.sqrt(x*x+y*y)) * 6371

    return d


info_defibrilateur = "1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217"

get_defibrilateur(info_defibrilateur)

distance = get_distance(3.87952263361082, 43.6071285339217, 3.879483, 43.608177)
print("distance:", distance)

