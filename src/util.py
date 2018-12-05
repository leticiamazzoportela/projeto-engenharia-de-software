import unidecode
import json

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
        elif (specie["status_plantlist"] != "nao_encontrado" and specie.__contains__("plantlist")):
            species_list.append(specie["plantlist"])

    return species_list

def get_list_flora_names(species):
    species_list = []
    for specie in species:
        if (specie["status_florabrasil"] != "nao_encontrado" and specie.__contains__("florabrasil")):
            species_list.append(specie["florabrasil"])
    return species_list

def get_list_plantlist_name(species):
    species_list = []
    for specie in species:
        if (specie["status_plantlist"] == "" and specie.__contains__("plantlist") and specie["status_florabrasil"] == "nao_encontrado"):
            species_list.append(specie["plantlist"])
    return species_list

def get_notfound_plants(data):
    species_list = []
    for specie in data:
        if (specie["status_florabrasil"] == "nao_encontrado" and specie["status_plantlist"] == "nao_encontrado"):
            species_list.append(specie["nome"])
    return species_list

def remove_author(specie):
    specie_token = specie.split(" ")
    return specie_token[0] + " " + specie_token[1]

def check_occurrences():
    specieslink = json.load(open("data/specieslink.json"))
    gbif = json.load(open("data/gbif.json"))

    for specie in specieslink:
        occurrences = []
        for ocurrence in specieslink[specie]:
            occurrences += ocurrence
        specieslink[specie] = occurrences
    
    with open('data/specieslink.json', 'w') as outfile:
        json.dump(specieslink, outfile)

if __name__ == "__main__":

    # data = json.load(open("data/plant_flora.json"))
    # # print(data)
    # data = get_notfound_plants(data)
    # with open('data/notfound.json', 'w') as outfile:
    #     json.dump(data, outfile)
    check_occurrences()
