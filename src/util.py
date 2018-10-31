import unidecode


def normalize(_str):
    if(_str):
        return unidecode.unidecode(_str)
    return ""


def get_list_of_valid_names(species):
    species_list = []
    for specie in species:
        if (specie["status_florabrasil"] != "nao_encontrado"):
            species_list.append(specie["florabrasil"])
        elif (specie["status_plantlist"] != "nao_encontrado"):
            species_list.append(specie["plantlist"])

    return species_list


if __name__ == "__main__":
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
