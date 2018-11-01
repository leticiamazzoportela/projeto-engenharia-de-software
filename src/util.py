import unidecode


def normalize(_str):
    if(_str):
        return unidecode.unidecode(_str)
    return ""

def normalize_str(_str):
    return _str.strip().lower()

def get_list_of_valid_names(species):
    species_list = []
    for specie in species:
        if (specie["status_florabrasil"] != "nao_encontrado" and specie.__contains__("florabrasil")):
            species_list.append(specie["florabrasil"])
        elif (specie["status_plantlist"] != "nao_encontrado"and specie.__contains__("plantlist")):
            species_list.append(specie["plantlist"])

    return species_list

def remove_author(specie):
    specie_token = specie.split(" ")
    return specie_token[0] + " " + specie_token[1]

if __name__ == "__main__":
    import json

    print(get_list_of_valid_names([
        {
            "nome": "Hygrophila guianensis Nees",
            "status_florabrasil": "nao_encontrado",
            "florabrasil": "flora brasil",
            "status_plantlist": "",
            "plantlist": "plant list"
        },
        {
            "nome": "Hygrophila guianensis Nees",
            "status_florabrasil": "",
            "florabrasil": "flora brasil",
            "status_plantlist": "",
            "plantlist": "plant list"
        },
    ]))
