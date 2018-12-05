from pygbif import occurrences
import json
import util
from config import config


def getOccurrences(plantsName):
    occurrences_output = {}
    index = ['family', 'phylum','order','genus','species','class', 'recordedBy',
        'decimalLatitude', 'decimalLongitude',
        'eventDate', 'country', 'stateProvince', 'locality']

    for plantName in plantsName:
        config.l_plant["text"] = plantName
        occurrences_plant = occurrences.search(
            scientificName=util.remove_author(plantName), continent='south_america')
        
        # print(json.dumps(occurrences_plant,indent=4))
        occurrences_list = []
        if (occurrences_plant.__contains__('count')):
            for result in occurrences_plant['results']:
                occurrence = {}
                for item in index:
                    if result and result.__contains__(item):
                        occurrence[item] = result[item]
                    else:
                        occurrence[item] = ''

                occurrences_list.append(occurrence)

        occurrences_output[plantName] = occurrences_list
    
    return occurrences_output


if __name__ == "__main__":
    # se preferir que print, basta descomentar
     print(json.dumps(getOccurrences([
        "Echinodorus bolivianus (Rusby) Hom-Niels"
        # "Echinodorus cordifolius (L.) Griseb. ",
        # "Echinodorus floribundus (Seub.) Seub.",
        # "Echinodorus glandulosus Rataj",
        # "Echinodorus grandiflorus (Cham. & Schltdl.) Micheli",
        # "Echinodorus grisebachii Small",
        # "Echinodorus lanceolatus Rataj",
    ]), indent = 4))
    # import json
    # import util

    # valid_names = json.loads(open("data/validname.json").read())
    # # valid_names = util.get_list_of_valid_names(plantlist_data)

    # occurrences = getOccurrences(valid_names)
    # with open('data/saida_gbif.json', 'w') as f:
    #         json.dump(occurrences, f)
