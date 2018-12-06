import unidecode
import json
from Levenshtein import distance
import datetime
from dateutil.rrule import *
from dateutil.parser import *


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

    occurrences_plant = {}
    for specie in specieslink:
        occurrences = []
        for occurrence_sl in specieslink[specie]:
            repeted = False
            for occurrence_gb in gbif[specie]:
                try:
                    # if the same guy took them both
                    if (distance(normalize_str(occurrence_sl["coletor"]), normalize_str(occurrence_gb["recordedBy"])) < 4):
                        gb_year = parse(occurrence_gb["eventDate"]).year
                        sl_year = occurrence_sl["data"].split("/")[-1]
                        # in the same year
                        if(int(gb_year) == int(sl_year)):
                            # in the same spot
                            if(occurrence_gb['decimalLatitude'] != "" and            occurrence_gb['decimalLongitude'] != "" and
                                occurrence_sl['lat'] != "" and
                                occurrence_sl['long'] != "" and
                                float(occurrence_gb['decimalLatitude']) == float(occurrence_sl['lat']) and
                                float(occurrence_gb['decimalLongitude']) == float(occurrence_sl['long'])):
                                    repeted = True
                                    print(occurrence_gb, occurrence_sl)
                                    break


                    print("ok")
                except Exception as e:
                    # print(e)
                    pass
            if not repeted:
                occurrences.append(occurrence_sl)
        occurrences_plant[specie] = occurrences
    with open('data/occurrences.json', 'w') as outfile:
        json.dump(occurrences_plant, outfile)



if __name__ == "__main__":

    # data = json.load(open("data/plant_flora.json"))
    # # print(data)
    # data = get_notfound_plants(data)
    # with open('data/notfound.json', 'w') as outfile:
    #     json.dump(data, outfile)
    check_occurrences()
