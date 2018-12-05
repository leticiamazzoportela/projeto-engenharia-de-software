# encoding: utf-8

import requests
import json
import os
import io
import util
from config import config

DIRNAME = os.path.dirname(__file__)


def getNames(species):
    lista_nomes = []

    for specie in species:
        config.l_plant["text"] = specie
        nomes = {}

        specie_name = specie.split(" ")
        name = specie_name[0] + " " + specie_name[1]
        r = requests.get(
            'http://servicos.jbrj.gov.br/flora/taxon/' + util.normalize(name))
        dado = json.loads(r.content)
        if(r.status_code == 200):
            if(dado.get('result') == None):  # checa se há resultado para essa espécie no Flora Brasil
                nomes['status_florabrasil'] = 'nao_encontrado'
                nomes['nome'] = specie
            else:
                nomes['status_florabrasil'] = ""
                nomes['nome'] = specie
                # checa se o nome buscado é o aceito
                if(dado.get('result')[0]['taxonomicstatus'] == 'NOME_ACEITO'):
                    nomes['status_florabrasil'] = ''
                    nomes['florabrasil'] = dado.get(
                        'result')[0]['scientificname']
                else:
                    nomes['status_florabrasil'] = 'sinonimo'
                    accepted_name = dado.get(
                        'result')[0]['acceptednameusage']
                    if (accepted_name):
                        nomes['florabrasil'] = accepted_name
                    else:
                        nomes['status_florabrasil'] = 'nao_encontrato'
                        nomes['nome'] = specie
        else:
            nomes['status'] = 'nao_encontrado'
            nomes['nome'] = specie

        lista_nomes.append(nomes)

    # print(lista_nomes)

    return lista_nomes


if __name__ == "__main__":
    print(getNames([
        "Echinodorus bolivianus (Rusby) Hom-Niels",
        "Echinodorus cordifolius (L.) Griseb. ",
        "Echinodorus floribundus (Seub.) Seub.",
        "Echinodorus glandulosus Rataj",
        "Echinodorus grandiflorus (Cham. & Schltdl.) Micheli",
        "Echinodorus grisebachii Small",
        "Echinodorus lanceolatus Rataj",
    ]))
