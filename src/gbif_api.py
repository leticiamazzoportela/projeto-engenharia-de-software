from pygbif import occurrences
import json

def getOccurrences(plantsName):
    occurrences_output = []
    i = 0
    index = ['decimalLatitude', 'decimalLongitude', 'eventDate', 'country', 'stateProvince', 'locality']

    for plantName in plantsName:
        occurrences_plant = occurrences.search(scientificName=plantName, continent = 'south_america')

        occurrences_data   = {}
        occurrences_data['nome_planta']    = plantName
        occurrences_data['qtd_ocorencias'] = occurrences_plant['count']
        
        while i < occurrences_plant['count']:
            for item in enumerate(index):
                if item in occurrences_plant['results'][i].keys():
                    occurrences_data[item]  = occurrences_plant['results'][i][item]
                else:        
                    occurrences_data[item]  = 'Nada consta'

            occurrences_data   = {}
            occurrences_data['qtd_ocorencias'] = occurrences_plant['count']
            occurrences_data['nome_planta']    = plantName
            
            i = i + 1
            occurrences_output.append(occurrences_data)

    return occurrences_output


if __name__ == "__main__":
    # se preferir que print, basta descomentar
    #  print(json.dumps(getOccurrences([
    #     "Echinodorus bolivianus (Rusby) Hom-Niels"
    #     # "Echinodorus cordifolius (L.) Griseb. ",
    #     # "Echinodorus floribundus (Seub.) Seub.",
    #     # "Echinodorus glandulosus Rataj",
    #     # "Echinodorus grandiflorus (Cham. & Schltdl.) Micheli",
    #     # "Echinodorus grisebachii Small",
    #     # "Echinodorus lanceolatus Rataj",
    # ]), indent = 4))

    with open('saida_gbif.json', 'w') as f:
            json.dump(getOccurrences([
                "Echinodorus bolivianus (Rusby) Hom-Niels",
                "Echinodorus floribundus (Seub.) Seub."]), f, indent=4)