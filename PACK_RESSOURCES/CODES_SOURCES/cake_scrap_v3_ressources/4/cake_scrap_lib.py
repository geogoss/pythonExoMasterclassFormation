import os
import json

JSON_FILENAME = "recette.json"

def charger_fichier_json(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        json_data = f.read()
        f.close()
        return json.loads(json_data)
    return None

